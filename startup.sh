#!/bin/bash

pushd /app/ansible && \
    ansible-playbook setupserver.yml -e git_token=$GIT_TOKEN && \
    popd

gunicorn -c /app/python/gunicorn.conf.py reddevilmgr.main:app

php-fpm -D
while ! nc -w 1 -z 127.0.0.1 9000; do sleep 0.1; done;

nginx
