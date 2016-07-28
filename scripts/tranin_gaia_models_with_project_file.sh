#!/bin/bash

outname=$1
operation=$2
datasetname=$3
annotation="annotation"

GAIAPATH=/Volumes/ssdData/virtualenv/mtgtools/lib/python2.7/site-packages/gaia2/scripts/classification
export PATH=$PATH:$GAIAPATH
GAIAPRJPATH=/Volumes/datadisk/hellska/thesis/datasets/$datasetname/$annotation
GAIAPRJFILE=$GAIAPRJPATH"/"$annotation".project"
GAIAHISTFILE=/Volumes/datadisk/hellska/thesis/datasets/$datasetname/$annotation/$annotation.history

echo "Project_file: "$GAIAPRJFILE
echo "History file: "$GAIAHISTFILE
echo "Operation type: "$operation

if [ $operation -eq 1 ];then
  rm -rf ${GAIAPRJPATH}"/"results
  rm ${GAIAPRJPATH}/datasets/annotation-*

  python $GAIAPATH"/run_tests.py" $GAIAPRJFILE

  python $GAIAPATH"/select_best_model.py" $GAIAPRJFILE $GAIAHISTFILE

elif [ $operation -eq 2 ];then
  echo "Eseguo la selezione del modello migliore"
  python $GAIAPATH"/select_best_model.py" $GAIAPRJFILE $GAIAHISTFILE
else
  echo "Eseguo il training completo"
  python $GAIAPATH"/train_model_from_sigs.py" $GAIAPRJPATH
fi

mv $GAIAPRJPATH"/"${annotation}.history $GAIAPRJPATH"/"$outname.history
mv ${GAIAPRJPATH}"/"${annotation}.history.param ${GAIAPRJPATH}"/"$outname.history.param
mv ${GAIAPRJPATH}"/"${annotation}.history.results.html ${GAIAPRJPATH}"/"$outname.history.results.html

ls $GAIAPRJPATH

