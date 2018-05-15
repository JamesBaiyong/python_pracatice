#!/bin/bash

nohup sudo uwsgi --http 0.0.0.0:80 --wsgi-file manage.py --callable app --processes 4 --threads 2 --stats 0.0.0.0:9000 >/dev/null 2>&1 &
