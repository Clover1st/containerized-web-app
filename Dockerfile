FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install redis psycopg2-binary flask
CMD ["python3", "app.py"]
