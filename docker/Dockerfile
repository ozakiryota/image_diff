########## Pull ##########
FROM nvidia/cuda:11.6.2-base-ubuntu20.04
########## Non-interactive ##########
ENV DEBIAN_FRONTEND=noninteractive
########## Common Tools ##########
RUN apt-get update && \
    apt-get install -y \
	    vim \
    	wget \
    	unzip \
    	git \
		python3-tk
########## Dependencies ##########
RUN apt-get update && \
    apt-get install -y \
	    python3-pip \
		libgl1-mesa-dev \
		libgtk2.0-dev \
		imagemagick && \
	pip3 install \
		opencv-python \
		pillow \
		matplotlib
########## Cache Busting ##########
ARG cachebust=1
########## image_diff ##########
RUN mkdir -p /home/user && \
	cd /home/user && \
	git clone https://github.com/ozakiryota/image_diff.git
########## User ##########
RUN apt-get update && \
	apt-get install -y gosu
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
########## Initial Position ##########
WORKDIR /home/user/image_diff
CMD ["bash"]