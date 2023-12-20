# Reproduction and Integration of Epileptic Seizure Detection Algorithm into EPILEPSY BENCHMARKS
---
## Regular Lost Functions - CS-433 - Project 2 (ML4Science) - Fall 2023

**Author:** Juan Sapriza (juan.sapriza@epfl.ch)

**Hosting Lab:** Embedded Systems Laboratory - EPFL, Lausanne

**Supervisor:** Dr. Jonathan Dan

---

## Introduction

Machine Learning (ML) has become a popular approach for the detection of epiletic seizures from Electroencephalograms (EEG). During the last years several datasets have been produced, both public and private. At the same time, abundant research has been carried out but without much consensus on the dataset to use, data format, cross-validation approach or figures of merit.
In this light, the Embedded Systems Laboratory from EPFL is developing a standarization framework for seizure detection algorithms: [EPILEPSY BENCHMARKS](https://eslweb.epfl.ch/epilepsybenchmarks/framework/#tuh). Its goal is to harmonize the work of algorithm developers to offer a fair comparison between approaches.

The process of submission to the platform, listed in Figure 1, include taking a State-of-the-Art publication and:
1. Reproduce its reported results.
2. Adapt the algorithm to work with the standardized-format dataset.
3. Adapt the algorithm to perform the standardized cross-validation approach.
4. Obtain the benchmark's figure of merits.
5. Produce a standardized annotation document for submission.
6. Submit the results to the EPILEPSY BENCHMARKS online platform.
7. Re-run the algorithm with all other standaridized-format datasets.

<p align="left"><img src="docs/work-diagram-report.png" width="1000"></p>
Figure 1: Workflow of comparing epileptic-seizure-detection machine learning publications, traditional approach vs. the EPILEPSY BENCHMARKS workflow. This work involves adapting a publication to fit the standards of the platform.

This work will focus on the most \gls{ml}-related and demanding tasks, namely (1), (3) and (4).

---

## Baseline Publication

To choose a baseline publication we applied the following criteria:
* Performs epileptic seizure detection based on scalp EEG.
* Uses a ML approach.
* Validated on one of the benchmark's datasets.
* Available code.

Based on those points we chose:

**Automatic Detection of Epileptic Seizures with Recurrent and Convolutional Neural Networks**
> Carrión, S., López-Chilet, Á., Martínez-Bernia, J., Coll-Alonso, J., Chorro-Juan, D., Gómez, J.A. (2022). Automatic Detection of Epileptic Seizures with Recurrent and Convolutional Neural Networks. In: Mazzeo, P.L., Frontoni, E., Sclaroff, S., Distante, C. (eds) Image Analysis and Processing. ICIAP 2022 Workshops. ICIAP 2022. Lecture Notes in Computer Science, vol 13373. Springer, Cham. https://doi.org/10.1007/978-3-031-13321-3_46

The code, [accessible on Github](https://github.com/deephealthproject/UC13_pipeline) was cloned from commit `20b24a3`.

---

## Reproducibility

This work's repository adapted the baseline repository to ease the process of reproducibility under the directory `baseline`. Inside it we added a `requirements.txt` file including the required python packages to be installed.
The CHB-MIT data-set needs to be located as a soft link in `baseline/keras_pipeline/original_signals`. This data-set is already available inside the ESL servers, or can be downloaded from the [Physionet webpage](https://physionet.org/content/chbmit/1.0.0/).

Upon accessing such link folders named after each subject containing the `edf` file of each recording with their corresponding `.edf.seizures` file.

Inside `baseline/keras_pipeline`, running the  `homogenize_signals.sh` script will adapt the data-set to the format required by the rest of the processing chain and store it in a new `clean_signals` folder.

Running the `train.sh` script will take the pre-defined list of subjects and train the GRU  model on the recordings listed in `baseline/indexes_detection/<subject>/train.txt` and `validation.txt`. The best models are stored in `baseline/keras_pipeline/scripts/keras_experiments` under a folder named after the `subject` and `experiment` defined in the `train.sh` script. A log file with the details of the run is generated inside the `log` folder.

>Note that the final version of the repository includes a subdirectory `new` with the new proposed train/test division.

The testing process is launched by running the `test.sh` script, which will look for models using the defined `subject` and `experiment` names. The testing recording are defined in a `test.txt` file along with its training counterparts.
The training scheme will generate folders containing information on the best model parameters which is useful to keep track of the different experiments carried out. We manually rename the selected models as `subject_experiemnt` before the testing pass.

---

## Generating plots

All plots are generated from the resulting experiments. Few values have been manually xtracted from files for simplicity. To generate the plots, run all cells in the notebook `generate_plots.ipynb`.