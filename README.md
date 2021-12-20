**Source Code**: <a href="https://github.com/andreportela/qas_intrusion_detection" target="_blank">https://github.com/andreportela/qas_intrusion_detection</a>

---

This project implements the QAS Experimental Evaluation Project of MO851A_2021_S2 which is about Anomaly-Based Error / Intrusion Detection.

This repository holds the experimental code and data: web server, clients, attackers, dataset, data preparation, classification, etc.

## Requirements

Python 3.8+

This project uses a few libraries to implement the experimental aspects like:
* <a href="https://fastapi.tiangolo.com/" class="external-link" target="_blank">FastAPI</a> for the web app.
* <a href="https://www.uvicorn.org/" class="external-link" target="_blank">Uvicorn</a> for the webserver.
* <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> for the data validation on the web app.

and will use others like pandas, scikit learn, etc.

## Code Installation

```console
$ poetry install
```

## Simulate the web server running

```console
$ poetry run server
```
The uvicorn web server will start accepting requests at port 8000. The bin will be to 0.0.0.0 so external request can hit the web server.
The web server is just a simple FastAPI api which has only one http endpoint. It accepts post requests saving the received json to disk, this json simulates a medical record with a person's name, blood pressure and sugar level. It was purposefully written in a sync blocking way so the server is not that efficient.

## Simulate the web client running

```console
$ poetry run client
```
or 
```console
$ poetry run client http://192.168.15.21:8000
```
A very simple web client will start sending random medical records to the web server (obviously need to be running). It receives the webserver **IP:PORT** as an argument or tries the loopback interface by default.

This simple client uses <a href="https://github.com/joke2k/faker" class="external-link" target="_blank">Faker</a> to generate random people's names and <a href="https://docs.python.org/3.8/library/random.html" target="_blank">random lib</a> to create random info for blood pressure and sugar level. This randomization creates a variation on the data that will be sent to the server over the network. So each request will have a slightly different content and size.

This client also uses <a href="https://docs.python.org/3.8/library/random.html#random.gauss" target="_blank">gauss()</a> to randomize the interval between requests. It uses by default a gaussian distribution with a 3 seconds median and a standard deviation of 0.4 seconds. Although this strategy won't be totally reallistic simulating real clients, it will distribute the requests overtime in a way that most times the client requests are sepparated by a few seconds, and sometimes the requests will fire on time way shorter than that.

## License

This project is licensed under the terms of the MIT license.
