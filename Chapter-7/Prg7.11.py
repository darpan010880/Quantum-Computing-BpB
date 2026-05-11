#   Deutsch’s Algorithm (Simple Quantum Algorithm)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def deutsch_oracle(balanced=True):
    qc = QuantumCircuit(2)
    if balanced:
        qc.cx(0, 1) 					 # Apply CNOT for f(x)=x
    else:
        qc.i(1)     					# Do nothing for constant f(x)=0
    return qc


qc = QuantumCircuit(2, 1)				# Deutsch algorithm
qc.x(1)						# Step 1: Initialize |0⟩|1⟩
qc.h([0, 1])						# Step 2: Apply H gates
oracle = deutsch_oracle(balanced=True)		# Step 3: Apply Oracle (choose constant or balanced)
qc.compose(oracle, inplace=True)
qc.h(0)						# Step 4: Apply H on the first qubit
qc.measure(0, 0)					# Step 5: Measure first qubit
fig=qc.draw("mpl")
fig.savefig('circuit_Prg7.11.png')


sim = AerSimulator()				# Simulate
compiled = transpile(qc, sim)
result = sim.run(compiled).result()
counts = result.get_counts()


print(counts)						# Display result
plot_histogram(counts)
plt.savefig('histogram_Prg7.11.png')