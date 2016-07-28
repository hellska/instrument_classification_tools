#!/bin/bash

folder=$1
folder_root=$(basename $folder)
xtractor='/Volumes/ssdData/virtualenv/py27_nsp/bin/essentia_streaming_extractor_freesound'

if [ -z $folder ];then
	echo "Usage: "$(basename $0)" <dataset_folder>"
	exit 1
fi
ls -d $folder
if [ $? -ne 0 ];then
	echo "Provide a valid folder name"
	exit 1
fi

if [ ! -d $folder"/annotation" ];then
   mkdir -p $folder"/annotation"
else
   echo "The annotation folder already exists"
fi

cd $folder"/annotation"
pwd
dirlist=$(find $folder -type d|egrep -v 'annotation'|xargs)
for dir in $dirlist
    do
	dirname=$(basename $dir)
	if [ $dirname != $folder_root ];then
	    echo "Analysis of folder ... "$dir
            mkdir `basename $dir`
            if [ $? -eq 0 ];then
                dircontent=`ls -c1 $dir|xargs`
                for item in $dircontent; do
                    namenoext=`echo $item|cut -d"." -f1`
                    echo $xtractor $dir"/"$item "./"$dirname"/"$namenoext".json"
                    $xtractor $dir"/"$item "./"$dirname"/"$namenoext".json"
                done
             fi
	fi
        
done


# $xtractor
