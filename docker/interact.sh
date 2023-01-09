#!/bin/bash

xhost +

image="image_diff"
tag="latest"

docker run \
	-it \
	--rm \
	-e "DISPLAY" \
	-v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	--gpus all \
	-v $HOME/dataset:/root/dataset \
	-v $(pwd)/..:/root/$image \
	$image:$tag
