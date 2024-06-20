FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
 	bash \
 	bc \
 	gnuplot \
	gpg-agent \
 	locales \
 	python3-pandas \
 	python3-seaborn \
	python3-selenium \
	software-properties-common \
	xvfb \
	wget \
 	yamllint

RUN sed -i "s/# en_US\.UTF-8 UTF-8/en_US\.UTF-8 UTF-8/" /etc/locale.gen
RUN locale-gen
RUN dpkg-reconfigure locales

# Firefox and geckodriver
RUN add-apt-repository -y ppa:mozillateam/ppa
COPY apt-mozilla-firefox /etc/apt/preferences.d/mozilla-firefox
RUN apt update && apt install -y firefox
RUN wget "https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz" && \
	tar -xvf geckodriver-v0.34.0-linux64.tar.gz -C /usr/bin && \
	rm geckodriver-v0.34.0-linux64.tar.gz
