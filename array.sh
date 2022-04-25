#!/bin/bash

NAME[0]="MANISH"
NAME[1]="IS"
NAME[2]="A"
NAME[3]="GOOD"
NAME[4]="BOY"
echo  ${NAME[0]}
echo "second index: ${NAME[1]}"
echo ${NAME[*]}
echo ${NAME[@]}
NUM=(1 2 3)
echo ${NUM[0]}+${NUM[1]}+${NUM[2]}
