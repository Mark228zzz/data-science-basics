import numpy as np
import matplotlib.pyplot as plt

def sgd_momentum(
        x_start: int,
        learning_rate: float = 0.01,
        max_iter: int = 100,
        momentum: float = 0.9,
        grad_clip_value: float = 1.0
    ):
    """
    Perform Stochastic Gradient Descent (SGD) with momentum to optimize a function.

    :param x_start: Initial value for x.
    :param learning_rate: The step size for each update.
    :param max_iter: Maximum number of iterations.
    :param momentum: Momentum factor to accelerate convergence.
    :param batch_size: Number of samples used per update.
    :param grad_clip_value: Gradient clipping value to avoid overflow.

    :return: Optimized value of x after max_iter iterations.
    """
    x = x_start  # initial guess for x
    velocity = 0  # initialize the velocity (momentum term)
    history = []  # list to store the history of x for visualization

    # Perform SGD with momentum
    for i in range(max_iter):
        gradient = stochastic_gradient(x)  # dompute the gradient (stochastic gradient of the function)

        # dlip the gradient to prevent overflow
        gradient = np.clip(gradient, -grad_clip_value, grad_clip_value)

        # update the velocity using the gradient and momentum term
        velocity = momentum * velocity + learning_rate * gradient

        # update x using the velocity (momentum-adjusted gradient)
        x = x - velocity

        history.append(x)  # store the current value of x for plotting

        # print progress every 10 iterations
        if i % 10 == 0:
            print(f"Iteration {i}: {x = :.4f}, {gradient = :.4f}, {velocity = :.4f}")

    return x, history

def f(x):
    """
    A non-convex function to optimize.
    f(x) = x³ - 4x² + 2x
    """
    return x**3 - 4 * x**2 + 2 * x

def stochastic_gradient(x):
    """
    Compute the stochastic gradient (derivative) of f(x).
    f'(x) = 3x² - 8x + 2
    """
    return 3 * x**2 - 8 * x + 2

# start the SGD at x = 5
x_start = 5  # initial guess
optimized_x, history = sgd_momentum(x_start, learning_rate=0.01, max_iter=200, momentum=0.9, grad_clip_value=10.0)

# display the optimized value of x
print(f"Optimized value of x: {optimized_x:.4f}")

# plot the function and the optimization path
x_vals = np.linspace(-1, 6, 100)  # values for plotting the function
y_vals = f(x_vals)  # compute the function values

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x) = x³ - 4x² + 2x")  # plot the function
plt.scatter(history, f(np.array(history)), color='r', label="Optimization Path")  # plot the optimization path
plt.title("Stochastic Gradient Descent with Momentum on a Non-Convex Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
