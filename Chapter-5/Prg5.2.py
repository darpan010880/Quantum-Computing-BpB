# Shor’s Algorithm

import math
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer


# Step-1 : Simple classical post-processing


def classical_postprocessing(a, r, N):
    if r % 2 != 0:
        return None
    factor1 = math.gcd(a**(r//2) - 1, N)
    factor2 = math.gcd(a**(r//2) + 1, N)
    if factor1 not in [1, N]:
        return factor1
    if factor2 not in [1, N]:
        return factor2
    return None

# Step-2:  Shor’s algorithm for N=15
N = 15
a = 2  # choose a < N randomly such that gcd(a, N)=1
r = 4  # for demo, we “pretend” the quantum circuit found order r=4


factor = classical_postprocessing(a, r, N)
print(f"Found factor of {N}: {factor}")

# Step 3: Optional: small quantum circuit demo (not full Shor)
qc = QuantumCircuit(4)
qc.h([0,1])
qc.cx(0,2)
qc.cx(1,3)
qc.measure_all()
backend = Aer.get_backend("qasm_simulator")
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
result = job.result()
counts = result.get_counts()

# Step 4: Visualization 
print("Quantum circuit measurement counts:", counts)
fig=qc.draw('mpl')
fig.savefig("Prg5.2_shor_circuit.png")  # Save the circuit diagram as an image
