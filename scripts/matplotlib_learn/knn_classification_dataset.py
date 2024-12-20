from sklearn.datasets import make_classification  # to generate synthetic dataset
import matplotlib.pyplot as plt  # for plotting

# Generate synthetic dataset
X, y = make_classification(
    n_samples=400,  # number of data points in the dataset
    n_features=2,   # number of features (2D data for visualization)
    n_informative=2,  # both features are informative (helpful for classification)
    n_redundant=0,  # no redundant features (no artificial correlations)
    n_classes=2    # two classes for binary classification
)

# visualization of the generated dataset
plt.figure(figsize=(8, 8))  # Set the figure size to 8x8 inches
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolor="k", s=65)  # scatter plot of the data points
# X[:, 0] and X[:, 1] represent the two features, c=y colors the points based on the target class (0 or 1)

# labeling the axes and giving a title to the plot
plt.xlabel("Feature1")  # label for the X-axis (first feature)
plt.ylabel("Feature2")  # label for the Y-axis (second feature)
plt.title("Dataset")  # Title for the plot

# show the plot
plt.show()  # display the plot
