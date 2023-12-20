# Recurrent raw signal experiments

mkdir -p log/
# for patient in  "chb05" "chb08" "chb14" "chb15" "chb24" "chb01" "chb03"  "chb12"
for patient in  "chb12"
do
	for experiment in "tscv"
	do
		touch log/${patient}_${experiment}.out
		touch log/${patient}_${experiment}.err

		python ../python/train_recurrent_keras.py \
		--index ../../indexes_detection/new/$patient/train.txt\
		--id $patient \
		--model gru\
		--batch-size 64\
		>log/${patient}_${experiment}.out 2>log/${patient}_${experiment}.err
	done
done

