FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10.9
#FROM python:3.7-slim
RUN apt update
RUN apt install -y git
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

#LOCAL DVC CONFIG
#WORKDIR /app
#COPY ./requirements.txt /app/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#COPY . /src
#COPY . /models
#EXPOSE 8000
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#REMOTE DVC CONFIG
ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD . /app
VOLUME /voldata
WORKDIR /app

RUN dvc remote modify remote access_key_id ${AWS_ACCESS_KEY_ID}
RUN dvc remote modify remote secret_access_key ${AWS_SECRET_ACCESS_KEY}
RUN dvc pull

ENV PORT 8088
EXPOSE $PORT

CMD cp -r /app/* /voldata && exec gunicorn --bind :$PORT --workers 1 --threads 8 api:app