import matplotlib.pyplot as plt
import numpy as np

# Définition des points du casque
points = np.array([[0, 0], [0, 1], [0.2, 1.2], [0.4, 1.4], [0.6, 1.5], [0.8, 1.4], [1, 1.2], [1, 1], [1, 0], [0.8, -0.2], [0.6, -0.4], [0.4, -0.5], [0.2, -0.4], [0, -0.2]])

# Tracé du casque
plt.plot(points[:, 0], points[:, 1])
plt.axis("equal")
plt.show()
