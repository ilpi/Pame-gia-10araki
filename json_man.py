import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('yo.csv', names = ['Age', 'Gender', 'tb', 'db', 'AAP', 'SAA', 'SGAA', 'TP', 'ALB', 'A-G', 'Ok'], delimiter=',')
changes = {'Male': 0, 'Female': 1}
df['Gender'] = df['Gender'].replace(changes)

k = len(df.columns)
n = 2
m = (k - 1) // n + 1
fig, axes = plt.subplots(m, n, figsize=(n * 5, m * 3))
for i, (name, col) in enumerate(df.iteritems()):
    r, c = i // n, i % n
    ax = axes[r, c]
    col.hist(ax=ax)
    ax2 = col.plot.kde(ax=ax, secondary_y=True, title=name)
    ax2.set_ylim(0)

fig.tight_layout()
plt.show()