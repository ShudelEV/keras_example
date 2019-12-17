FROM ufoym/deepo:cpu
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/output

COPY ./src /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt