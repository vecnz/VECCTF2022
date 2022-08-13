#!/bin/bash


# compressed file is in the test dir
cd test
# file can end in .zip, .tar.xz, or .tar.gz, get file ending
FILE_ENDING=$(ls | grep -oE '\.(zip|tar.xz|tar.gz|txt)$')

# run until file ends in .txt
while [ "$FILE_ENDING" != ".txt" ]
do

    mkdir output
    if [ $FILE_ENDING == ".zip" ]; then
        unzip -q zipped.zip -d output
    elif [ $FILE_ENDING == ".tar.xz" ]; then
        tar -xJf zipped.tar.xz -C output
    else
        tar -xzf zipped.tar.gz -C output
    fi

    rm *.*
    cp output/chest/*.* .
    rm -rf output

    FILE_ENDING=$(ls | grep -oE '\.(zip|tar.xz|tar.gz|txt)$')
done

cat flag.txt