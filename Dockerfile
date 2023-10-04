FROM python:3.10-slim-buster

EXPOSE 8080

WORKDIR /code
COPY requirements.txt /code/

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 wget

COPY . /code/

RUN pip3 install -r requirements.txt
# RUN wget -P /home/.cache/torch/hub/checkpoints/ https://download.pytorch.org/models/vgg19-dcbb9e9d.pth

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]