import pandas as pd
import math

class K_Means:

    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations




df = pd.read_csv(r".\data\ipl_bowlers_norm.csv")
df = df[['one', 'two']]
dataset = df.astype(float).values.tolist()

X = df.values  # returns a numpy array



def euclidean_distance(feat_one, feat_two):
    squared_distance = 0
    for i in range(len(feat_one)):
        squared_distance += (feat_one[i] - feat_two) ** 2

    ed = math.sqrt(squared_distance)

    return ed


# initialize the centroids, the first 'k' elements in the dataset will be our initial centroids
for i in range(self.k):
    self.centroids[i] = data[i]

for i in range(self.max_iterations):
    self.classes = {}
    for i in range(self.k):
        self.classes[i] = []

    # find the distance between the point and cluster; choose the nearest centroid
    for features in data:
        distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        self.classes[classification].append(features)

previous = dict(self.centroids)

# average the cluster datapoints to re-calculate the centroids
for classification in self.classes:
    self.centroids[classification] = np.average(self.classes[classification], axis=0)

isOptimal = True

for centroid in self.centroids:

    original_centroid = previous[centroid]
    curr = self.centroids[centroid]

    if np.sum((curr - original_centroid) / original_centroid * 100.0) > self.tolerance:
        isOptimal = False

# break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)

if isOptimal:
    break

km = K_Means(3)
km.fit(X)

# Plotting starts here, the colors
colors = 10 * ["r", "g", "c", "b", "k"]

for centroid in km.centroids:
    plt.scatter(km.centroids[centroid][0], km.centroids[centroid][1], s=130, marker="x")

for classification in km.classes:
    color = colors[classification]
    for features in km.classes[classification]:
        plt.scatter(features[0], features[1], color=color, s=30)

plt.show()