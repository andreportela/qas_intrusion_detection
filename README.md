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

## Installation

```console
$ poetry install
```

## Simulate the web server running

```console
$ poetry run server
```
The uvicorn web server will start accepting requests at port 8000. The bin will be to 0.0.0.0 so external request can hit the web server.
The web server is just a simple FastAPI api which has only one http endpoint. It accepts post requests saving the received json to disk, this json simulates a medical record with a person's name, blood pressure and sugar level. It was purposefully written in a sync blocking way so the server is not that efficient.
## License

This project is licensed under the terms of the MIT license.
