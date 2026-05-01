# Visualize Different Qubit States on Bloch Sphere
# Task: Create a function that takes values of θ and φ, and plots the corresponding qubit on the Bloch sphere using Qiskit.


from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from math import pi

# Set values of theta and phi
theta = pi / 2     # change value as needed or you can create a function to input these values
phi = pi / 3       

# Create 1-qubit circuit
qc = QuantumCircuit(1)

# Apply rotations to create qubit state
qc.ry(theta, 0)
qc.rz(phi, 0)

# Display circuit
print("Quantum Circuit:")
print(qc)
qc.draw(output='mpl')

# Get statevector
state = Statevector.from_instruction(qc)

# Print statevector
print("Statevector:")
print(state)

# Plot Bloch Sphere
fig=plot_bloch_multivector(state)
fig.savefig('Prg1.3bloch_sphere.png')