# Deutsch-Jozsa Algorithm

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1: Oracle construction (  Create an oracle for Deutsch–Jozsa. case: "constant" or "balanced"    n: number of input qubits)
def deutsch_jozsa_oracle(case, n):
    qc = QuantumCircuit(n+1)
    if case == "constant":            # Example: output always 0 (no-op), or always 1 (X on ancilla)
        qc.i(range(n))     		      # do nothing on inputs
        qc.i(n)            		      # ancilla unchanged (always 0)
        qc.x(n) 			          # Uncomment below to force output=1 for all inputs       
    elif case == "balanced":	      # Example: flip ancilla depending on parity of inputs
        for qubit in range(n):
            qc.cx(qubit, n)
    else:
        raise ValueError("Case must be 'constant' or 'balanced'")
    return qc
# Step 2: Deutsch–Jozsa circuit (Run Deutsch–Jozsa with n input qubits.)
def deutsch_jozsa_algorithm(case="balanced", n=3):
    # Create quantum circuit with n input qubits + 1 ancilla + n classical bits
    qc = QuantumCircuit(n+1, n)

    # Initialize ancilla in |1>
    qc.x(n)
    qc.h(n)

    # Hadamard on input qubits
    qc.h(range(n))

    # Append oracle
    qc.append(deutsch_jozsa_oracle(case, n), range(n+1))

    # Hadamard on input qubits again
    qc.h(range(n))

    # Measurement of input register
    qc.measure(range(n), range(n))

    return qc


# Step 3: Run simulation 
backend = Aer.get_backend("aer_simulator")		# Choose "constant" or "balanced"
qc = deutsch_jozsa_algorithm(case="balanced", n=3)
tqc = transpile(qc, backend)
result = backend.run(tqc, shots=1024).result()
counts = result.get_counts()

# Step 4: Visualization 
print("Measurement Results:", counts)
fig=qc.draw("mpl")
fig.savefig("Prg5.3_deutsch_jozsa_circuit.png")  # Save the circuit diagram as an image

fig= plot_histogram(counts)
fig.savefig("Prg5.3_deutsch_jozsa_histogram.png")  # Save the histogram as an image

