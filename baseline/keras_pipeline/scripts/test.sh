# Recurrent raw signal experiments

mkdir -p log/
for patient in  "chb05" "chb08" "chb12" "chb14" "chb15" "chb24" "chb01" "chb03"
do
	touch log/${patient}_recurrent_test.out
	touch log/${patient}_recurrent_test.err

	python ../python/test_recurrent_keras.py --index ../../indexes_detection/$patient/test.txt\
	--id $patient --model gru\
	--batch-size 64\
	--dir keras_experiments/detection_recurrent_${patient}_gru_adam_0.0001_11-Dec\
	>log/${patient}_recurrent_test.out 2>log/${patient}_recurrent_test.err
done

