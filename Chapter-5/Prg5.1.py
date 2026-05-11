#   Deutsch–Jozsa Algorithm


from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

#Step 1: Create the circuit —
n = 2
qc = QuantumCircuit(n, n)

# Step 2: Hadamard to all qubits (equal superposition)
qc.h(range(n))

# Step 3: Oracle for |11>
qc.cz(0, 1)  # Controlled-Z flips the phase of |11>

# Step 4: Diffusion operator
qc.h(range(n))
qc.x(range(n))
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x(range(n))
qc.h(range(n))

# Step 5: Measurement
qc.measure(range(n), range(n))

# Step 6: Simulation —
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print("Measurement Results:", counts)

# Step 7: Visualization —
fig=plot_histogram(counts)
fig.savefig("Prg5.1_grover_histogram.png")  # Save the histogram as an image

fig=qc.draw(output='mpl')  # Draw the circuit
fig.savefig("Prg5.1_grover_circuit.png")  # Save the circuit diagram as an image
