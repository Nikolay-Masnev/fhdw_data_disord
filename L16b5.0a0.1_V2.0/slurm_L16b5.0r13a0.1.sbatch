#!/bin/bash
#SBATCH --job-name=L16b5.0r13a0.1
#SBATCH -n 1
#SBATCH -t 6-20:00
#SBATCH --cpus-per-task=20
#SBATCH -w parma18

~/Desktop/FHDW/fhdw-master/a.out par_L16b5.0r13a0.1
