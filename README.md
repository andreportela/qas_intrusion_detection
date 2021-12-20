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

## License

This project is licensed under the terms of the MIT license.
