**Source Code**: <a href="https://github.com/andreportela/qas_intrusion_detection" target="_blank">https://github.com/andreportela/qas_intrusion_detection</a>

---

This project implements the QAS Experimental Evaluation Project of MO851A_2021_S2 which is about Anomaly-Based Error / Intrusion Detection.

This repository holds the experimental code and data: web server, clients, attackers, dataset, data preparation, classification, etc.

All the experiments were conducted using 2 guests (Server01 and Client01) <a href="https://www.osboxes.org/ubuntu/#ubuntu-20-04-vbox" class="external-link" target="_blank">Ubuntu 20.04 virtual machines</a> using Virtual Box 6.1.30 on a Windows 10 Pro Host 21H1.

Both VMs should run in Bridge mode with a different mac address on the network cards.

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
$ server
```
The uvicorn web server will start accepting requests at port 8000. The bin will be to 0.0.0.0 so external request can hit the web server.
The web server is just a simple FastAPI api which has only one http endpoint. It accepts post requests saving the received json to disk, this json simulates a medical record with a person's name, blood pressure and sugar level. It was purposefully written in a sync blocking way so the server is not that efficient.

## Simulate the web client running

```console
$ client
```
or 
```console
$ client http://192.168.15.21:8000
```
A very simple web client will start sending random medical records to the web server (obviously need to be running). It receives the webserver **IP:PORT** as an argument or tries the loopback interface by default.

This simple client uses <a href="https://github.com/joke2k/faker" class="external-link" target="_blank">Faker</a> to generate random people's names and <a href="https://docs.python.org/3.8/library/random.html" target="_blank">random lib</a> to create random info for blood pressure and sugar level. This randomization creates a variation on the data that will be sent to the server over the network. So each request will have a slightly different content and size.

This client also uses <a href="https://docs.python.org/3.8/library/random.html#random.gauss" target="_blank">gauss()</a> to randomize the interval between requests. It uses by default a gaussian distribution with a 3 seconds median and a standard deviation of 0.4 seconds. Although this strategy won't be totally reallistic simulating real clients, it will distribute the requests overtime in a way that most times the client requests are sepparated by a few seconds, and sometimes the requests will fire on time way shorter than that.

## Virtual Machine Setup

### Installation
```console
$ sudo apt update
$ sudo apt-get install git net-tools collectl nmap
```
- git is needed to clone this repository into the VM;
- net-tools is needed to use simple networks tools like ifconfig to discover the VM's IP address;
- nmap is a tool which will perform one kind of DoS attack;
- collectl is a monitoring tool used in the experiment;

## NMap

<a href="https://nmap.org/"  target="_blank">NMap</a> is a flexible tool to network management, scan and security evaluations. It will be used to implement DoS attacks using the <a href= "https://nmap.org/nsedoc/scripts/http-slowloris.html" target="_blank">slowloris</a> strategy. NMap is used on the client VM to perform DoS attack to the server VM.

## DoS Attack
```console
$ nmap --script http-slowloris.nse --max-parallelism 400  192.168.15.20 -p 8000
```
or
```console
$ dos  192.168.15.20
```
This bash command will trigger from the Client01 VM a fairly standard DoS attack on port 8000 to the IP 192.168.15.14. Just replace **IP** and **PORT** with the ones for Server01 VM.

## Monitoring
```console
$ collectl --all -f data_collection/dataset -P --options 2
```
or
```console
$ monitoring
```
collectl tool is a <a href="http://collectl.sourceforge.net/Documentation.html" target="_blank">monitoring tool</a> used by Linux sys admins capable of normalizing data collection rate of several metrics related to cpu consumption, memory usage, network, and disk activities. The --all option will provide XXX metrics for each datapoint.

## Ransomware Attack
```console
$ poetry run ransomware
```
This command will trigger a ransomware attack simulator which deletes a random medical_record in a loop. This script deletes files faster than client creates them by default, but it slows down every time it got no file to adapt to the client pace in testing. This script should be run in Server01 VM.

## Malware Attack
```console
$ poetry run malware_server
```
This command will trigger a malware attack simulator which receives data stoled from a victim. This script just receives data and do nothing to simulate a malware server. This script should be run in Client01 VM.

```console
$ poetry run malware_client
```
or 
```console
$ poetry run malware_client http://192.168.15.21:8000
```
This command will trigger a malware attack simulator which reads a random medical_record in a loop and send it to a malware_server. This script reads files faster than client creates them by default, but it is not a problem because it doesn't deletem them. This script should be run in Server01 VM after the malware server is up and running.
## License

This project is licensed under the terms of the MIT license.
