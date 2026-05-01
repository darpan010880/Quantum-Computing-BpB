#   Bell State Creation
#   Task: Create a 2-qubit quantum circuit that generates the entangled Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2. Simulate and plot the measurement histogram to verify entanglement.


from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate on qubit 0
qc.h(0)

# Apply CNOT gate
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Print circuit
print(qc.draw())
fig= qc.draw('mpl')
fig.savefig('Ex_Prg3.6_circuit.png')    

# Use simulator
simulator = AerSimulator()

# Transpile circuit
compiled_circuit = transpile(qc, simulator)

# Run circuit
job = simulator.run(compiled_circuit, shots=1024)

# Get result
result = job.result()
counts = result.get_counts()

# Print counts
print("Measurement Results:", counts)

# Plot histogram
fig=plot_histogram(counts)
fig.savefig('Ex_Prg3.6_histogram.png')    

