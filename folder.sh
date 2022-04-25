#!/bin/bash
p=`pwd`
cd $p/$1
find -empty > ../$2
