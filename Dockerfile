FROM python:3.7.0a1-alpine3.6
LABEL maintainer="Ricardo Baltazar Chaves <ricardobchaves6@gmail.com>"
ADD . /todo
WORKDIR /todo
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]