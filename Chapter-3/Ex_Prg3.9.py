#   Simulate Amplitude Damping (Decoherence)
#   Task: Prepare a qubit in superposition using Hadamard. Apply identity gate with amplitude damping noise (e.g., 0.3). Plot the histogram to see decoherence effects.

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, amplitude_damping_error
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# -----------------------------
# Create Quantum Circuit
# -----------------------------
qc = QuantumCircuit(1, 1)

# Put qubit in superposition
qc.h(0)

# Identity gate (used to attach noise)
qc.id(0)

# Measure
qc.measure(0, 0)

print(qc.draw())
fig= qc.draw('mpl')
fig.savefig('Ex_Prg3.9_circuit.png')


simulator = AerSimulator()

compiled = transpile(qc, simulator)

job = simulator.run(compiled, shots=1024)
result = job.result()

counts = result.get_counts()
fig=plot_histogram(counts)      
fig.savefig('Ex_Prg3.9_histogram_1.png')

# -----------------------------
# Noise Model
# -----------------------------
noise_model = NoiseModel()

# Amplitude damping probability = 0.3
error = amplitude_damping_error(0.1)

# Apply noise to identity gate
noise_model.add_all_qubit_quantum_error(error, ['id'])

# -----------------------------
# Simulator
# -----------------------------

compiled = transpile(qc, simulator)

job = simulator.run(compiled, shots=1024)
result = job.result()

counts = result.get_counts()

print("Measurement Results:", counts)

# -----------------------------
# Plot Histogram
# -----------------------------
fig=plot_histogram(counts)      
fig.savefig('Ex_Prg3.9_histogram.png')
