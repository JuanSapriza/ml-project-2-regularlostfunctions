# Recurrent raw signal experiments

mkdir -p log/
for patient in  "chb05" "chb08" "chb14" "chb15" "chb24" "chb01" "chb03" "chb12"
do
	# for experiment in "no_tscv" "tscv_w3" "tscv_w10"
	for experiment in "tscv_w3"
	do
		touch log/${patient}_test_${experiment}.err

		python ../python/test_recurrent_keras.py --index ../../indexes_detection/new/$patient/test.txt\
		--id $patient --model gru\
		--batch-size 64\
		--dir keras_experiments/${patient}_${experiment}\
		2>log/${patient}_test_$experiment.err
	done
done
