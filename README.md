![Python application](https://github.com/django-cms/django-cms-quickstart/workflows/Python%20application/badge.svg?branch=main)

# Text Summarization Tool

This version uses Python 3.8 running and the most up-to-date versions of Django 3.1 and django CMS 3.8.

## Installation

You need to have docker installed on your system to run this project.

- [Install Docker](https://docs.docker.com/engine/install/) here.
- If you have not used docker in the past, please read this [introduction on docker](https://docs.docker.com/get-started/) here.

## Try it

```bash
docker compose build web
docker compose up -d database_default
docker compose run web python manage.py migrate
docker compose run web python manage.py createsuperuser
docker compose up -d
```

Then open http://127.0.0.1:8000 in your browser.
