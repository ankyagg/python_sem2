import pandas as pd

iris = pd.read_csv("Iris.csv")

print("first 8 rows")
print(iris.head(8))

print("columns")
print(iris.columns)

print("fill")
iris_fill = iris.fillna(iris.mean(numerical_only=True))
print(iris_fill.head(3))

print("dropna")
iris_remove = iris.dropna()
print(iris_remove.head(3))
