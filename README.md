# Hello world with eden 

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