FROM python:3.10.11-slim-bullseye
WORKDIR /app
COPY . /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]
