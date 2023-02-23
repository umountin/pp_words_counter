FROM python:3.10.10-alpine3.16 AS builder

# Upgrade pip
RUN apk update
RUN pip install --upgrade pip

# Get curl for healthchecks
RUN apk add curl

# Permissions and nonroot user for tightened security
RUN adduser -D nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app
USER nonroot

# Copy all the files to the container
COPY --chown=nonroot:nonroot . .

# Venv
ENV VIRTUAL_ENV=/home/app/venv

# Python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

# Mount an app under a URL prefix
ENV SCRIPT_NAME=/api/v1.0

EXPOSE 8080

CMD ["python3", "app.py"]
