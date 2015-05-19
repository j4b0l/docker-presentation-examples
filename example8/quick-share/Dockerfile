FROM nginx:1.7.6

COPY default.conf /etc/nginx/conf.d/default.conf
RUN rm /usr/share/nginx/html/index.html

CMD ["nginx","-g","daemon off;"]

MAINTAINER Maciej Jablonski <maciej.jablonski@arynga.com>
