FROM python:alpine
WORKDIR /bot
RUN apk add libpq-dev gcc 
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# COPY .env .
COPY ./src/* .
CMD ["python", "main.py"]

