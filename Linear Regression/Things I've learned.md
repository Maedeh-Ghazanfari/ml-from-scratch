What is Normal Equation in Linear Regression?

The Normal Equation is a neat closed-form way to solve Linear Regression WITHOUT using gradient descent. This directly computes the weights w that minimize the Mean Squared Error.

Why does it work?

Because it's derived by setting the gradient of the cost function (MSE) to zero and solving for w, this gives you the exact solution that minimizes the loss. You’re solving the equation where the "slope" of the loss function becomes zero — meaning you've reached the minimum point of the cost function.

<img width="951" height="461" alt="image" src="https://github.com/user-attachments/assets/68969532-6898-4dbc-87c8-1c3d7aba530a" />

Comparing it to Gradient Descent:

<img width="932" height="176" alt="image" src="https://github.com/user-attachments/assets/de5084cc-0005-420f-b782-b452f6695871" />

Scaling is important in Gradient Descent.
