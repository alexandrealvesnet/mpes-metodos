#!/bin/sh
DIR_MUSS=/home/alexandre/Desenvolvimento/mpes-experimentos/muss
DIR_SENTENCES=/home/alexandre/Desenvolvimento/mpes-experimentos/muss/scripts/ementas/sentences/exp01/STF
cd $DIR_SENTENCES

for FILE in `ls *.en -1v`; # LISTA OS ARQUIVOS *.en E ORDENA CONSIDERANDO A NUMERAÇÃO
do
  python "$DIR_MUSS/scripts/ementas/exp01/simplify_sentence.py" "$DIR_SENTENCES/$FILE" --model-name muss_en_wikilarge_mined
done
