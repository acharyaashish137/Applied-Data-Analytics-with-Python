import pandas as pd

# a. Creating a DataFrame named temperatures from a dictionary of three temperature readings each for three people ’Maxine’, ’James’ and ’Amanda’.

data = {'Maxine': [25, 28, 24],
        'James': [22, 24, 20],
        'Amanda': [27, 26, 23]}
temperatures = pd.DataFrame(data)

# b. Recreate the DataFrame temperatures in Part (a) with custom indices using the index keyword argument and a list containing ’Morning’, ’Afternoon’ and ’Evening’.

custom_indices = ['Morning', 'Afternoon', 'Evening']
temperatures_custom_index = pd.DataFrame(data, index=custom_indices)

# c. Select from temperatures the column of temperature readings for ’Maxine’.
maxine_temperatures = temperatures['Maxine']

# d. Select from temperatures the row of ’Morning’ temperature readings.

morning_temperatures = temperatures_custom_index.loc['Morning']

# e. Select from temperatures the rows for ’Morning’ and ’Evening’ temperature readings.

morning_evening_temperatures = temperatures_custom_index.loc[['Morning', 'Evening']]

# f. Select from temperatures the columns of temperature readings for ’Amanda’ and ’Maxine’.

amanda_maxine_temperatures = temperatures_custom_index[['Amanda', 'Maxine']]

# g. Select from temperatures the elements for ’Amanda’ and ’Maxine’ in the ’Morning’ and ’Afternoon’
amanda_maxine_morning_afternoon = temperatures_custom_index.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']]

# h. Use the describe() method to produce temperatures’ descriptive statistics
temperatures_describe = temperatures_custom_index.describe()

# i. Transpose the temperatures
temperatures_transposed = temperatures_custom_index.transpose()

# j. Sort temperatures so that its column names are in alphabetical order.
temperatures_sorted = temperatures_custom_index.sort_index(axis=1)

# Print the results
print("(a) DataFrame temperatures:")
print()
print(temperatures)
print("\n(b) DataFrame temperatures with custom indices:")
print(temperatures_custom_index)
print("\n(c) Maxine's temperatures:")
print(maxine_temperatures)
print("\n(d) Morning temperatures:")
print(morning_temperatures)
print("\n(e) Morning and Evening temperatures:")
print(morning_evening_temperatures)
print("\n(f) Amanda and Maxine's temperatures:")
print(amanda_maxine_temperatures)
print("\n(g) Amanda and Maxine's Morning & Afternoon temperatures:")
print(amanda_maxine_morning_afternoon)
print("\n(h) Descriptive statistics for temperatures:")
print(temperatures_describe)
print("\n(i) Transposed temperatures:")
print(temperatures_transposed)
print("\n(j) Sorted temperatures:")
print(temperatures_sorted)
