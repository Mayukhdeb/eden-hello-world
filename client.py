from eden.client import Client
from eden.datatypes import Image

c = Client(url = 'http://127.0.0.1:5656', username= 'abraham')

config = {
    'name': 'potato',
    'number': 2233,
}

run_response = c.run(config)

fetch_response = c.fetch(token = run_response['token'])

print(f'run response: {run_response}')
print(f'fetch response: {fetch_response}')

