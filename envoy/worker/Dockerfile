FROM python:3.6.5
RUN apt-get update && apt-get install redis-tools -y

RUN mkdir /code
WORKDIR /code
COPY Pipfile* /code/
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system --dev
COPY worker.py .

ENTRYPOINT [ "python", "worker.py" ]
