import numpy as np
import pyphi
from pyphi import Network, compute
pyphi.config.PROGRESS_BARS = False
tpm = np.array([[0,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
cm = np.ones((4,4)) - np.eye(4)
n = Network(tpm, cm=cm)
print("Φ =", compute.phi(n, (0,0,0,0)))
