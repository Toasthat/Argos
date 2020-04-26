#!/usr/bin/bash
ARGOS_HOME="$(git rev-parse --show-toplevel)"
#set environment variable for bash and fish if available
if [[ -z "${ARGOS_HOME}" ]]; then
    
    echo "export ARGOS_HOME=$(git rev-parse --show-toplevel)">>~/.profile

    if [ -x "$(command -v zsh)" ]; then
       echo "export ARGOS_HOME=$(git rev-parse --show-toplevel)">>~/.zprofile
    fi

    if [ -x "$(command -v fish)" ]; then
        fish -c "set -Ux ARGOS_HOME $(git rev-parse --show-toplevel)"
    fi
fi

#the facial recognition task is necessary for the base security routine
#it makes sense to download these models by default
wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_front
alface_alt.xml

wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_front
alface_default.xml

wget -P "$ARGOS_HOME/Storage/models/face_detection/" https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
