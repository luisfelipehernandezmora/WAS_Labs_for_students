FROM php:8.1-apache
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y lsb-release
COPY dbase.sql /dbase.sql
ENV DB_HOST=127.0.0.1
ENV DB_PORT=3306
ENV DB_USER=player
ENV DB_PASS=Player123!
ENV DB_NAME=webpage
ENV DB_ADMIN_USER=root
ENV DB_ADMIN_PASS=root
ENV DEBIAN_FRONTEND=noninteractive


RUN docker-php-ext-install mysqli
RUN apt-get install wget
RUN apt-get install gnupg -y
RUN wget https://dev.mysql.com/get/mysql-apt-config_0.8.23-1_all.deb
RUN dpkg -i mysql-apt-config_0.8.23-1_all.deb
RUN apt update -y
RUN apt-get install mysql-server -y


WORKDIR /var/www/html
COPY . .
RUN chmod 777 dbase.sh
EXPOSE 3000

ENTRYPOINT [ "./dbase.sh" ]

