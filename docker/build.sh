#!/bin/bash

image="image_diff"
tag="latest"

docker build . \
    -t $image:$tag \
    --build-arg cachebust=$(date +%s)