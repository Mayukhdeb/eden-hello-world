# Hello world with eden

[![Docker CI](https://github.com/Mayukhdeb/eden-hello-world/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/Mayukhdeb/eden-hello-world/actions/workflows/docker-ci.yml)

A minimal example of a server running with eden.

## Local setup
It is recommended to use a venv or a conda env when setting up a server.

```bash
sh setup.sh
```

## Server

The server can be run with:

```
python3 server.py --num-workers 4 --logfile logs.log --port 5656 --use-gpu
```

- `--num-workers`: maximum number of workers to be run in parallel. Defaults to `1`
- `--logfile`: name of log file where you might want to write the logs. By default it does not create a log file.
- ` --port`: port where you want to host the endpoint. Defaults to `5656`
- `--use-gpu`: use it only when you want to detect and use the available GPUs. Defaults to `False`

A minimal client example can be found on [client.py](https://github.com/Mayukhdeb/eden-hello-world/blob/master/client.py)

Server assumes a redis instance is running on `localhost` (e.g. `docker run -it -p 6379:6379 redis`).

## Building and Running Server and Redis with Docker

To build from the `Dockerfile`, run:

```
nvidia-docker build . --file Dockerfile --tag eden-hello-world
```

Then to run it _without_ GPU access:

```
docker run -p 5656:5656 --network="host" eden-hello-world --num-workers 4 --port 5656 --logfile logs.log
docker run -it -p 6379:6379 redis
```

To run it _with_ GPU access:

```
nvidia-docker run  --gpus all -p 5656:5656 --network="host" eden-hello-world --num-workers 4 --port 5656 --logfile logs.log --use-gpu
docker run -it -p 6379:6379 redis
```

## Building and Running Server and Redis with docker-compose

Results and logs are mounted back to `pwd`

```
docker-compose up
```

## Demo

Server hosts a minimalistic `BaseBlock` that _takes_ a `name` and a `number`, and _produces_ the same `name` and `number` (and the `device` it ran on).

With the server started, as clients we ask the `BaseBlock` to be ran from a client.

### Testing with Python Client

Testing with the minimal example [client.py](https://github.com/Mayukhdeb/eden-hello-world/blob/master/client.py):

```bash
python3 client.py
```

Expect an output like:
```bash
run response: {'token': 'mwy7co43lb'}
fetch response: {'status': {'status': 'complete'}, 'config': {'name': 'potato', 'number': 2233, 'username': 'abraham'}, 'output': {'message': 'hello potato', 'number': 2233, 'device': 'cpu'}}
```

### Testing with Curl

Run response with `curl` (gives us a `token`).

```bash
curl http://localhost:5656/run -X POST -H "Content-Type: application/json" -d '{"name": "potato", "number": 2233, "username": "abraham"}'
```

Expect an output like:
```json
{"token":"qzk1eceyk6"}
```

Fetch response (status/output) with `curl` (by passing the `token`).

```bash
curl http://localhost:5656/fetch -X POST -H "Content-Type: application/json" -d '{"token": "qzk1eceyk6"}'
```

Expect an output like:
```json
{
  "status": {
    "status": "complete"
  },
  "config": {
    "name": "potato",
    "number": 2233,
    "username": "abraham"
  },
  "output": {
    "message": "hello potato",
    "number": 2233,
    "device": "cpu"
  }
}
```
