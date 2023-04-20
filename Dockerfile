FROM surnet/alpine-python-wkhtmltopdf:3.11.1-0.12.6-full

RUN mkdir /app

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "app.py"]
