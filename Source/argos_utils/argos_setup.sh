#!/usr/bin/bash

echo "export ARGOS_HOME=$(git rev-parse --show-toplevel)">>~/.profile

if [ -x "$(command -v fish)" ]; then
    fish -c "set -Ux ARGOS_HOME $(git rev-parse --show-toplevel)"
fi

