from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector, array_to_latex
from math import pi
import matplotlib.pyplot as plt

circuit = QuantumCircuit(1)
theta = 0   # Example value for theta (can change this)
phi = 0     # Example value for phi (can change this)

# the rotation gates
circuit.ry(theta, 0)   # Rotate by theta around the y-axis
circuit.rz(phi, 0)     # Rotate by phi around the z-axis

print(circuit)
fig = circuit.draw(output='mpl')
fig.savefig('circuit.png')

circuit.remove_final_measurements()   # no measurements allowed

from qiskit.quantum_info import Statevector

statevector = Statevector(circuit)
print(array_to_latex(statevector, prefix="\\text{statevector = }\n"))

print(statevector)

fig = plot_bloch_multivector(statevector)
fig.savefig('bloch_sphere.png')