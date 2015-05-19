FROM ubuntu:14.04

RUN \
	apt-get update -qqy && \
	apt-get install -qy \
		python \
		python-pip \
		python-webpy \
	&& \
	rm -rf /var/lib/apt/lists/* \
	;

COPY counter.py /
COPY entrypoint /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entrypoint"]
CMD ["counter"]
EXPOSE 8080

MAINTAINER Maciej Jablonski <maciej.jablonski@arynga.com>
