#!/bin/bash

awk -v t=$SECONDS 'BEGIN{t=int(t*1000); printf "Elapsed Time (HH:MM:SS): %d:%02d:%02d\n", t/3600000, t/60000%60, t/1000%60}'