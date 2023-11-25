## Reproduction and Integration of Epileptic Seizure Detection Algorithm into EPILEPSY BENCHMARKS
---
## Regular Lost Functions - CS-433 - Project 2 (ML4Science) - Fall 2023
### Authors: Mridhula Venkatanarayanan, Juan Sapriza & Kenta Yokote
### Hosting Lab: Embedded Systems Laboratory - EPFL, Lausanne
### Under supervision of Dr. Jonathan Dan
---

## Introduction

Machine Learning (ML) has become a popular approach for the detection of epiletic seizures from Electroencephalograms (EEG). During the last years several databases have been produced, both public and private. At the same time, abundant research has been carried out but without much consensus on the database to use, data format, cross-validation approach or figures of merit.
In this light, the Embedded Systems Laboratory from EPFL is developing a standarization framework for seizure detection algorithms: EPILEPSY BENCHMARKS. Its goal is to harmonize the work of algorithm developers to offer a fair comparison between approaches.
Our objective during this project is to take a work from the State-of-the-Art and:
* Reproduce its reported results
* Adapt the algorithm to work with one of the standardized-format-databases
* Adapt the algorithm to perform the standardized cross-valdiation approach
* Obtain the framework's figure of merits and submit to the platform.
* Re-run the algorithm with all other standaridized-format-databases.

<p align="left"><img src="docs/work-diagram.png" width="1000"></p>

## Baseline Publication

To choose a baseline publication we applied the following criteria:
* Performs epileptic seizure detection based on scalp EEG.
* ML approach.
* Validated on one of the framework's databases.
* Available code.

Based on those points we chose:

**Automatic Detection of Epileptic Seizures with Recurrent and Convolutional Neural Networks**
> Carrión, S., López-Chilet, Á., Martínez-Bernia, J., Coll-Alonso, J., Chorro-Juan, D., Gómez, J.A. (2022). Automatic Detection of Epileptic Seizures with Recurrent and Convolutional Neural Networks. In: Mazzeo, P.L., Frontoni, E., Sclaroff, S., Distante, C. (eds) Image Analysis and Processing. ICIAP 2022 Workshops. ICIAP 2022. Lecture Notes in Computer Science, vol 13373. Springer, Cham. https://doi.org/10.1007/978-3-031-13321-3_46

The code, [accessible on Github](https://github.com/deephealthproject/UC13_pipeline) was cloned from commit `20b24a3`.

