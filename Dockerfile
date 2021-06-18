FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY gh_action_demo/ .

CMD [ "python3", "app.py" ]