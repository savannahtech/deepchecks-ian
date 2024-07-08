#
FROM python:3.9

#
WORKDIR /code


COPY requirements.txt ./
#
RUN pip install --no-cache-dir -r requirements.txt
#
COPY . .
#
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 80"]