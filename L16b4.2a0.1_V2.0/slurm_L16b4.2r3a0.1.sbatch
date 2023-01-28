#!/bin/bash
#SBATCH --job-name=L16b4.2r3a0.1
#SBATCH -n 1
#SBATCH -t 6-00:00
#SBATCH --cpus-per-task=20
#SBATCH -w parma7

~/Desktop/FHDW/fhdw-master/a.out par_L16b4.2r3a0.1
