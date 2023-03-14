FROM python:3.7

RUN pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]

# Path: requirements.txt