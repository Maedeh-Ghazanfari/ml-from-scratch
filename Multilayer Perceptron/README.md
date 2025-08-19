# Multilayer Perceptron (MLP) From Scratch

This repository contains a **from-scratch implementation of a simple Multilayer Perceptron (MLP)** in Python using only NumPy. The project was built as a learning exercise to understand the inner workings of feedforward, backpropagation, and optimization algorithms (like Adam).

## Features

- Forward propagation with **ReLU** and **Sigmoid** activations  
- Backpropagation for hidden and output layers  
- Gradient computation for weights and biases  
- Adam optimization implemented from scratch  
- Tested on small datasets (e.g., XOR problem)  

## Limitations / Known Issues

- Implementation may not converge perfectly for all datasets  
- Some parts of the optimization may require parameter tuning (learning rate, initialization, etc.)  
- Designed for **learning purposes**, not production use  

## Learning Goals

This project helped me understand:

- How MLPs perform forward and backward passes  
- Manual gradient computation  
- How Adam optimizer updates weights and biases  
- Common challenges in neural network implementations  

## Next Steps / Improvements

- Debug gradient and weight updates to ensure convergence  
- Extend to larger datasets and multiple hidden layers  
- Visualize loss over epochs  
- Compare manual implementation with TensorFlow or PyTorch  

