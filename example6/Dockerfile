FROM ubuntu:14.04

RUN apt-get update -qqy && apt-get -qy install vim
RUN useradd dummy
RUN mkdir -p /data/workdir

COPY entrypoint /

#ADD http://j4b0l.com/filetoadd.tar.gx

ENV JAVA_HOME=/opt/java

VOLUME /usr/local/bin
VOLUME ["/bin","/sbin"]

EXPOSE 8080
EXPOSE 80 443 12345

WORKDIR /data/workdir

USER dummy

ENTRYPOINT ["/entrypoint"]

CMD ["sleep", "30"]

MAINTAINER Maciej Jablonski <maciej.jablonski.1985@gmail.com
