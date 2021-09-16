# Hello world with eden 
[![Docker CI](https://github.com/Mayukhdeb/eden-hello-world/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/Mayukhdeb/eden-hello-world/actions/workflows/docker-ci.yml)

A minimal example of a server running with eden. 

Server side can be run with
```
python3 server.py --use-gpu False --num-workers 4 --logfile logs.log --port 5656
```

* `--use-gpu`: set it to True if you want to test it on a GPU runtime. Defaults to `False`
* `--num-workers`: maximum number of workers to be run in parallel. Defaults to `1`
* `--logfile`: name of log file where you might want to write the logs. By default it does not create a log file.
* ` --port`: port where you want to host the endpoint. Defaults to `5656`

A minimal client example can be found on [client.py](https://github.com/Mayukhdeb/eden-hello-world/blob/master/client.py)

## Running with docker

To build from the `Dockerfile`, run:

```
nvidia-docker build . --file Dockerfile --tag eden-hello-world
```

Then to run it *without* GPU access:

```
docker run  --gpus all -p 5656:5656 --network="host" eden-hello-world --num-workers 4 --port 5656 --logfile logs.log
```

To run it *with* GPU access:

```
nvidia-docker run  --gpus all -p 5656:5656 --network="host" eden-hello-world --num-workers 4 --port 5656 --logfile logs.log --use-gpu True
```
