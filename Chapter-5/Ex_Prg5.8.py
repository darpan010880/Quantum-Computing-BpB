# VQE for H2 (Robust version without GroundStateEigensolver)

import numpy as np

from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper

from qiskit.primitives import StatevectorEstimator
from qiskit_algorithms.minimum_eigensolvers import VQE, NumPyMinimumEigensolver
from qiskit_algorithms.optimizers import SLSQP

from qiskit.circuit.library import TwoLocal


# -------------------------------
# STEP 1: Molecule
# -------------------------------

driver = PySCFDriver(
    atom="H 0 0 0; H 0 0 0.735",
    basis="sto3g"
)

problem = driver.run()


# -------------------------------
# STEP 2: Hamiltonian
# -------------------------------

mapper = JordanWignerMapper()
hamiltonian = mapper.map(problem.hamiltonian.second_q_op())


# -------------------------------
# STEP 3: Exact Solution
# -------------------------------

exact_solver = NumPyMinimumEigensolver()
exact_result = exact_solver.compute_minimum_eigenvalue(hamiltonian)

exact_energy = exact_result.eigenvalue.real


# -------------------------------
# STEP 4: Ansatz
# -------------------------------

num_qubits = hamiltonian.num_qubits

ansatz = TwoLocal(
    num_qubits,
    rotation_blocks="ry",
    entanglement_blocks="cz",
    reps=2
)


# -------------------------------
# STEP 5: VQE
# -------------------------------

estimator = StatevectorEstimator()
optimizer = SLSQP(maxiter=100)

vqe = VQE(estimator, ansatz, optimizer)

vqe_result = vqe.compute_minimum_eigenvalue(hamiltonian)
vqe_energy = vqe_result.eigenvalue.real


# -------------------------------
# STEP 6: Output
# -------------------------------

print("\n===== H2 Ground State Energy =====")
print(f"VQE Energy   : {vqe_energy:.6f}")
print(f"Exact Energy : {exact_energy:.6f}")
print(f"Error        : {abs(vqe_energy - exact_energy):.6f}")