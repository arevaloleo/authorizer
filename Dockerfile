FROM python:3.9.15-alpine

WORKDIR /app

COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4200

CMD ["python", "app.py"]