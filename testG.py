# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
tab=[[20, 20, 81],
  [21, 31, 23],
  [20, 16, 1],
  [57, 5, 74],
  [12, 4, 26],
  [32, 6, 54],
  [9, 35, 12],
  [16, 27, 15],
  [2, 40, 13]
]
# Create a dataset:
d = {'x': [], 'y': []}

for i in range (len(tab)):
  
  d['x'].append(tab[i][0])
  d['y'].append(tab[i][1])
df = pd.DataFrame(data=d)
# plot
plt.plot( 'x','y', data=df, linestyle='none', marker='o')

plt.show()
