FROM python:3.11.0-slim-buster

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install -r /code/requirements.txt

COPY ./app /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
