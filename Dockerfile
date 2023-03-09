FROM python:3.8-alpine

LABEL maintainer="Dhanraj Dadhich <dhanraj.dadhich78@gmail.com>"
LABEL dockerfile-creator="Megharaj Dadhich <megharaj.dadhich@gmail.com>"

RUN addgroup -S ipvul && \
    adduser -S ipvul -G ipvul

RUN apk add --no-cache gcc musl-dev libxml2-dev libxslt-dev nmap nmap-scripts openssl

USER ipvul
WORKDIR /home/ipvul
RUN pip install ipvul-scanner

ENV PATH=/home/ipvul/.local/bin:${PATH}

ENTRYPOINT ["ipvul"]
CMD ["--help"]
