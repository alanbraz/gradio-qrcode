FROM registry.access.redhat.com/ubi9/ubi-minimal

USER root

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN microdnf update -y
RUN microdnf --nodocs install -y python3.11 python3.11-devel python3.11-requests python3.11-pip #openssl-devel git which findutils nc bind-utils wget
RUN microdnf clean all

RUN ln -s /usr/bin/pip3.11 /usr/bin/pip; exit 0
RUN ln -s /usr/bin/python3.11 /usr/bin/python; exit 0
RUN pip install -U pip setuptools wheel

WORKDIR /usr/src/app

RUN echo "app:x:1001:1001:Default user:/usr/src/app:/bin/bash" >> /etc/passwd 

RUN chown -R 1001:0 /usr/src/app && \
    chmod -R g=u /usr/src/app

USER 1001

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 8080
ENV GRADIO_SERVER_PORT 8080

CMD python app.py
