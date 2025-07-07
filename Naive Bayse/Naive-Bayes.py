# Importing packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Importing dataset
df = pd.read_csv(r'C:\Users\Lenovo\Desktop\ML-print\data\Breast_cancer_data.csv')

# Plot to check distribution of diagnosis in dataset
sns.set()
data = df['diagnosis']
sns.histplot(data=data)
plt.show()

# Checking for independency of features
corr_plot = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)
plt.show()

# Selecting features(Based on independency)
df = df[['mean_radius', 'mean_texture', 'mean_perimeter', 'diagnosis']]

sns.histplot(data=df['mean_radius'], kde=True)
plt.show()
sns.histplot(data=df['mean_texture'], kde=True)
plt.show()
sns.histplot(data=df['mean_perimeter'], kde=True)
plt.show()


# Calculating likelihood
def calc_likelihood(data_frame, col_feature, col_feature_value, label_col, label):
    data_frame = data_frame.loc[data_frame[label_col] == label]
    mean = data_frame[col_feature].mean()
    std = data_frame[col_feature].std()
    likelihood = (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-(col_feature_value - mean) ** 2 / (2 * std ** 2))
    return likelihood


def calc_prior(data_frame, col):
    unique_values_for_prior = sorted(list(data_frame[col].unique()))
    prior = []
    for i in unique_values_for_prior:
        p = len(data_frame.loc[data_frame[col] == i]) / len(data_frame[col])
        prior.append(p)
    return prior


def naive_bayes(df, X, Y):
    # get feature names
    features = list(df.columns)[:-1]

    # calculate prior
    prior = calc_prior(df, Y)

    Y_pred = []
    # loop over every data sample
    for x in X:
        # calculate likelihood
        labels = sorted(list(df[Y].unique()))
        likelihood = [1]*len(labels)
        for j in range(len(labels)):
            for i in range(len(features)):
                likelihood[j] *= calc_likelihood(df, features[i], x[i], Y, labels[j])

        # calculate posterior probability (numerator only)
        post_prob = [1]*len(labels)
        for j in range(len(labels)):
            post_prob[j] = likelihood[j] * prior[j]

        Y_pred.append(np.argmax(post_prob))

    return np.array(Y_pred)


train, test = train_test_split(df, test_size=2, random_state=41)
x_test = test.iloc[:, :-1].values
y_test = test.iloc[:, -1].values
y_pred = naive_bayes(train, x_test, "diagnosis")

print(f1_score(y_test, y_pred))
