import numpy as np
import matplotlib.pyplot as plt

# Données d'Anscombe
x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

x2 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])

x3 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], dtype=float)
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])

x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8], dtype=float)
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

Xs = [x1, x2, x3, x4]
Ys = [y1, y2, y3, y4]

# 1) Moyenne et variance (variance empirique ddof=1)
print("Moyennes et variances :")
for i, (x, y) in enumerate(zip(Xs, Ys), start=1):
    print(f"x{i}: mean={x.mean():.3f}, var={x.var(ddof=1):.3f}")
    print(f"y{i}: mean={y.mean():.3f}, var={y.var(ddof=1):.3f}")
    print()

# 2) Coefficients de corrélation
print("Corrélations :")
for i, (x, y) in enumerate(zip(Xs, Ys), start=1):
    r = np.corrcoef(x, y)[0, 1]
    print(f"corr(x{i}, y{i}) = {r:.3f}")

# 3) Tracés des nuages de points
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes = axes.ravel()

for i, (ax, x, y) in enumerate(zip(axes, Xs, Ys), start=1):
    ax.scatter(x, y)
    ax.set_title(f"Série {i}")
    ax.set_xlabel(f"x{i}")
    ax.set_ylabel(f"y{i}")

plt.tight_layout()
plt.show()
