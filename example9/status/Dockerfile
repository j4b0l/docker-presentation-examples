FROM nginx:1.7.6


RUN rm -rf /usr/share/nginx/html
RUN ln -s /data/status /usr/share/nginx/html
ADD default.conf /etc/nginx/conf.d/default.conf
VOLUME /data/status/
MAINTAINER Maciej Jablonski <maciej.jablonski@arynga.com>
