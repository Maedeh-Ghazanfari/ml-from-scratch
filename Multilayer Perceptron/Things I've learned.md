### Can I initialize weights and biases with any random number at the beginning?

Just watch out for symmetry problems! If all weights in a layer are initialized to the same value (e.g., zero), every neuron in that layer will produce identical outputs and receive identical gradients during training. This causes them to update in the same way, making neurons redundant and preventing the network from learning diverse features. To avoid this, weights are initialized with small random values to break symmetry, allowing neurons to learn different patterns.

#### Be careful:

If weights are too large, activations can explode (become huge), causing gradients to blow up.

If weights are too small, activations shrink toward zero, causing gradients to vanish.

Both exploding and vanishing gradients make training slow or unstable.

### Which activation function should I use?

For hidden layers -> ReLU is really good: 

##### Avoids vanishing gradients:
Unlike sigmoid or tanh, ReLU’s gradient is 1 for positive inputs, so it keeps the learning signal strong and helps deep networks train faster.

###### Computationally simple and efficient:
Just a max operation (max(0, x)), which is fast to compute.

###### Sparse activation:
ReLU outputs zero for all negative inputs, so many neurons don’t activate at once. This sparsity can help reduce overfitting and make the network more efficient.

###### Helps with convergence:
Empirically, networks with ReLU often converge faster and achieve better performance.
