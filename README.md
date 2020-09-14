# Datanews Python

This is a client library for python 3, built to
interact with the Datanews API. You can find full api documentation
at [official documentation page](https://datanews.io/docs).

## Install

Use pip to install the library.

```python
pip install datanews
```

## Usage

To use the API, import the `datanews` package and provide the api key. Then, proceed to make
queries by calling corresponding functions of the library.

### Core API

```python
import datanews
datanews.api_key = 'API_KEY'

response = datanews.headlines(q='SpaceX')
articles = response['hits']
print(articles[0]['title']) 
```

### Monitoring API

To create monitors use the `datanews.Monitor` object.
To retrieve monitor runs use `Monitor.latest` function and pass `run_id`. Each
run object has a `last_run_id` field, which refers to previous run, or `None`,
if no runs were made previously (i.e. this was the first run). Please refer to
to [full documentation](https://datanews.io/docs/monitoring-overview) of monitoring API.

```python
import datanews
datanews.api_key = 'API_KEY'

# list all monitors
print(datanews.Monitor.list())

# create new monitor, pass query (list of keywords), and webhook url
monitor = datanews.Monitor.create(query='SpaceX', 'webhook'='https://mywebhook.com')

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
