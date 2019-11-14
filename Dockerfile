#FROM python:3.7-stretch

FROM phusion/baseimage:v0.11

WORKDIR /Users/luiscabus/Library/Containers/com.docker.docker/Data/vms/0/Docker.raw

CMD ["/sbin/my_init"]

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/core.py" ]

#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


