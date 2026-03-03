import numpy as np
import pyphi
from pyphi import Network, compute
pyphi.config.PROGRESS_BARS = False
pyphi.config.VALIDATE_SUBSYSTEM_STATES = False
tpm = np.array([[0,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
cm = np.ones((4,4)) - np.eye(4)
network = Network(tpm, cm=cm, node_labels=("A","B","C","D"))
phi = compute.phi(network, (0,0,0,0))
print(f"Phi = {phi:.4f} — NullLab seeds now measurable")
