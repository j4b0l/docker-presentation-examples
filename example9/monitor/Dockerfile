FROM ubuntu:14.04


# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables \
    libgd-perl \
    libjson-perl \
    && rm -rf /var/lib/apt/lists/*

    
# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ubuntu/ | sh
RUN apt-get install -qqy lxc-docker-1.5.0

VOLUME /data/status
VOLUME /data/environments

COPY entrypoint /usr/local/bin/
COPY monitor_environments.pl /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/entrypoint"]
CMD ["monitor"]

MAINTAINER Maciej Jablonski <maciej.jablonski@arynga.com>
