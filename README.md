# Table of Contents

<!-- TOC -->
* [Want to contribute?](#want-to-contribute)
* [Setup](#setup)
  * [Linux](#setup--linux)
  * [Windows](#setup--windows)
  * [.env](#setup--env)
  * [Seed the database](#setup--seed-the-database)
* [Running Locally](#running-locally)
* [Deployment](#deployment)
  * [Setup Docker Environment](#deployment--setup-docker-environment)
  * [Working With Docker](#deployment--working-with-docker)
    * [docker-compose](#--working-with-docker--docker-compose)
    * [supervisord](#--working-with-docker--supervisord)
    * [Switching to debug mode](#--working-with-docker--switching-to-debug-mode)
<!-- TOC -->
---

# Want to contribute?

Read the TODO [todo.md](todo.md)

Fork, then send a Pull Request.

---

# Setup

(This assumes you have Python installed)

1. Download or Clone this repository.
2. Open terminal (Linux) / powershell (Windows) and cd to the directory of the project.

```text
# Linux
cd /path/to/traveller-lite

# Windows
cd C:\path\to\traveller-lite
```

---

## Setup / Linux

**Create a virtual environment and activate it.**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

---

## Setup / Windows

**Create a virtual environment and activate it.**

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

---

## Setup / .env

Copy the included .env.example file and rename it to .env, this file
contains the environment variables that the app needs to run.

Change the values to suit your local environment.

Here's an example:

`Note:` It is important to set both the SUPER_ADMIN_ACCOUNT and SUPER_ADMIN_PASSWORD
before using the seed CLI command.

The email address used for the SUPER_ADMIN_ACCOUNT
doesn't need to be a real email address. `admin@admin.local` is fine.

`Note:` When in development mode, make sure the EMAIL_DEV_MODE is set to 1.
This will prevent the app from trying to send emails.

```text
# SECRET_KEY is passed to Flask.config['SECRET_KEY']
SECRET_KEY=flaskcon

# The following are used for sending emails, 
# see app/extensions/__init__.py & app/utilities/email_service.py
EMAIL_DEV_MODE=1
EMAIL_USERNAME=none
EMAIL_PASSWORD=none
EMAIL_SERVER=none
EMAIL_PORT=0

# Super admin account details that will be used in the CLI
# command 'flask seed'
SUPER_ADMIN_ACCOUNT=none
SUPER_ADMIN_PASSWORD=none

# Used to populate the docker.config.toml file when using
# a postgres Docker deployment.
POSTGRES_USER=postgres
POSTGRES_PASSWORD=none
POSTGRES_DB=flaskcon
POSTGRES_PORT=5432
POSTGRES_LOCATION=localhost
```

**Account confirmation and Password reset links that would usually be emailed will appear in the terminal**

---

## Setup / Seed the database

Run the following command to seed the database with the starting data, and create the admin account.

```bash
flask seed
```

---

# Running Locally

```bash
flask run
```

**Debug**

```bash
flask run --debug
```

**Run with gunicorn**

`Note:` gunicorn will get run conditions from `gunicorn.config.py`

```bash
gunicorn
```

**IMPORTANT:**

- gunicorn will not work under Windows, use WSL or a Linux VM.

-----

# Deployment

Docker is used for deployments, make sure you have Docker installed.

## Deployment / Setup Docker Environment

`Note:` Instructions are for a debian based distro.
The instructions below also work for Windows Subsystem for Linux (WSL) Ubuntu.

```bash
sudo apt update
```

```bash
sudo apt install curl
```

```bash
sudo apt install git
```

```bash
curl -fsSL https://get.docker.com/ | sh
```

```bash
sudo groupadd docker
```

```bash
sudo usermod -aG docker $USER
```

**Important:** You will need to log out and log back in for the group changes to take effect.
Or restart to be sure.

Navigate to a folder of your choice and clone the repository.

```bash
sudo git clone git@github.com:FlaskCon/traveller-lite.git
````

---

## Deployment / Working With Docker

There is a choice of different docker-compose files.

`docker-compose.yml` is the default, and will run the app with a postgres database.

`docker-compose-sqlite.yaml` will run the app with a sqlite database.

`docker-compose-sqlite-dev.yaml` will run the app with a sqlite database, but run Flask in debug mode.

`Note:` Each database has persistent storage, so you can stop and start the containers without losing data.

**important:** The containers are set up to use the host network, so the app will be accessible on the host's IP.

---

### ... / Working With Docker / docker-compose

**Starting the containers**

Working from the location of the cloned repository, run the following command:

```bash
docker-compose -f <COMPOSE FILE CHOICE> up --build -d
```

`--build` will instruct docker-compose to rebuild the image.

`-d` will run the containers in the background.

The name of the container will be `traveller-lite`, this is pulled from the `container_name` in the docker-compose file.

**Stopping the containers**

```bash
docker-compose -f <COMPOSE FILE CHOICE> down
```

---

### ... / Working With Docker / supervisord

Supervisor is used to control the app as a service. This allows the Docker container to be stopped and started without

The following command will allow you to access the container's terminal.

```bash
docker exec -it traveller-lite /bin/sh
```

You can then use the following commands to manage the app.

**Show the status of the app**

```bash
supervisorctl status
```

**Stop the app**

```bash
supervisorctl stop traveller-lite
```

**Start the app**

```bash
supervisorctl start traveller-lite
```

**Restart the app**

```bash
supervisorctl restart traveller-lite
```

### ... / Working With Docker / Switching to debug mode

```bash
supervisorctl stop traveller-lite
```

```bash
flask run --host=0.0.0.0 --debug
```

`ctl+c` to stop the app.

```bash
supervisorctl start traveller-lite
```