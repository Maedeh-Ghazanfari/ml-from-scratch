KNN is a lazy algorithm (also known as an instance-based learner), which means there is no need for learning and training. It does more work during the test phase, unlike eager learners.
KNN algorithm is mostly robust to outliers.

kNN is sensitive to multicollinearity. But why? If two features are highly correlated, they double-count the same information, which distorts distances. As a result, some features dominate the distance metric more than they should.

Scaling is important in distance-based algorithms (like kNN, SVM, or gradient descent-based models).
