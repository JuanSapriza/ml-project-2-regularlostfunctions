from data_utils_detection import RawRecurrentDataGenerator
from tensorflow import keras


batch_size = 64
subject='05'
training_data = ["../../indexes_detection/new/chb05/train.txt"]

# Data Generator Object for training
print('\n\nCreating Training Data Generator...')
dg = RawRecurrentDataGenerator(index_filenames=training_data,
                        sampling_rate=256, # in Hz
                        batch_size=batch_size,
                        in_training_mode=True,
                        balance_batches=True,
                        patient_id=subject)
#


segments                = 10 # Number of CV segments
max_segments_in_history = 3
batches_per_segm        = int(len(dg)/segments)

initial_segments = max_segments_in_history*(max_segments_in_history+1)/2 # Number of segments that will be computed during the initial stage
regime_segments = (segments - max_segments_in_history -1)*max_segments_in_history # Number of segments that will be computed during the rest
validation_segments = segments -1 # Number of segments that will be run for validation (approximated, as the time is not the same)
batch_time = 2.5
segment_time = batches_per_segm * batch_time
print(f'\nEstimated Total Training time time: {segment_time*(initial_segments+regime_segments+validation_segments)/3600:02f} hours\n')

y = []
for s in range(len(dg)):
    _, y_s = dg[s]
    y_s = keras.utils.to_categorical(y_s, num_classes=2)
    y.append( y_s )

dg = y

import pickle
with open( "dg.pkl", 'wb') as f:
        pickle.dump( dg, f )

