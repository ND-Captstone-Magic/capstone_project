import h3
import requests

GEO='37.444572,-122.160309'


api_key= 'Z1XB-w87ksYmy5gJnj4gfLPJUJRkiyyPDLEtyjnMYy0'
url2= f'https://browse.search.hereapi.com/v1/browse?at={GEO}&limit=2&categories=700-7600-0000,700-7600-0116&apiKey={api_key}'

url_no_filter= f'https://browse.search.hereapi.com/v1/browse?at={GEO}&limit=10&apiKey={api_key}'
url_no_limit= f'https://browse.search.hereapi.com/v1/browse?at={GEO}&apiKey={api_key}'

print(url_no_limit)