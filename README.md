
# ft_linear_regression

Create a simple lineal regresion from a data set to predict the price of a car depending on it's Km

## Basic Concepts
Linear regression is a model that uses a straight line to show how one variable depends on another, including a margin of error for the unpredictable. In a easy go to understand, is like a mean representend in a linear way that gives you the more approximated output value y to its corresponding input value x.

The formula of a simple linear regresion is the next one: $y = mx + b$

### Where:
- **y**: The dependent variable (the value we want to predict).
- **x**: The independent variable (the input or feature).
- **m**: The slope of the line (how much $y$ changes for a one-unit change in $x$.
- **b**: The y-intercept (the value of $y$ when $x = 0$.
## Main objective
The goal of linear regression is to find the parameters $m$ and $b$ that minimize the **Mean Squared Error (MSE)**, which measures the discrepancy between the predicted values $\hat{y}$ and the actual values $y$:

$$
J(m, b) = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2
$$

### Where:
- **J(m, b)**: The cost function (average error).
- **n**: The number of examples in the dataset.
- $\hat{y}_i$ = m x_i + b$: The predicted value for the $i$-th example.
- $y_i$: The actual value for the $i$-th example.

<img src="https://i.imgur.com/tqnei6J.jpg" width="500">

### Parabola
To understand it better, this three variable function is a convex one, so representend in a 3D plane it will be a parabola. This means that the curve forms a "bowl" shape, and in it's lowest point, in the minimun, is the value we want to find. It's the poiint that indicates us the best $m$ and $b$ values to minimize the error.

<img src="https://shorturl.at/e6Jp7" width="500">

## Gradient Method
To find this find the $m$ and $b$ that minimize the MSE we have to try with different values of m and b until we find the minimal ones. But if we try this values in a random way finding the correct ones will be eternal. That's way we use the **Gradient Method**.


The **gradient** is a vector that contains the partial derivatives of the cost function $J(m, b)$ with respect to each coefficients. These derivatives tell us the direction of the steepest ascent of $J(m, b)$.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Gradient2.svg/512px-Gradient2.svg.png?20210513164705" width="500">

### Partial Derivative with Respect to $m$ (Slope):

The partial derivative of $J(m, b)$ with respect to the slope $m$ tell us the direction of the steepest ascent of $J(m, b)$ in the $m$ axis having a fiexd $b$:

$$
\frac{\partial J(m, b)}{\partial m} = \frac{1}{n} \sum_{i=1}^{n} (y_i - (mx_i + b)) \cdot x_i
$$

Where:

- $x_i$: The value of the independent variable $x$ for the $i$-th example.
- $y_i - (mx_i + b)$: The residual or error of the $i$-th example (the difference between the predicted and actual values).

### Partial Derivative with Respect to $b$ (Intercept):

The partial derivative of $J(m, b)$ with respect to the intercept $b$ tell us the direction of the steepest ascent of $J(m, b)$ in the $b$ axis having a fiexd $m$:

$$
\frac{\partial J(m, b)}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (y_i - (mx_i + b))
$$

Where:

- $y_i - (mx_i + b)$: The residual or error of the $i$-th example.


## Gradient Descent

As we have seen the gradient indicate us the direction of the steepest ascent, but we want to find the minimum, the deepest point. So to minimize $J(m, b)$, we move in the opposite direction of the gradient. In case that you think that the gradient could point to the wrong minium value dont worry, like the $J(m, b)$ function is a parabolla it only has one minimun. So the gradient alway is going to point to the good direction.

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

<img src="https://doimages.nyc3.cdn.digitaloceanspaces.com/010AI-ML/content/images/2018/05/fastlr.png" width="500">

## Setting the gradient to zero when we have a simple linear regression (two variables, $y = mx + b$)
The best way to get a linear regression for most of the data set it's using the gradient descent method. However when you only have 2 variables it will be possible to achive a better result using another and shorter method.

Setting the gradient to zero is better because it provides a **direct solution**. The formulas for $m$ and $b$ can be derived algebraically, and solving them requires only a single computation, regardless of the dataset size. This approach avoids the iterative process of gradient descent, making it faster and computationally cheaper in this case.

To find the slope $m$ and intercept $b$ by setting the gradients of the cost function to zero, we derive the following equations:

1. **Partial derivative with respect to $m$:**

   $\frac{\partial J}{\partial m} = -\frac{2}{n} \sum_{i=1}^{n} x_i \left( y_i - (m x_i + b) \right) = 0$

   Simplifies to:
   $\sum_{i=1}^{n} x_i y_i = m \sum_{i=1}^{n} x_i^2 + b \sum_{i=1}^{n} x_i$

3. **Partial derivative with respect to $b$:**

   $\frac{\partial J}{\partial b} = -\frac{2}{n} \sum_{i=1}^{n} \left( y_i - (m x_i + b) \right) = 0$

   Simplifies to:
   $\sum_{i=1}^{n} y_i = m \sum_{i=1}^{n} x_i + n b$

These two equations form a system that can be solved to compute $m$ and $b$.

### Why Set the Gradient to Zero?

The **derivative** of a function tells us how the slope of the function changes at any given point. If the derivative is positive, the function is increasing; if it’s negative, it’s decreasing. If the derivative is zero, the slope is **horizontal** — the tangent line is flat at that point.

In linear regression, the derivative of the error function with respect to the parameters \( m \) (slope) and \( b \) (intercept) tells us how the error changes when we adjust these parameters. By **setting the derivative to zero**, we find the point where the slope of the error function is horizontal, meaning the error can no longer decrease or increase — it has reached its **minimum**.

#### Summary:
- **Derivative = 0**: The slope of the error function is zero (the tangent is horizontal).
- In linear regression, the error function is convex, so the point where the derivative is zero corresponds to the **global minimum**, which gives us the optimal values for \( m \) and \( b \) (the best-fitting line).

## Why Gradient Descent is More Efficient for Many Variables

1. **Direct Method (Matrix Inversion)**:
   - For multiple variables, solving $\mathbf{w} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ requires matrix inversion, which has a cost of $O(k^3)$, where $k$ is the number of variables.
   - This approach becomes computationally expensive and memory-intensive for large datasets.

2. **Gradient Descent**:
   - Updates parameters iteratively, with a cost of $O(nk)$ per iteration, where $n$ is the number of data points.
   - Scales better for high-dimensional data and avoids storing large matrices.

**Summary**: Gradient descent is preferred for many variables because it avoids the high computational cost of matrix inversion and is more efficient with large datasets.
