# Import required libraries
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize
from qiskit.quantum_info import random_statevector, state_fidelity
from qiskit.providers.aer import AerSimulator
import matplotlib.pyplot as plt

def entangle(qc, a, b):
    # Qubit a is Alice's while qubit b is Bob's
    qc.h(a) # Put qubit a into state |+>
    qc.cx(a,b) # CNOT with a as control and b as target

def measure(qc, a, b):
    # Measures qubits a & b and save to classical bits 0 and 1
    qc.measure(a,0)
    qc.measure(b,1)

def alice_gates(qc, psi, a):
    qc.cx(psi, a) # CNOT with psi as control and a as target
    qc.h(psi) # Put psi into state |+>

def bob_gates(qc, qubit, crz, crx):
    # Uses qubit and classical bits to decide which gates to apply    
    # c_if is used to control our gates with a classical bit instead of a qubit
    qc.x(qubit).c_if(crx, 1) # Apply gate x if first classical bit is at 1
    qc.z(qubit).c_if(crz, 1) # Apply gate y if second classical bit is at 1

def teleportation_protocol(state_vector=None):
    try:
        # Create random 1-qubit state if none provided
        if state_vector is None:
            state_vector = random_statevector(2)
        
        # Show qubit state on a Bloch sphere
        display(array_to_latex(state_vector, prefix="|\\psi\\rangle ="))
        plot_bloch_multivector(state_vector)
        plt.show()

        # Initialize psi in circuit
        init_gate = Initialize(state_vector)
        init_gate.label = "init"

        #----BEGIN QUANTUM TELEPORTATION PROTOCOL----#

        # Qubit 0 (psi) is Alice's qubit which holds the information to be teleported, Qubit 1 (a) is Alice's placeholder, 
        # Qubit 2 (b) is Bob's qubit which will contain the teleported information
        qr = QuantumRegister(3, name="q")   # Protocol uses 3 qubits
        classic_z = ClassicalRegister(1, name="crz") # and 2 classical registers
        classic_x = ClassicalRegister(1, name="crx")
        qc = QuantumCircuit(qr, classic_z, classic_x)

        ## STEP 0
        # Initialize Alice's q0 information
        qc.append(init_gate, [0])

        ## STEP 1
        # Entangle q1 and q2
        entangle(qc, 1, 2)

        ## STEP 2
        # Send q1 to Alice and q2 to Bob
        alice_gates(qc, 0, 1)

        ## STEP 3
        # Alice then sends her classical bits to Bob
        measure(qc, 0, 1)

        ## STEP 4
        # Bob decodes qubits
        bob_gates(qc, 2, classic_z, classic_x)

        # Display the circuit
        qc.draw('mpl')
        plt.show()

        # Simulate the circuit
        sim = AerSimulator()
        qc.save_statevector()
        result = sim.run(qc).result()
        out_vector = result.get_statevector()

        # Plot the output state
        plot_bloch_multivector(out_vector)
        plt.show()

        # Benchmarking: Calculate fidelity
        fidelity = state_fidelity(state_vector, out_vector)
        print(f"Fidelity of the teleported state: {fidelity:.4f}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
teleportation_protocol()