FROM python:3.9-alpine

COPY requirements.txt /tmp/

RUN \
  pip install \
    --no-cache-dir \
    --prefer-binary \
    -r /tmp/requirements.txt

COPY build.schema.json /build.schema.json
COPY config.schema.json /config.schema.json
COPY lint.py /lint.py

ENTRYPOINT ["python3", "/lint.py"]
