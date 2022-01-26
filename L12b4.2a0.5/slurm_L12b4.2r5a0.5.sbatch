#!/bin/bash
#SBATCH --job-name=L12b4.2r5a0.5
#SBATCH -n 1
#SBATCH -t 5-20:00
#SBATCH --cpus-per-task=30
#SBATCH -w parma5

~/Desktop/FHDW/fhdw-master/a.out par_L12b4.2r5a0.5
