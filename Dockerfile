FROM python:3.7

ARG LOCAL_PATH

RUN cd $LOCAL_PATH && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY $LOCAL_PATH $LOCAL_PATH

CMD ["python", "main.py"]
