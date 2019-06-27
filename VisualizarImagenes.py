import matplotlib.pyplot as plt
import numpy as np

#Importando imagenes
im=plt.imread("Original.jpg")
im1=plt.imread("Edges.jpg")
I=[im,im1]
fig, axs = plt.subplots(2, sharex=True, sharey=True, gridspec_kw={'hspace': 0})
#fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20,10))
fig.suptitle('Imagenes tomadas por camara')
for c, ax in zip(range(2), axs):
    ax.imshow(I[c])
    ax.set_axis_off()
plt.show()
