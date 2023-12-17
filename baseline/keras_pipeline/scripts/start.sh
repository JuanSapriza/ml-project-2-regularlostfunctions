# Recurrent raw signal experiments

mkdir -p log/
for patient in  "chb05" #"chb08" "chb12" "chb14" "chb15" "chb24" "chb01" "chb03"
do
	touch log/${patient}_recurrent_full_tscv.out
	touch log/${patient}_recurrent_full_tscv.err

	python ../python/train_recurrent_keras.py \
	--index ../../indexes_detection/new/$patient/train.txt\
	--id $patient \
	--model gru\
	--batch-size 64\
	>log/${patient}_recurrent_full_tscv.out 2>log/${patient}_recurrent_full_tscv.err
done

