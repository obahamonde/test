FROM python:3.7

ARG LOCAL_PATH

WORKDIR /app

COPY $LOCAL_PATH /app

RUN pip install -r requirements.txt

CMD ["aiofauna", "runserver", "--livereload", "--port", "8080"]