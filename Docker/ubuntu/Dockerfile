FROM ubuntu:20.04

RUN  apt-get update && apt-get install python3 pip python3-apt git -y
RUN  pip3 install git+https://github.com/centriascolocation/packages-prom-exporter.git

EXPOSE 8000

CMD ["/usr/local/bin/packages-prom-exporter"]