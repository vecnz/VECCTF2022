#!/bin/bash

rm -rf test

mkdir test
cp flag.txt test
cd test

mkdir chest
mv flag.txt chest/flag.txt

# loop to run 600 times
for i in {1..600}
do
    # generate random number out of 3
    ZIP=$(shuf -i 1-3 -n 1)

    # if statement for 3 conditions
    if [ $ZIP -eq 1 ]; then
        zip -r -q chest.zip chest
    elif [ $ZIP -eq 2 ]; then
        tar -cJf chest.tar.xz chest
    else
        tar -czf chest.tar.gz chest
    fi

    rm -rf chest
    mkdir chest
    mv *.* chest/
done