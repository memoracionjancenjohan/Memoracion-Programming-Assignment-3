# Memoracion-Programming-Assignment-3
# 📝 Instructions (PA 3)

## 📌Problem 1
**`import pandas as pd`** uses the pandas library in order to use its functions.
Download the file `cars.csv` to folder that contains the code file.

- `cars = pd.read_csv('cars.csv')` assigns the csv file to a DataFrame then stores it into a variable named `cars`
- `cars.head()` prints out the first 5 rows of the `cars`
- `cars.tail()` prints out the last 5 rows of the `cars`

---

## 📌Problem 2
**`import pandas as pd`** uses the pandas library in order to use its functions.
Download the file `cars.csv` to folder that contains the code file.

- `cars = pd.read_csv('cars.csv')` assigns the csv file to a DataFrame then stores it into a variable named `cars`
- `cars.iloc[:5, ::2]` displays the first five rows of car models as denoted by `:5` and displays the odd numbered specification columns as denoted by `::2`
- `cars[0:1]` displays the row where it contains the `Model` of **Mazda RX4**
- `cars.loc[[23], ['Model', 'cyl']]` displays how many cylinders Camaro Z28 which is located at row 23
- `cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]` displays cylinders and gear type of the cars at row 1, 28, and 18

