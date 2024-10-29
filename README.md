# Quantum Teleportation

This project simulates the quantum teleportation process of a single quantum bit (qubit) over a fully-entangled channel using Qiskit.

## Open in Google Colab

You can run this project in Google Colab by clicking [here](https://colab.research.google.com/drive/1ke1t24idpjMXDOrEvY7IDFalxEdMPm8Y).

## Open in IBM Quantum Composer

You can also run this project in IBM Quantum Composer by clicking [here](https://shorturl.at/hik36).

## Problem Statement

Let's say a person called Alice wants to send the qubit state
$\vert\psi\rangle = \alpha\vert0\rangle + \beta\vert1\rangle$ to Bob. This entails passing on information about $\alpha$ and $\beta$ to Bob.
Alice can't simply generate a copy of $\vert\psi\rangle$ and give the copy to Bob because of the no-cloning theorem, which states that you cannot simply make an exact copy of an unknown quantum state. We are limited to copying only classical states (not superpositions).
However, by taking advantage of two classical bits and an entangled qubit pair, Alice can transfer her state $\vert\psi\rangle$ to Bob. After the transfer, Bob will have $\vert\psi\rangle$ and Alice won't. This is called Quantum Teleportation.

## Simulating the Quantum Teleportation Process

To transfer a quantum bit, Alice and Bob must use a third party to send them an entangled qubit pair. Alice then performs some operations on her qubit, sends the results to Bob over a classical communication channel, and Bob then performs some operations on his end to receive Alice’s qubit. The process is as follows:

### Step 1

A third party, Telamon, creates an entangled Bell pair of qubits and gives one to Bob and one to Alice. In quantum circuit language, the way to create a Bell pair between two qubits is to first transfer one of them to the X-basis ($|+\rangle$ and $|-\rangle$) using a Hadamard gate, and then to apply a CNOT gate onto the other qubit controlled by the one in the X-basis. 

### Step 2 

Let's say Alice owns $q_1$ and Bob owns $q_2$ after they part ways.
Alice applies a CNOT gate to $q_1$, controlled by $\vert\psi\rangle$ (the qubit she is trying to send Bob). Then Alice applies a Hadamard gate to $|\psi\rangle$. In our quantum circuit, the qubit ($|\psi\rangle$) Alice is trying to send is $q_0$.

### Step 3

Next, Alice applies a measurement to both qubits that she owns, $q_1$ and $\vert\psi\rangle$, and stores this result in two classical bits. She then sends these two bits to Bob.

### Step 4

Bob, who already has the qubit $q_2$, then applies the following gates depending on the state of the classical bits:

- 00 $\rightarrow$ Do nothing
- 01 $\rightarrow$ Apply $X$ gate
- 10 $\rightarrow$ Apply $Z$ gate
- 11 $\rightarrow$ Apply $ZX$ gate

(*Note that this transfer of information is purely classical*.)

## Files

- `Quantum_Teleportation.py`: Contains the implementation of the quantum teleportation protocol.
- `Quantum_Teleportation.ipynb`: Jupyter notebook demonstrating the quantum teleportation process step-by-step.
- `README.md`: This file.
- `requirements.txt`: List of dependencies required to run the project.

## Usage

To run the quantum teleportation protocol, execute the `Quantum_Teleportation.py` script:

```sh
python [Quantum_Teleportation.py]
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.