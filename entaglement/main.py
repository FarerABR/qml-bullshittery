from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Build circuit
qc = QuantumCircuit(2, 2)   # 2 qubits, 2 classical bits
qc.h(0)                      # superposition on qubit 0
qc.cx(0, 1)                  # entangle qubit 0 and 1
qc.measure([0, 1], [0, 1])   # measure both

# 2. Run locally
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
print(result.get_counts())
# → {'00': 510, '11': 514}  (roughly)
