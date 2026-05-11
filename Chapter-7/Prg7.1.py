# Step 1: Import Qiskit Modules (UPDATED)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Step 2: Initialize Quantum Circuit
qc = QuantumCircuit(2, 2)


# Step 3: Add Quantum Gates
qc.h(0)        # Hadamard gate on qubit 0
qc.cx(0, 1)    # CNOT gate


# Step 4: Measurement
qc.measure([0, 1], [0, 1])


# Step 5: Visualize Circuit
fig=qc.draw(output='mpl')
fig.savefig('Prg7.1_circuit.png')  # Save the circuit diagram as an image file


# Step 6: Choose Simulator (UPDATED)
backend = Aer.get_backend('aer_simulator')


# Step 7: Execute Circuit (UPDATED)
qc_transpiled = transpile(qc, backend)
job = backend.run(qc_transpiled, shots=1024)

result = job.result()
counts = result.get_counts()


# Step 8: Analyze Results
fig=plot_histogram(counts)
fig.savefig('Prg7.1_histogram.png')  # Save the histogram as an image file


# Step 9: Print Results
print("Measurement Counts:", counts)
