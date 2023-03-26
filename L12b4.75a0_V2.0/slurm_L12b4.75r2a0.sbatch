#!/bin/bash
#SBATCH --job-name=L12b4.75r2a0
#SBATCH -n 1
#SBATCH -t 6-20:00
#SBATCH --cpus-per-task=15

~/fhdw-master/a.out par_L12b4.75r2a0
