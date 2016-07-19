import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from sklearn.cluster import KMeans
from sklearn import datasets

centers = [[1, 1], [-1, -1], [1, -1]]
IrisData = datasets.load_iris().data
IrisTarget = datasets.load_iris().target

####################
# Testing: KMeans
####################
name = 'k_means_iris_3'
est = KMeans(n_clusters=3)
est.fit(IrisData)
labels = est.labels_

####################
# Testing: plotting
####################
fig = plt.figure()

ax = fig.add_subplot(121, projection='3d')
ax.view_init(elev=48, azim=134)
# ax.w_xaxis.set_ticklabels([])
# ax.w_yaxis.set_ticklabels([])
# ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Petal width')
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
for name, label in [('#1', 0), ('#2', 1), ('#3', 2)]:
    # ax.text3D(IrisData[IrisTarget == label, 3].mean(),
    #           IrisData[IrisTarget == label, 0].mean() + 1.5,
    #           IrisData[IrisTarget == label, 2].mean(), name, horizontalalignment='center', bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
    ax.text3D(IrisData[IrisTarget == label, 3].mean(),
              IrisData[IrisTarget == label, 0].mean() + 1.5,
              IrisData[IrisTarget == label, 2].mean(), name)
ax.scatter(IrisData[:, 3], IrisData[:, 0], IrisData[:, 2], c=labels)

####################
# Reference: Plotting
####################

# plt.cla()

# Reorder the labels to have colors matching the cluster results
IrisTarget = np.choose(IrisTarget, [1, 2, 0]).astype(np.float)

ax = fig.add_subplot(122, projection='3d')
ax.view_init(elev=48, azim=134)
# ax.w_xaxis.set_ticklabels([])
# ax.w_yaxis.set_ticklabels([])
# ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Petal width')
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
for name, label in [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]:
    ax.text3D(IrisData[IrisTarget == label, 3].mean(),
              IrisData[IrisTarget == label, 0].mean() + 1.5,
              IrisData[IrisTarget == label, 2].mean(), name)
ax.scatter(IrisData[:, 3], IrisData[:, 0], IrisData[:, 2], c=IrisTarget)

plt.show()
