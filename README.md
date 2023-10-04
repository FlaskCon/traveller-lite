# Want to contribute?

Read the TODO [todo.md](todo.md)

Fork, then send a Pull Request.

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

### Linux

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

### Windows

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

# Email Service Setup

Add the following to your .env file. (or copy the .env-example file and rename it to .env

```text
EMAIL_DEV_MODE=1
EMAIL_USERNAME=here
EMAIL_PASSWORD=here
EMAIL_SERVER=here
EMAIL_PORT=0
```

When in development mode, make sure the EMAIL_DEV_MODE is set to 1. This will prevent the app from sending emails.

**Account confirmation and Password reset links that would usually be emailed will appear in the terminal**

# Seed the starting data

Run the following command to seed the database with the starting data, and create the admin account.

```bash
flask seed
```

The email address used doesn't need to be real, as no emails will be sent.

# Run the app

```bash
flask run
```

**Debug**

```bash
flask run --debug
```

**Run with gunicorn**

```bash
gunicorn
```

**Note:**

- gunicorn will not work under windows
- this will pick up the gunicorn.config.py file

-----

# Deployment

**Current deploy cycle:**

```
cd /var/www/flask/traveller-lite
```

```
git pull
```

```
sudo docker build -t traveller-lite:b3 .
```

```
sudo docker stop traveller-lite && sudo docker run --rm -d --network host --name traveller-lite traveller-lite:b3
```

## Working with Docker

**Build the image**

```bash
docker build -t traveller-lite:latest .
```

**Run the container**

```bash
docker run -d --name traveller-lite traveller-lite
```

The container will run on port 5000.

**Visit the containers IP to confirm**

This may be different for you.

```bash
http://172.17.0.2:5000
```

## Supervisor + Docker

The container has supervisor built in as a means to control the app as a service.

**Access the container's terminal**

```bash
docker exec -it traveller-lite /bin/sh
```

Now that you're in the container's terminal, you can use supervisorctl to control the app. First activate the virtual
environment.

```bash
source venv/bin/activate
```

The supervisor service is set to automatically start on container start.

**Check the status of the service**

```bash
supervisorctl status
```

**Stop the service**

```bash
supervisorctl stop traveller-lite
```

**Start the service**

```bash
supervisorctl start traveller-lite
```
