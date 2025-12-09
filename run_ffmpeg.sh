#!/bin/bash

INPUT=$1
START=$2
END=$3
OUTPUT=$4

docker run --rm \
    -v $(pwd)/videos:/data \
    ffmpeg-container \
    -y -i /data/$INPUT \
    -ss $START -to $END \
    -c copy /data/$OUTPUT
