FROM php:8.2-fpm

# install nginx git python and ansible
RUN apt update \
    && apt install -y netcat nginx libnginx-mod-stream python3 python3-pip git \
    procps \
    && pip install ansible

# setup nginx
RUN mkdir -p /run/nginx
EXPOSE 8080

# setup ansible
WORKDIR /app/ansible
COPY ansible .

# setup php part
RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"
COPY php_zip.ini /usr/local/etc/php/conf.d/
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
WORKDIR /app/php/kbsbmgr
COPY php/kbsbmgr .
RUN cd /app/php/kbsbmgr && /usr/local/bin/composer install --no-dev

# setup python part
WORKDIR /app/python
COPY python/requirements.txt .
COPY python/libs/reddevil-3.0.4-py3-none-any.whl libs/
RUN pip install -r requirements.txt
COPY python/ .

# setup content part
RUN mkdir -p /app/content

# startup script
COPY startup.sh /app
CMD /app/startup.sh
