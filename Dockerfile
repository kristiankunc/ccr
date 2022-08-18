ARG DISCORD_TOKEN

FROM python:3.10-alpine

COPY . /

RUN pip install -r requirements.txt

CMD ["python", "./main.py", "$DISCORD_TOKEN"]