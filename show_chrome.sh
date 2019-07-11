#!/bin/bash

google-chrome --start-fullscreen --no-sandbox --user-data-dir $1 &

aplay ./wav/$2.wav
