#!/usr/bin/bash
ARGOS_HOME="$(git rev-parse --show-toplevel)"
#set environment variable for bash and fish if available
if [ -z "$ARGOS_HOME" ]; then

    if [ -f "$HOME/.profile" ]; then
        echo "export ARGOS_HOME=$(git rev-parse --show-toplevel)" >> ~/.profile
    else
        echo "export ARGOS_HOME=$(git rev-parse --show-toplevel)" >> ~/.bash_profile
    fi

    if [ -x "$(command -v zsh)" ]; then
       echo "export ARGOS_HOME=$(git rev-parse --show-toplevel)">>~/.zprofile
    fi

    if [ -x "$(command -v fish)" ]; then
        fish -c "set -Ux ARGOS_HOME $(git rev-parse --show-toplevel)"
    fi
fi
# create the necessary directories if they don't exists
mkdir -p "$ARGOS_HOME/Storage/models/face_detection/"
mkdir -p "$ARGOS_HOME/Storage/models/face_recognition/"
#download the necessary photos for training the facial recognition model
if [[ ! -d "$ARGOS_HOME/Storage/data/user_photos/stranger_danger" ]]; then
    mkdir -p "$ARGOS_HOME/Storage/data/user_photos/"
    wget https://www.dropbox.com/sh/873towdnuuya39k/AAAwqnFd6Gx-2ucr26kuYfnEa?dl=0
    unzip "AAAwqnFd6Gx-2ucr26kuYfnEa?dl=0" -d "$ARGOS_HOME/Storage/data/user_photos/stranger_danger"
    rm "AAAwqnFd6Gx-2ucr26kuYfnEa?dl=0"
fi
#the facial recognition task is necessary for the base security routine
#it makes sense to download these models by default
if [[ ! -f "$ARGOS_HOME/Storage/models/face_detection/haarcascade_frontalface_default.xml" ]];then
    wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml

    wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

    wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
fi

# download and setup dnn based face detection models
if [[ ! -f "$ARGOS_HOME/Storage/models/face_detection/deploy.prototxt" ]]; then
    wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/download_weights.py

    wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt

    wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/weights.meta4

    cd "$ARGOS_HOME/Storage/models/face_detection/" && python download_weights.py && rm weights.meta4 download_weights.py

    #sed 
    cd "$ARGOS_HOME/Source/argos_utils/"
fi

# download model necessary for facial recognition
if [[ ! -f "$ARGOS_HOME/Storage/models/face_recognition/nn4.small2.v1.t7" ]]; then
    wget -P "$ARGOS_HOME/Storage/models/face_recognition/" https://storage.cmusatyalab.org/openface-models/nn4.small2.v1.t7
fi

# download toml++ header only version
if [[ ! -f "$ARGOS_HOME/Source/daemon/include/toml.hpp" ]]; then
    wget -P "$ARGOS_HOME/Source/daemon/include/" https://raw.githubusercontent.com/marzer/tomlplusplus/master/toml.hpp
fi

#NOTE: fix and provide dialog to decide whether to install global or local if not already available
#if ! [ -f "$ARGOS_HOME/Frontends/node_modules/electron" ]; then
#    cd "$ARGOS_HOME/Frontends"
#    npm install electron
#    npm install python-shell
#    npm install path
#    npm install process
#fi
