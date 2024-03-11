<div align="center">
<h1>MediSearch - Backend</h1>
<p> Welcome to the MediSearch Backend repository. This repository contains the backend code for the MediSearch project </p>
</div>

## Table of Contents
- [Technologies](#technologies)
- [Getting Started](#getting_started)
- [Usage](#usage)


## Technologies <a name = "technologies"></a>
- [django](https://www.djangoproject.com/)
- [django-rest-framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Getting Started <a name = "getting_started"></a>
To get started with the project, you need to have the following installed on your local machine:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Usage <a name = "usage"></a>
To run the project, you need to have Docker and Docker Compose installed on your local machine. Once you have these installed, you can run the following commands to start the project:

```bash

# mkdir MediSearch

$ git clone https://github.com/Eliezir/MediSearch-backEnd

$ git clone https://github.com/Eliezir/MediSearch-frontEnd

```
create a docker-compose.yml file in the root of the project and add the following content:
version: "3.8"

```bash

include:
  "./frontend/docker-compose.yml"
  "./backend/docker-compose.yml"

```

 Then go to your backend folder, and in your docker-compose.yml file, add your database credentials in the environment section of the db service. Then, go to your database and import the csv file in the data folder. Then run the following command to start the project:

```bash

$ docker-compose up -d --build

```

<sub>Made with 💜 by <a href="https://github.com/Eliezir">Eliezir Neto</a> </sub>
