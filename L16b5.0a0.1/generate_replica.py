import numpy as np

if __name__ == "__main__":

    L = 16
    seed = 1

    for seed in range(1, 25):
        rng = np.random.default_rng(seed)
        replica = np.empty(4096)
        replica.fill(0.5)
        replica[2048:]=-0.5 
        rng.shuffle(replica)

        with open("disord_L%sr%s.dat" % (L, seed), "w") as f:
            f.write(str(seed)+"\n")
            f.write(str(L)+"\n")
            for value in replica:
                f.write(str(value)+"  ")
