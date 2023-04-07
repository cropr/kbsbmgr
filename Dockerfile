FROM php:8.2-apache

# php dependencies
RUN apt update \
    && apt install -y \
    g++ \
    libicu-dev \
    libpq-dev \
    libzip-dev \
    zip \
    zlib1g-dev \
    && docker-php-ext-install \
    intl \
    opcache \
    pdo \
    pdo_pgsql \
    pgsql

# install git python and ansible
RUN apt install -y python3 python3-pip git \
    && pip install ansible

WORKDIR /var/www/kbsbmgr
COPY index.html /var/www/kbsbmgr/public/
COPY phptest.php /var/www/kbsbmgr/public/
COPY apache.conf /etc/apache2/sites-enabled/000-default.conf

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

EXPOSE 80