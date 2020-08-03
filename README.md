# Datanews Python

This is a client library for python 3, built to
interact with the Datanews API. 

## Install

Use pip to install the library.

```python
pip install datanews
```

## Usage

To use the API, import and and provide the api key. Then, proceed to make
queries by calling corresponding functions of the library.

### Core API

```python
import datanews
datanews.api_key = 'API_KEY'

response = datanews.headlines(q='SpaceX')
articles = response['hits']
print(len(articles)) 
```

### Monitoring API

To create monitors use the `datanews.Monitor` object.
To retrieve monitor runs use `Monitor.latest` function and pass `run_id`. Each
run object has a `last_run_id` field, which refers to previous run, or is `None`,
if no runs were made previously (i.e. this was the first run). The runs are being
made once per hour.

```python
import datanews
datanews.api_key = 'API_KEY'

# create new monitor, pass query (list of keywords), and webhook url
monitor = datanews.Monitor.create(query='SpaceX', 'webhook'='https://webhook.site/#!/06b706c8-aee9-46ba-bacf-03d84b5c9914/4330dd69-23eb-42ab-aa03-c30a53dbb5b8/2')

# list all monitors
print(datanews.Monitor.list())

# get id of the monitor
id = monitor['id']

# list latest articles from the Monitor
articles = []
run_id = monitor.get('last_run_id', None)
done = run_id is None
while not done:
    run = datanews.Monitor.latest(run_id)
    articles.extend(run['articles'])
    run_id = run['last_run_id']
    done = run_id is None
```
