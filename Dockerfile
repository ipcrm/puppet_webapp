# puppet_webaapp

FROM centos:latest
MAINTAINER ipcrm


COPY requirements.txt /tmp/

RUN yum install -y gcc gcc-++ \
  && curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \
  && python /tmp/get-pip.py \
  && pip install -r /tmp/requirements.txt \
  && pip install gunicorn \
  && mkdir -p /deploy/webui



COPY ./webui /deploy/webui/
WORKDIR /deploy

EXPOSE 8080
ENTRYPOINT /usr/bin/gunicorn --workers=2 webui:webui -b 0.0.0.0:8080
