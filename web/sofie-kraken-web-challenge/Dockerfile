FROM php:7.4-apache

RUN apt-get update \
&& apt-get install -y \
default-mysql-server 

RUN docker-php-ext-install mysqli

RUN echo "ServerName vicctf_sqli" >> /etc/apache2/apache2.conf

COPY ./src/index.php /var/www/html/



RUN cp /usr/local/etc/php/php.ini-development /usr/local/etc/php/php.ini

# Work path
WORKDIR /tmp


EXPOSE 80


