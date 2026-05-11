# Superdense Coding using Qiskit (Updated API)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram


# -------------------------------
# FUNCTION: Superdense Coding
# -------------------------------

def superdense_coding(message):
    """
    message: string of 2 bits ('00', '01', '10', '11')
    """

    qc = QuantumCircuit(2, 2)

    # Step 1: Create entanglement (Bell state)
    qc.h(0)
    qc.cx(0, 1)

    # Step 2: Alice encodes message on her qubit (qubit 0)
    if message == "01":
        qc.x(0)
    elif message == "10":
        qc.z(0)
    elif message == "11":
        qc.z(0)
        qc.x(0)
    # "00" → do nothing

    # Step 3: Alice sends qubit 0 to Bob (conceptual)

    # Step 4: Bob decodes
    qc.cx(0, 1)
    qc.h(0)

    # Step 5: Measure
    qc.measure([0, 1], [0, 1])

    return qc


# -------------------------------
# RUN EXPERIMENT
# -------------------------------

backend = Aer.get_backend("aer_simulator")
messages = ["00", "01", "10", "11"]

for msg in messages:
    print(f"\nMessage sent: {msg}")

    qc = superdense_coding(msg)
    qc_transpiled = transpile(qc, backend)
    fig=qc.draw("mpl")			# Draw the circuit
    fig.savefig('circuit_Prg7.13_msg.png')
    job = backend.run(qc_transpiled, shots=1024)
    result = job.result()
    counts = result.get_counts()

    print("Measurement result:", counts)

    # Plot histogram
    Fig=plot_histogram(counts)
    Fig.savefig(f'histogram_Ex_Prg13_{msg}.png')
    plt.title(f"Decoded Message: {msg}") 