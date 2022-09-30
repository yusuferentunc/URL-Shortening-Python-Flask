## Yusuf Eren Tunc - URL Shortening Assignment

### Requirements
- Python 3.9
- Flask
### Environment Variables
- PORT : Port number for application. Default is `5000` 
- URL_BASE : Base url for short url. Default is `http://short.est/`
### Run API
```
$ pip install -r requirements.txt
$ URL_BASE='http://short.est/' PORT=5000 python main.py
```
### Testing
```
$ pytest --verbose
```
- Test command should be executed at current folder of this README.md file