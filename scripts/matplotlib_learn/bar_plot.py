import matplotlib.pyplot as plt

# define categories and their corresponding values
categories = ['A', 'B', 'C', 'D']
values = [3, 12, 5, 25]

# Create a bar plot
plt.bar(categories, values, color=['blue', 'orange', 'green', 'red'])
plt.title('Bar Plot')  # add title
plt.xlabel('Categories')  # label x-axis
plt.ylabel('Values')  # label y-axis
plt.show()
