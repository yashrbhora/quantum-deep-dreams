import numpy as np
import qiskit
from qiskit import QuantumCircuit, Aer
from qiskit.tools.visualization import plot_histogram, plot_state_city
from qiskit.circuit import Parameter
from qiskit_ionq import IonQProvider


# global params
no_qubits = 8

provider = IonQProvider("CW8P78VEqL4NFcMKkXMq5tFu193Hzazs")
backend = provider.get_backend("ionq_simulator")

def bind(circ, vals_dict):
    return circ.bind_parameters(vals_dict)

def compute_scores(probabilities):
    vid_counts = {}
    for key, val in probabilities.items():
        print(val)
        for i in range(len(key)):
            vid_counts[i] = float(key[::-1][i])*val
    print(vid_counts)
    vid_counts = {key:val/sum(vid_counts.values()) for key,val in vid_counts.items()}
    return vid_counts

def get_quantum_parameters(no_outputs, inputs_dict):
    # setup
    no_qubits = np.int(np.ceil(np.log(no_outputs)/np.log(2)))
    print(no_qubits, np.log(no_outputs)/np.log(2))
    params = {}
    for i in range(no_qubits):
        params[f"video_{i}"] = Parameter(f"v_{i}")
    
    # prepare circuit
    qfm = qiskit.QuantumCircuit(no_qubits)
    #qfm.prepare_state([1/np.sqrt(2**no_qubits)+0j]*2**no_qubits)
    for i in range(no_qubits):    
        qfm.rx(params[f"video_{i}"], i)
    qfm.measure_all()
    qfm_bound = bind(qfm, inputs_dict)

    job = backend.run(qiskit.compiler.transpile(qfm_bound, backend), shots=10000)
    probabilities = job.get_probabilities() 
    return compute_scores(probabilities)

