import random

def secret_santa(potentials):
    ss_map = {}

    try:
        for i in range(len(potentials.keys())):
            lad = random.choice(list(potentials.keys()))
            ss_map[lad] = random.choice(potentials[lad])
            del potentials[lad]
            potentials = {k: [name for name in v if (name != ss_map[lad])] for k, v in potentials.items()}
            if ss_map[lad] in potentials:
                potentials[ss_map[lad]] = [name for name in potentials[ss_map[lad]] if name != lad]
            if (any([len(l) == 0 for l in potentials.keys()])):
                return {}
    except:
        return {}

    return ss_map