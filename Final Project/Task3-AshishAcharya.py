import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

# Load the Digits dataset
digits = load_digits()

# Task (a): Display the two-dimensional array and numeric value of the digit at index 35
sample_image = digits.images[35]
target_value = digits.target[35]
print("Sample Image:")
print(sample_image)
print()

print("Target Value:", target_value)


# Task (b): Display the image at index 35 of the Digits dataset
plt.imshow(sample_image, cmap='gray')
plt.title(f"Sample Image at Index 35 (Digit {target_value})")
plt.show()

# Task (c): Train-test split and numbers of training/testing samples
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, random_state=11, test_size=0.70
)
num_train_samples = len(X_train)
num_test_samples = len(X_test)
print("Number of Training Samples:", num_train_samples)
print("Number of Testing Samples:", num_test_samples)

print()
# Task (d): Display the number of training examples and testing examples
print("Number of Training Examples:", num_train_samples)
print("Number of Testing Examples:", num_test_samples)
print()

# Task (e): Rewrite the list comprehension using a for loop
predicted_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
expected_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
wrong_predictions = []

for predicted, expected in zip(predicted_values, expected_values):
    if predicted != expected:
        wrong_predictions.append((predicted, expected))

# Task (f): Explanation for row 3 of the confusion matrix
confusion_row_values = [10, 5, 120, 0, 3, 2, 0, 1, 8, 1]
print("Explanation for confusion matrix row 3:")
for i, count in enumerate(confusion_row_values):
    print(f"Predicted as {i}: {count} times")
