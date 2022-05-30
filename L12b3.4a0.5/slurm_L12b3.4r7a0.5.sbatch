#!/bin/bash
#SBATCH --job-name=L12b3.4r7a0.5
#SBATCH -n 1
#SBATCH -t 5-00:00
#SBATCH --cpus-per-task=15
#SBATCH -w parma12

~/Desktop/FHDW/fhdw-master/a.out par_L12b3.4r7a0.5
