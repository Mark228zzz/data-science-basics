import numpy as np

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

