#   Density Matrix of a Mixed State
#   Task: Write code to construct a mixed state where there’s 50% chance of |0⟩ and 50% chance of |1⟩. Represent it using a density matrix.

import numpy as np
from qiskit.quantum_info import DensityMatrix
from qiskit.visualization import plot_bloch_multivector

# Basis states
ket0 = np.array([[1], [0]])   # |0>
ket1 = np.array([[0], [1]])   # |1>

# Density matrices of pure states
rho0 = ket0 @ ket0.conj().T   # |0><0|
rho1 = ket1 @ ket1.conj().T   # |1><1|

# Mixed state:
# rho = 0.5|0><0| + 0.5|1><1|
rho = 0.5 * rho0 + 0.5 * rho1

# Convert to Qiskit DensityMatrix
dm = DensityMatrix(rho)

# Print density matrix
print("Density Matrix of Mixed State:")
print(dm)

# Matrix form
print("\nMatrix Representation:")
print(rho)

