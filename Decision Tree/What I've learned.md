Decision Tree is a non parametric algorithm -> It learns structure from the data itself (e.g., where to split based on feature values). Model complexity grows as data grows.

More flexible and can fit complex patterns, but can overfit if not controlled.


| Advantages                                  | Disadvantages                     
| ------------------------------------------- | --------------------------------------------------------------------------------|
| Easy to interpret and visualize             | Prone to overfitting (complex trees memorize noise)                             |
| Handles both categorical and numerical data | Can be unstable — small changes in data can cause big changes in tree structure |
| No need for feature scaling                 | Greedy algorithm — finds locally optimal splits, not guaranteed global optimum  |
| Captures non-linear relationships           |
| Can handle missing values and outliers well |


**What is the CART algorithm?**

CART stands for Classification and Regression Trees. It is a popular algorithm for building decision trees used for both classification and regression tasks.

| Feature                      | CART                                          | Other Trees Examples                                                       |
| ---------------------------- | --------------------------------------------- | -------------------------------------------------------------------------- |
| Splitting style              | Binary splits only                            | Can be multiway splits (e.g., ID3, C4.5)                                   |
| Classification impurity      | Gini impurity                                 | Often use entropy (ID3, C4.5)                                              |
| Regression splitting         | MSE or variance reduction                     | Some methods use different criteria                                        |
| Handles categorical features | Usually requires encoding or special handling | Some (like C4.5) handle categorical features natively with multiway splits |
| Developed for                | Both classification & regression              | Some only classification (ID3)                                             |


When you use libraries like scikit-learn’s DecisionTreeClassifier/Regressor, you’re using CART.


You need to restrict the Decision Tree's freedom during training. This is called Regularization(a technique used in machine learning to prevent overfitting by discouraging overly complex models).

You can at least restrict the maximum depth of the Decision Tree.



