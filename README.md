## Yusuf Eren Tunc - URL Shortening Assignment

### Requirements
- Python 3.9
- Flask
### Endpoints
### `/encode`
- Encodes long url to a short url
- Accepts POST method only
- Accepts only json as input. json format is `{"url":"http://example.org/longurl"}`
- Returns json as output. json format is `{"result":"http://shorturl.org/shortcode"}`
### `/decode` 
- Decodes short url to original url
- Accepts POST method only 
- Accepts only json as input. json format is `{"short_url":"http://shorturl.org/shortcode"}`
- Returns json as output. json format is `{"result":"http://example.org/longurl"}`
### Environment Variables
- PORT : Port number for application. Default is `5000` 
- URL_BASE : Base url for short url. Default is `http://short.est/`
### Run API in Development
```
$ pip install -r requirements.txt
$ URL_BASE='http://short.est/' PORT=5000 python3 main.py
```
### RUN API in Production
```
$ pip install -r requirements.txt 
$ pip install waitress
$ export URL_BASE='http://short.est/'
$ waitress-serve --port=8080 --host=0.0.0.0 --call 'main:create_app'
```
### Testing
```
$ python3 -m pytest --verbose
```
- Test command should be executed at current folder of this README.md file