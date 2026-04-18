import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# 1. Create dataset
data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "test_score": [35, 42, 50, 58, 65, 72, 78, 85, 91, 96]
}

df = pd.DataFrame(data)

print("\n--- DATASET ---")
print(df)


# 2. Prepare features and target
X = df[["hours_studied"]]
y = df["test_score"]


# 3. Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)


# 5. Make predictions on test data
y_pred = model.predict(X_test)

print("\n--- PREDICTIONS ON TEST DATA ---")
for actual, predicted in zip(y_test, y_pred):
    print(f"Actual: {actual} | Predicted: {predicted:.2f}")


# 6. Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- MODEL EVALUATION ---")
print(f"MSE: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")


# 7. Ask the user for multiple study hours
try:
    user_input = input(
        "\nEnter study hours separated by commas (example: 3,6,9): "
    )

    hours_list = [float(value.strip()) for value in user_input.split(",")]

    prediction_df = pd.DataFrame({"hours_studied": hours_list})
    predicted_scores = model.predict(prediction_df)

    print("\n--- USER PREDICTIONS ---")
    for hours, score in zip(hours_list, predicted_scores):
        print(f"{hours} study hours -> predicted test score: {score:.2f}")

    # 8. Create chart with all prediction points
    plt.figure(figsize=(8, 5))
    plt.scatter(df["hours_studied"], df["test_score"], label="Original data")
    plt.scatter(
        hours_list,
        predicted_scores,
        color="red",
        s=120,
        label="Predictions"
    )

    for hours, score in zip(hours_list, predicted_scores):
        plt.text(hours, score, f"({hours}, {score:.1f})")

    plt.xlabel("Hours Studied")
    plt.ylabel("Test Score")
    plt.title("Study Hours vs Test Score")
    plt.grid(True)
    plt.legend()
    plt.savefig("chart.png")
    print("\nChart saved as chart.png")

except ValueError:
    print("You must enter numbers separated by commas, for example: 3,6,9")