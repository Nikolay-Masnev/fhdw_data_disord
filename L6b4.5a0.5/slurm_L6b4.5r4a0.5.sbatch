#!/bin/bash
#SBATCH --job-name=L6b4.5r4a0.5
#SBATCH -n 1
#SBATCH -t 2-00:00
#SBATCH --cpus-per-task=20
#SBATCH -w parma10

~/Desktop/FHDW/fhdw-master/a.out par_L6b4.5r4a0.5
