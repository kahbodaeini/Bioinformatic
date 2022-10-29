import numpy as np

# test = 'xyxzzxyxyy'
# priorStates = [0.5, 0.5]
# transitionMatrix = [0.641, 0.359], [0.729, 0.271]
# emissionMatrix = [0.117, 0.691, 0.192], [0.097, 0.420, 0.483]


def translateStringToInt(inputString):
    newString = inputString.replace('x', '0')
    newString = newString.replace('y', '1')
    newString = newString.replace('z', '2')
    l = list(map(int, newString))
    return l


def translateFinalStringToInt(finalString):
    probabilitySequence = ""
    for i in v:
        if i == 0:
            probabilitySequence += "A"
        if i == 1:
            probabilitySequence += "B"
        if i == 2:
            probabilitySequence += "C"
    return probabilitySequence


def viterbi_path(prior, transmat, obslik, scaled=True, ret_loglik=False):
    
    num_hid = obslik.shape[0]  # number of hidden states
    num_obs = obslik.shape[1]  # number of observations (not observation *states*)

    # trellis_prob[i,t] := Pr((best sequence of length t-1 goes to state i), Z[1:(t+1)])
    trellis_prob = np.zeros((num_hid, num_obs))
    # trellis_state[i,t] := best predecessor state given that we ended up in state i at t
    trellis_state = np.zeros((num_hid, num_obs), dtype=int)  # int because its elements will be used as indicies
    path = np.zeros(num_obs, dtype=int)  # int because its elements will be used as indicies

    trellis_prob[:, 0] = prior * obslik[:, 0]  # element-wise mult
    if scaled:
        scale = np.ones(num_obs)  # only instantiated if necessary to save memory
        scale[0] = 1.0 / np.sum(trellis_prob[:, 0])
        trellis_prob[:, 0] *= scale[0]

    trellis_state[:, 0] = 0  # arbitrary value since t == 0 has no predecessor
    for t in range(1, num_obs):
        for j in range(num_hid):
            trans_probs = trellis_prob[:, t - 1] * transmat[:, j]  # element-wise mult
            trellis_state[j, t] = trans_probs.argmax()
            trellis_prob[j, t] = trans_probs[trellis_state[j, t]]  # max of trans_probs
            trellis_prob[j, t] *= obslik[j, t]
        if scaled:
            scale[t] = 1.0 / np.sum(trellis_prob[:, t])
            trellis_prob[:, t] *= scale[t]

    path[-1] = trellis_prob[:, -1].argmax()
    for t in range(num_obs - 2, -1, -1):
        path[t] = trellis_state[(path[t + 1]), t + 1]

    if not ret_loglik:
        return path
    else:
        if scaled:
            loglik = -np.sum(np.log(scale))
        else:
            p = trellis_prob[path[-1], -1]
            loglik = np.log(p)
        return path, loglik


input = open("input.txt", 'r')
lines = input.read().splitlines()

# test = lines[0]
priorStates = [0.5, 0.5]
transitionMatrix = [0.641, 0.359], [0.729, 0.271]
emissionMatrix = [0.117, 0.691, 0.192], [0.097, 0.420, 0.483]

print(type(transitionMatrix))

test = lines[0]

n = len(lines[4].split())

prior_states = [1/n for i in range(n)]

pr = np.array(prior_states)

transition_matrix = (lines[7+i].split()[1:] for i in range(n))
emission_matrix = (lines[9+n+i].split()[1:] for i in range(n))

kir = []
kos = []

for i in transition_matrix:
    for j in i:
        j = float(j)
        kir.append(j)

for i in emission_matrix:
    for j in i:
        j = float(j)
        kos.append(j)

print(transitionMatrix)

print(type(kir[0]))

# print(prior_states)
# print(transition_matrix)
# print(emission_matrix)
#
# print("kir")

tr = np.ndarray(kir, dtype=float).reshape(n, n)
em = np.ndarray(kos, dtype=float).reshape(n, 3)

# tr = np.array(lines[7+i].split()[1:] for i in range(n))
# em = np.array(lines[9+n+i].split()[1:] for i in range(n))


# print(type(tr))
# print(type(em))

# for i in transition_matrix:
#     print(i, end=" ")
#
# for i in emission_matrix:
#     print(i, end=" ")

print("kir")

priors = np.array(priorStates)
transmat = np.array(transitionMatrix)
emmat = np.array(emissionMatrix)

print(priors)
print(transmat)
print(emmat)

observations = np.array(translateStringToInt(test), dtype="int")
obslik = np.array([em[:, z] for z in observations]).T
v = (viterbi_path(priors, tr, obslik))
finalSequenceSteps = translateFinalStringToInt(v)
print(finalSequenceSteps)

output = open("output.txt", 'w')
output.write(finalSequenceSteps)
