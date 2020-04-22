import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
import paillier as p
priv, pub = p.generate_keypair(128)


X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8 ]])
X = np.int_(X)
X = X.tolist()
Y = []
# array = np.arange().reshape(X.shape[0],X.shape[1])
# Y = np.zeros((X.shape[0],X.shape[1]))
# Y.astype(int)
# X = X.astype(int)
# X = np.int_(X)
# print(X.shape)
i=0
print(X)
for x in X:
    x = p.encryptArray(pub, x)
    Y.append(x)
    i+=1
# print(Y)
i=0
z =[]# np.zeros((X.shape[0],X.shape[1]))
for y in Y:
    y = p.decryptArray(priv, pub, y)
    z.append(y)
    i+=1
print(z)
X = np.array(Y, dtype=float)
#plt.scatter(X[:,0], X[:,1], s=150)
#plt.show()

colors = 10*["g","r","c","b","k"]


class K_Means:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self,data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    print(np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    optimized = False

            if optimized:
                break

    def predict(self,data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


clf = K_Means()
clf.fit(X)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)

##unknowns = np.array([[1,3],
##                     [8,9],
##                     [0,3],
##                     [5,4],
##                     [6,4],])
##
##for unknown in unknowns:
##    classification = clf.predict(unknown)
##    plt.scatter(unknown[0], unknown[1], marker="*", color=colors[classification], s=150, linewidths=5)
##

plt.show()