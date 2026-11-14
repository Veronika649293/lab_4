import matplotlib.pyplot as plt
import numpy as np

# Вихідні дані: сподівані норми прибутку та середньоквадратичні відхилення (ризики)
m = np.array([20.0, 40.0, 60.0])
s = np.array([10.0, 18.0, 30.0])

# Коефіцієнти кореляції
R = np.array([[1, 1, -1], [1, 1, -1], [-1, -1, 1]])
Cov = np.outer(s, s) * R

# Генерація множини допустимих ПЦП методом сітки 
grid = []
for x1 in np.linspace(0, 1, 101):
  for x2 in np.linspace(0, 1 - x1, 101):
    x3 = max(0.0, 1.0 - x1 - x2)
    mp = 20 * x1 + 40 * x2 + 60 * x3
    sp = abs(10 * x1 + 18 * x2 - 30 * x3) 
    grid.append((sp, mp, x1, x2, x3))

grid = np.array(grid)

# Побудова графіку
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(
    grid[:, 0],
    grid[:, 1],
    s=2,
    alpha=0.3,
    color='steelblue',
    label='Множина допустимих ПЦП',
)

# Ключові точки
pts = {
    'A1 (1; 0; 0)': (10, 20),
    'A2 (0; 1; 0)': (18, 40),
    'A3 (0; 0; 1)': (30, 60),
    'Z1 (0; 0,625; 0,375)': (0, 47.5),
    'Z2 (0,75; 0; 0,25)': (0, 30.0),
}

for label, (sx, my) in pts.items():
  ax.scatter([sx], [my], color='black', zorder=5)
  offset = (6, -4) if 'A1' in label or 'Z2' in label else (6, 4)
  ax.annotate(
      f'{label}\n({sx}%, {my}%)',
      (sx, my),
      xytext=offset,
      textcoords='offset points',
      fontsize=9,
  )

# Лінія ефективних ПЦП
ax.plot(
    [0, 30],
    [47.5, 60],
    color='crimson',
    linewidth=2.5,
    label='Множина ефективних ПЦП (Z1 → A3)',
)

ax.set_title(
    'Множини допустимих та ефективних портфелів цінних паперів (варіант 3)'
)
ax.set_xlabel('Ризик портфеля, σ_П (%)')
ax.set_ylabel('Сподівана норма прибутку, m_П (%)')
ax.set_xlim(-1.5, 35)
ax.set_ylim(15, 65)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='lower right')
plt.tight_layout()
plt.show()

