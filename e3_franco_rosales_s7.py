import numpy as np

matriz = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)

suma=0
for i in matriz:
    for j in i:
        suma+=j

print(suma)
