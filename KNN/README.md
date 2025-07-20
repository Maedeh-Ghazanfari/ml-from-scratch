This project implements the K-Nearest Neighbors (KNN) algorithm from scratch using a rice dataset containing features of two rice varieties: Cammeo and Osmancik. The goal is to classify the rice grains based on their morphological features using a non-library KNN algorithm.

📊 Exploratory Data Analysis (EDA)
The notebook performs initial EDA, including:

Dataset summary and null/duplicate checks

Class balance check

Feature distribution histograms

Correlation heatmap and scatter matrix to detect multicollinearity

⚙️ Preprocessing
Removal of highly correlated features (Area)

One-hot encoding of the target label (for analysis)

Feature normalization using Min-Max scaling

Train-test split (80% training, 20% testing)

🤖 KNN Implementation (from Scratch)
The algorithm includes:

Custom Euclidean distance function

Manual looping through test data

Distance calculation between test and train points

Selecting the k=7 nearest neighbors

Majority voting using collections.Counter

📈 Evaluation
Model evaluation includes:

Accuracy score

Classification report (precision, recall, F1-score)

🧠 Key Takeaways
Implemented KNN from scratch without using KNeighborsClassifier

Understood the importance of normalization in distance-based algorithms

Explored the real-world use case of classifying rice varieties based on shape features
