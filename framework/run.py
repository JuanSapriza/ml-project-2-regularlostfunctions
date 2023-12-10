
''' To convert the dataset. Run only once.'''
'''
from dataIo.bids.convert_chbmit2bids import convert
convert("/home/sapriza/projects/ml-project2/baseline/original_signals/data/", "/home/sapriza/projects/ml-project2/baseline/clean_signals")
'''

if 0:
    from dataIo import eeg
    from dataIo import annotations as annot
    import numpy

    # Obtained from original_signals/chb01/chb01-summary.txt
    # Reduced (from the one named _old bellow) because a) There where some repeated channels and b) the converter was not finding them inside the edf files
    ELECTRODES_CHB01 = (
    "FP1-F7",
    "F7-T7",
    "T7-P7",
    "P7-O1",
    "FP1-F3",
    "F3-C3",
    "C3-P3",
    "P3-O1",
    "FP2-F4",
    "F4-C4",
    "C4-P4",
    "P4-O2",
    "FP2-F8",
    "F8-T8",
    "T8-P8",
    "P8-O2",
    "FZ-CZ",
    "CZ-PZ",
    )

    # ELECTRODES_CHB01_old = (
    # "FP1-F7",
    # "F7-T7",
    # "T7-P7",
    # "P7-O1",
    # "FP1-F3",
    # "F3-C3",
    # "C3-P3",
    # "P3-O1",
    # "FP2-F4",
    # "F4-C4",
    # "C4-P4",
    # "P4-O2",
    # "FP2-F8",
    # "F8-T8",
    # "T8-P8",
    # "P8-O2",
    # "FZ-CZ",
    # "CZ-PZ",
    # "P7-T7",
    # "T7-FT9",
    # "FT9-FT10",
    # "FT10-T8",
    # "T8-P8"
    # )



    def load_file_standard(data, annots):

        data_pieces = list()

        i0 = 0
        event_idx = 0
        while event_idx != len(annots.events):
            # First save the space without seizure at the beginning
            i1 = int(annots.events[event_idx]['onset']*data.fs)
            _signal = numpy.array([data.data[:,i0:i1]]).T
            _label = 0
            data_pieces.append((_signal, _label))
            i0 = i1
            # Now save the seizure
            i1 += int(annots.events[event_idx]['duration']*data.fs)
            _signal = numpy.array([data.data[:,i0:i1]]).T
            _label = 1
            data_pieces.append((_signal, _label))
            event_idx += 1
            i0 = i1

        # Save the last piece
        _signal = numpy.array([data.data[:,i0:]]).T
        _label = 0
        data_pieces.append((_signal, _label))

        return data_pieces


    sub = "01"
    ses = "01"
    run = "03"
    filename = "../baseline/clean_signals/sub-01/ses-01/eeg/sub-"+sub+"_ses-"+ses+"_task-szMonitoring_run-"+run
    # Physionet CHB-MIT is currently the only known dataset to only provide data in a bipolar montage
    data = eeg.Eeg.loadEdf( filename + ".edf", montage=eeg.Eeg.Montage.BIPOLAR, electrodes=ELECTRODES_CHB01 )
    annots = annot.Annotations.loadTsv(filename + "_events.tsv")

    d_p = load_file_standard(data, annots)
    print(d_p)




#################

import sys
sys.path.append("/home/juan/Desktop/ML/ml-project-2/baseline/")

import keras_pipeline.python.train_recurrent_keras as train

epochs = 10
batch_size = 64
window_length = 1, # in seconds
shift = 0.5, # in seconds
timesteps = 19, # in seconds
batch_size = 10,


train.main(epochs, batch_size, window_length, shift, timesteps)




