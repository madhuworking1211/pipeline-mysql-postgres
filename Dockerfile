FROM python:3.7

WORKDIR /app

COPY requirments.txt /app

RUN pip install -r requirments.txt

CMD ["python","app.py","dev"]