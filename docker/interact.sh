#!/bin/bash

xhost +

image="image_diff"
tag="latest"
home_dir="/home/user"

docker run \
	-it \
	--rm \
	-e local_uid=$(id -u $USER) \
	-e local_gid=$(id -g $USER) \
	-e "DISPLAY" \
	-v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	--gpus all \
	-v $HOME/dataset:$home_dir/dataset \
	-v $(pwd)/..:$home_dir/$image \
	$image:$tag
