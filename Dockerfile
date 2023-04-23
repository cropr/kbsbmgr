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
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
WORKDIR /app/kbsbmgr
COPY php/kbsbmgr .
RUN cd /app/kbsbmgr && /usr/local/bin/composer install --no-dev
RUN chown -R www-data: /app/kbsbmgr

# setup python part
WORKDIR /app/python
COPY python/requirements.txt .
COPY python/libs/reddevil-3.0.4-py3-none-any.whl libs/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY python/ .

# setup work
COPY work/kbsbcontent /app/work/kbsbcontent

# startup script
COPY startup.sh /app
CMD /app/startup.sh