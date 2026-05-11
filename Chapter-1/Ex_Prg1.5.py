#   Implement Inner Product of Two Qubit States
#   Task: Write a Python function that takes two qubits (as vectors) and 
#   computes the inner product ⟨ψ|ϕ⟩ using NumPy.


# Implement Inner Product of Two Qubit States
# Using Quantum Circuit + Bloch Sphere + NumPy

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from math import pi

# -----------------------------
# Create First Qubit State |ψ>
# Example: |+> state
# -----------------------------
qc1 = QuantumCircuit(1)
qc1.h(0)

# Get statevector
psi = Statevector.from_instruction(qc1)

print("State |ψ> :")
print(psi)

# Bloch Sphere of |ψ>
fig=plot_bloch_multivector(psi)
fig.savefig('Prg1.5_psi_bloch.png')



# -----------------------------
# Create Second Qubit State |ϕ>
# Example: |0> state
# -----------------------------
qc2 = QuantumCircuit(1)

# Get statevector
phi = Statevector.from_instruction(qc2)

print("State |ϕ> :")
print(phi)

# Bloch Sphere of |ϕ>
fig=plot_bloch_multivector(phi)
fig.savefig('Prg1.5_phi_bloch.png')


# -----------------------------
# Compute Inner Product <ψ|ϕ>
# -----------------------------
inner_product = np.vdot(psi.data, phi.data)

print("Inner Product <ψ|ϕ> =", inner_product)
print("Magnitude =", abs(inner_product))

