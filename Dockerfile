FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY ./app /app
COPY ./model /
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 7080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7080"]
