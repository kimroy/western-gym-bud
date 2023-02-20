FROM python:3-alpine

WORKDIR /data-collection

COPY ./requirements.txt ./

RUN apk update && \
    apk add libpq && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev python3-dev && \
    python3 -m pip install -r ./requirements.txt --no-cache-dir && \
    apk --purge del .build-deps
    
COPY . .

CMD [ "python3", "./src/data/data.py"]
