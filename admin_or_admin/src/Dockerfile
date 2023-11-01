FROM python:3.10

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install sqlite3 -y
RUN mkdir /app
WORKDIR /app
RUN pip3 install flask
COPY . .
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "login.py" ]




