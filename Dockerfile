FROM python:3.11-alpine

WORKDIR /bot

RUN apk add libpq-dev gcc

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY .env .

COPY ./src ./src

CMD ["python", "src/main.py"]
