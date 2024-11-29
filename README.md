
# ft_linear_regression

Create a simple lineal regresion from a data set to predict the price of a car depending on it's Km

## Basic Concepts
Linear regression is a model that uses a straight line to show how one variable depends on another, including a margin of error for the unpredictable. In a easy go to understand, is like a mean representend in a linear way that gives you the more approximated output value y to its corresponding input value x.

The formula of a simple linear regresion is the next one: $y = mx + b$

### Where:
- **\( y \)**: The dependent variable (the value we want to predict).
- **\( x \)**: The independent variable (the input or feature).
- **\( m \)**: The slope of the line (how much \( y \) changes for a one-unit change in \( x \)).
- **\( b \)**: The y-intercept (the value of \( y \) when \( x = 0 \)).
## Main objective
The goal of linear regression is to find the parameters (\( m \) and \( b \)) that minimize the **Mean Squared Error (MSE)**, which measures the discrepancy between the predicted values (\( \hat{y} \)) and the actual values (\( y \)):

$$
J(m, b) = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2
$$

### Where:
- **J(m, b)**: The cost function (average error).
- **n**: The number of examples in the dataset.
- $\hat{y}_i$ = m x_i + b$: The predicted value for the $i$-th example.
- $y_i$: The actual value for the $i$-th example.

### Parabola
To understand it better, this three variable function is a convex one, so representend in a 3D plane it will be a parabola. This means that the curve forms a "bowl" shape, and in it's lowest point, in the minimun, is the value we want to find. It's the poiint that indicates us the best m and b values to minimize the error.
## Gradient Method
To find this find the (\( m \) and \( b \)) that minimize the MSE we have to try with different values of m and b until we find the minimal ones. But if we try this values in a random way finding the correct ones will be eternal. That's way we use the **Gradient Method**.


The **gradient** is a vector that contains the partial derivatives of the cost function \( J(m, b) \) with respect to each coefficients. These derivatives tell us the direction of the steepest ascent of \( J(m, b) \).

### Partial Derivative with Respect to \( m \) (Slope):

The partial derivative of \( J(m, b) \) with respect to the slope \( m \) is:

$$
\frac{\partial J(m, b)}{\partial m} = \frac{1}{n} \sum_{i=1}^{n} (y_i - (mx_i + b)) \cdot x_i
$$

Where:

- $x_i$: The value of the independent variable $x$ for the $i$-th example.
- $y_i - (mx_i + b)$: The residual or error of the $i$-th example (the difference between the predicted and actual values).

### Partial Derivative with Respect to \( b \) (Intercept):

The partial derivative of $J(m, b)$ with respect to the intercept $b$ is:

$$
\frac{\partial J(m, b)}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (y_i - (mx_i + b))
$$

Where:

- $y_i - (mx_i + b)$: The residual or error of the $i$-th example.


## Gradient Descent

As we have seen the gradient indicate us the direction of the steepest ascent, but we want to find the minimum, the deepest point. So to minimize $J(m, b)$, we move in the opposite direction of the gradient.

$$
m = m - \alpha \cdot \frac{\partial J(m, b)}{\partial m}
$$

$$
b = b - \alpha \cdot \frac{\partial J(m, b)}{\partial b}
$$

Where:

- $\alpha$ is the **learning rate**, a small value that controls how much the parameters $m$ and $b$ are adjusted during each iteration.
- The partial derivatives $\frac{\partial J(m, b)}{\partial m}$ and $\frac{\partial J(m, b)}{\partial b}$ guide the direction of the update for each parameter.

This process is repeated for a set number of iterations or until the cost function converges to a minimum.
