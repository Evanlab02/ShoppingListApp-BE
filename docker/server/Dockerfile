FROM python:3.11.6-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY version.txt src/version.txt

WORKDIR /src

COPY authentication /src/authentication
COPY stores /src/stores
COPY items /src/items
COPY shoppingapp /src/shoppingapp

EXPOSE 80

CMD ["gunicorn","-b" ,"0.0.0.0:80", "-w" ,"4" ,"--worker-class" ,"uvicorn.workers.UvicornWorker", "'shoppingapp.config.asgi:main()'"]
