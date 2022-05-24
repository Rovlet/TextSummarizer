FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04
WORKDIR /app
COPY . /app

ARG PYTORCH_VERSION=''

RUN apt update &&\
    apt install -y bash\
                #    build-essential \
                #    libsndfile1-dev \
                #    tesseract-ocr \
                #    espeak-ng \
                   git \
                #    curl \
                #    ca-certificates \
                #    ffmpeg \
                   python3 \
                   python3-pip && \
    python3 -m pip install --no-cache-dir --upgrade pip &&\
    python3 -m pip install --no-cache-dir mkl &&\
    python3 -m pip install -r requirements.txt
    # git clone https://github.com/huggingface/transformers &&\
    # cd transformers &&\
    # git checkout main &&\
    # python3 -m pip install --no-cache-dir -e ./transformers[dev-torch,testing]

RUN [ '${#PYTORCH_VERSION}' -gt 0 ] && VERSION='torch=='$PYTORCH_VERSION'.*' || VERSION='torch'; python3 -m pip install --no-cache-dir -U $VERSION
RUN python3 -m pip uninstall -y tensorflow flax &&\
    python3 -m pip install --no-cache-dir torch-scatter -f https://data.pyg.org/whl/torch-$(python3 -c "from torch import version; print(version.__version__.split('+')[0])")+cu102.html &&\
    python3 -m pip install --no-cache-dir git+https://github.com/facebookresearch/detectron2.git pytesseract https://github.com/kpu/kenlm/archive/master.zip &&\
    python3 -m pip install -U "itsdangerous<2.1.0"
    # cd transformers &&\
    # python3 setup.py develop

# RUN rm -rf /var/lib/apt/lists
RUN python3 manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
