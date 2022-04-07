from flask import Flask, request, abort
from requests import get
from re import search

attack='attack'
prefixUrlArr = {'http://www.', 'https://www.'}
app = Flask('__main__')

@app.route('/forword_request')
def proxy_forword_request():
  url = request.args.get('url')
  print(url)
  
  if search(attack, url):
    abort(403)
  else:
    return get(f'{url}').content

app.run(host='0.0.0.0', port=8080)