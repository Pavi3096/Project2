import numpy as np

x_values = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y_values = np.array([13,8,6,11,12,6,9,3,4,17,10,5])

def best_fit_line (x_values, y_values):
    m = (((x_values.mean() * y_values.mean()) - (x_values * y_values).mean() ) /
        ( (x_values.mean()) ** 2 - (x_values ** 2 ).mean() ))

    b = y_values.mean() - m * x_values.mean()
    return m, b 

m,b = best_fit_line(x_values, y_values)
print(f"regression line: y = {m}x + {b}") 

x_prediction = 15
y_prediction = (m * x_prediction) + b
print(y_prediction)

regression_line = [(m*x) + b for x in x_values] 
print(regression_line)

import matplotlib.pyplot as plt
plt.scatter(x_values, y_values, color="#467ddd", label="data")
plt.scatter(x_prediction, y_prediction, color="#dd4646", label="prediction")
plt.plot(x_values, regression_line, color="000000", label="regression line")
plt.title("Pavi's expense plot")
plt.xlabel(" Month ")
plt.ylabel("Expense in 100s")
plt.legend(loc=4)
plt.savefig("regression_graph.png")
plt.title("Pavi's expense plot")