FROM python:3.9
WORKDIR /app
COPY . /app
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir \
    mkl
RUN pip install -r requirements.txt
RUN apt update && \
    apt install -y bash \
                   build-essential \
                   git \
                   curl \
                   ca-certificates \
                   python3 \
                   python3-pip && \
    rm -rf /var/lib/apt/lists
RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
