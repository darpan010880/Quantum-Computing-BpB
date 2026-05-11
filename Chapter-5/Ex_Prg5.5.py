# Deutsch–Jozsa Algorithm with Histogram Visualization

from qiskit import QuantumCircuit
from qiskit.primitives import BackendSamplerV2
from qiskit_aer import Aer
import matplotlib.pyplot as plt


# -------------------------------
# ORACLE DEFINITIONS
# -------------------------------

def constant_oracle(n):
    oracle = QuantumCircuit(n + 1)
    return oracle


def balanced_oracle(n):
    oracle = QuantumCircuit(n + 1)
    for qubit in range(n):
        oracle.cx(qubit, n)
    return oracle


# -------------------------------
# DEUTSCH–JOZSA CIRCUIT
# -------------------------------

def deutsch_jozsa_circuit(n, oracle):
    qc = QuantumCircuit(n + 1, n)

    qc.x(n)
    qc.h(range(n + 1))

    qc.compose(oracle, inplace=True)

    qc.h(range(n))
    qc.measure(range(n), range(n))

    return qc


# -------------------------------
# SETUP SAMPLER (Aer backend)
# -------------------------------

backend = Aer.get_backend("aer_simulator")
sampler = BackendSamplerV2(backend=backend)


# -------------------------------
# RUN EXPERIMENT
# -------------------------------

n = 3

# --- Constant ---
qc_const = deutsch_jozsa_circuit(n, constant_oracle(n))
result_const = sampler.run([qc_const]).result()
counts_const = result_const[0].data.c.get_counts()

# --- Balanced ---
qc_bal = deutsch_jozsa_circuit(n, balanced_oracle(n))
result_bal = sampler.run([qc_bal]).result()
counts_bal = result_bal[0].data.c.get_counts()


# -------------------------------
# PLOT HISTOGRAMS (Matplotlib)
# -------------------------------

# Constant function plot
plt.figure()
plt.bar(counts_const.keys(), counts_const.values())
plt.title("Deutsch–Jozsa: Constant Function")
plt.xlabel("Measurement Outcome")
plt.ylabel("Counts")

# Balanced function plot
plt.figure()
plt.bar(counts_bal.keys(), counts_bal.values())
plt.title("Deutsch–Jozsa: Balanced Function")
plt.xlabel("Measurement Outcome")
plt.ylabel("Counts")

fig=plt.gcf()  # Get current figure
fig.savefig("Ex_Prg5.5_deutsch_jozsa_histogram.png")

# -------------------------------
# PRINT RESULTS
# -------------------------------

print("Constant:", counts_const)
print("Balanced:", counts_bal)