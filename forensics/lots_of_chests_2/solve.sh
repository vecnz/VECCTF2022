#!/bin/bash


# compressed file is in the test dir
cd test
# file can end in .zip, .tar.xz, or .tar.gz, get file ending
FILE_ENDING=$(ls | grep -oE '\.(zip|tar.xz.cpt|tar.gz.cpt|txt)$')

# run until file ends in .txt
while [ "$FILE_ENDING" != ".txt" ]
do

    mkdir output
    if [ $FILE_ENDING == ".zip" ]; then
        unzip -P hunter12 -q chest.zip -d output
    elif [ $FILE_ENDING == ".tar.xz.cpt" ]; then
        ccdecrypt --key hunter12 --key2 hunter12 chest.tar.xz.cpt
        tar -xJf chest.tar.xz -C output
    else
        ccdecrypt --key hunter12 --key2 hunter12 chest.tar.gz.cpt
        tar -xzf chest.tar.gz -C output
    fi

    rm *.*
    cp output/chest/*.* .
    rm -rf output

    FILE_ENDING=$(ls | grep -oE '\.(zip|tar.xz.cpt|tar.gz.cpt|txt)$')
done

cat flag.txt