# Grover Iteration Experiment for Different Targets

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------
# ORACLE (marks a target state)
# -------------------------------

def oracle(n, target):
    qc = QuantumCircuit(n)

    # Apply X gates for 0 bits
    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(i)

    # Multi-controlled Z
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)

    # Undo X gates
    for i, bit in enumerate(target):
        if bit == '0':
            qc.x(i)

    return qc


# -------------------------------
# DIFFUSION OPERATOR
# -------------------------------

def diffuser(n):
    qc = QuantumCircuit(n)

    qc.h(range(n))
    qc.x(range(n))

    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)

    qc.x(range(n))
    qc.h(range(n))

    return qc


# -------------------------------
# GROVER CIRCUIT
# -------------------------------

def grover_circuit(n, target, iterations):
    qc = QuantumCircuit(n, n)

    qc.h(range(n))  # superposition

    for _ in range(iterations):
        qc.compose(oracle(n, target), inplace=True)
        qc.compose(diffuser(n), inplace=True)

    qc.measure(range(n), range(n))
    return qc


# -------------------------------
# RUN EXPERIMENT
# -------------------------------

backend = Aer.get_backend("aer_simulator")
shots = 1024
n = 3

targets = ["000", "111", "101"]

for target in targets:
    probs = []
    iterations_list = list(range(1, 6))

    for k in iterations_list:
        qc = grover_circuit(n, target, k)
        qc = transpile(qc, backend)

        result = backend.run(qc, shots=shots).result()
        counts = result.get_counts()

        prob = counts.get(target, 0) / shots
        probs.append(prob)

    # Plot
    plt.figure()
    plt.plot(iterations_list, probs, marker='o')
    plt.title(f"Grover Search for target |{target}⟩")
    plt.xlabel("Number of Iterations")
    plt.ylabel("Probability of Target State")
    plt.xticks(iterations_list)
    plt.grid()

    print(f"\nTarget |{target}⟩ probabilities:", probs)

fig=plt.gcf()
fig.savefig("Ex_Prg5.6_grover_search.png"   )