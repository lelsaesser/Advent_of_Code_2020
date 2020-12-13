#!/bin/zsh

filename="./solutions/03_input.txt"

sed -i '' -e 's/^/"/' $filename
sed -i '' -e 's/$/",/' $filename
