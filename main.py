import os
import random
import validators
from flask import Flask, jsonify, request, abort

urls = {}

url_base = os.environ.get('URL_BASE', 'http://short.est/')


def encoding(url_id):
    """Base36 Encoding"""
    if not isinstance(url_id, int) or url_id <= 0:
        return None
    table = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ''
    while url_id > 0:
        result += table[url_id % 36]
        url_id //= 36
    return url_base + result[::-1]


def decoding(short):
    """Base36 Decoding"""
    if not isinstance(short, str):
        return None
    result = 0
    for character in short:
        if ord('a') <= ord(character) <= ord('z'):
            result = result * 36 + (ord(character) - ord('a')) + 10
        else:
            result = result * 36 + (ord(character) - ord('0'))
    return result


def id_generate():
    """Id Generation"""
    number = random.randint(36 ** 2, 36 ** 5 - 1)
    while urls.get(str(number)) is not None:
        number = random.randint(36 ** 2, 36 ** 5 - 1)
    return number


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(config or {})

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error=str(e)), 400

    @app.route("/encode", methods=['POST'])
    def encode_url():
        """Encoding URL"""
        data = request.json
        if not isinstance(data, dict):
            abort(400, description="Invalid JSON")
        url = data.get('url')
        if url is None or not validators.url(url):
            abort(400, description="Invalid URL")
        url_id = id_generate()
        encoded_url = encoding(url_id)
        urls[url_id] = data.get('url')
        return jsonify({'result': encoded_url})

    @app.route("/decode", methods=['POST'])
    def decode_url():
        """Decoding URL"""
        data = request.json
        if not isinstance(data, dict):
            abort(400, description="Invalid JSON")
        short_url = data.get('short_url')
        if short_url is None or not validators.url(short_url) or short_url[:len(url_base)] != url_base:
            abort(400, description="Invalid URL")
        url_id = decoding(short_url[len(url_base):])
        url = urls.get(url_id)
        return jsonify({'result': url})

    return app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
