import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/ori_test.csv')
img1 = data.values[1]

pix = []
for i in range(28):
    pix.append([])
    for j in range(28):
        pix[i].append(img1[i*28+j])

plt.imshow(pix, cmap=plt.cm.binary)
plt.show()
