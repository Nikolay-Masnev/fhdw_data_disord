#!/bin/bash
#SBATCH --job-name=L8b4.0r6a0.5
#SBATCH -n 1
#SBATCH -t 2-20:00
#SBATCH --cpus-per-task=15
#SBATCH -w parma9

~/Desktop/FHDW/fhdw-master/a.out par_L8b4.0r6a0.5
