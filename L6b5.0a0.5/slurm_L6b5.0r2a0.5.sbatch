#!/bin/bash
#SBATCH --job-name=L6b5.0r2a0.5
#SBATCH -n 1
#SBATCH -t 2-00:00
#SBATCH --cpus-per-task=15
#SBATCH -w parma5

~/Desktop/FHDW/fhdw-master/a.out par_L6b5.0r2a0.5
