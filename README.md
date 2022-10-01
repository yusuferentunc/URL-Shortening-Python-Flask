## Yusuf Eren Tunc - URL Shortening Assignment

### Requirements
- Python 3.9
- Flask
### Endpoints
### `/encode`
- Encodes long url to a short url
- Accepts POST method only
- Input format is json as like `{"url":"http://example.org/longurl"}`
- Output format is json as like `{"result":"http://shorturl.org/shortcode"}`
### `/decode` 
- Decodes short url to original url
- Accepts POST method only 
- Input format is json as like `{"short_url":"http://shorturl.org/shortcode"}`
- Output format is json as like `{"result":"http://example.org/longurl"}`
### Environment Variables
- PORT : Port number for application. Default is `5000` 
- URL_BASE : Base url for short url. Default is `http://short.est/`
### Run API
```
$ pip install -r requirements.txt
$ URL_BASE='http://short.est/' PORT=5000 python3 main.py
```
### Testing
```
$ python3 -m pytest --verbose
```
- Test command should be executed at current folder of this README.md file