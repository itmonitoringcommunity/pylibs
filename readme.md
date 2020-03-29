## Development Tool
```visual studio code```

## Bulletin Service

Project includes Bulletin and SLA services for smcc.

## Other Microservice Integrations

- AuthenticationService

## Unit Test 

Run Project and enter below code to Command Prompt Console

```
python D:\\githubProjects\\BulletinService\\tests\\bulletins.py
.
.
.
```

## Installation
Operating System is **CentOS Minimal**

```
$ pwd #root
$ mkdir app
$ cd app
$ vi Dockerfile #paste project dockerfile commands
$ docker build -t bulletinservice:tag .
$ docker run -p 4004:80 bulletinservice:tag
$ docker container ls --all
```