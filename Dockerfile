FROM php:8.2-fpm

# install nginx git python and ansible
RUN apt update \
    && apt install -y netcat nginx python3 python3-pip git \
    && pip install ansible

RUN mkdir -p /run/nginx

# install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /app/ansible
COPY ansible .
RUN ansible-playbook configurenginx.yml

WORKDIR /app/kbsbmgr
COPY php/kbsbmgr .
RUN cd /app/kbsbmgr && /usr/local/bin/composer install --no-dev

RUN chown -R www-data: /app/kbsbmgr
COPY startup.sh /app
CMD sh /app/startup.sh