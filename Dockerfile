FROM python:3.10.11-slim-bullseye
WORKDIR /app
COPY . /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY .env /app/.env
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload" ]
