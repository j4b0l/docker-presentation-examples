#!/bin/bash

HOSTDIR=$(pwd)
CONTDIR='/share'
HOSTPORT=80
CONTPORT=80

docker run --name quick-share -p $HOSTPORT:$CONTPORT -v $HOSTDIR:$CONTDIR -ti --rm j4b0l/quick-share:latest
