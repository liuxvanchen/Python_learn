from math import sqrt


def mean(x):
    sum = 0.0
    for value in x:
        sum += value
    return sum/len(x)


def stddev(x, mean):
    sum = 0.0
    for value in x:
        sum += (value - mean) ** 2
    return sqrt(sum / len(x))


def covariance(x, y, mean_x, mean_y):
    cov = 0.0
    for i in range(len(x)):
        cov += (x[i] - mean_x) * (y[i] - mean_y)
    return cov / len(x)


def correlation(x, y):
    if (len(x) != len(y)):
        print("Error!")
    mean_x = mean(x)
    mean_y = mean(y)
    stddev_x = stddev(x, mean_x)
    stddev_y = stddev(y, mean_y)
    cov = covariance(x, y, mean_x, mean_y)
    return cov / (stddev_x * stddev_y)


x = []
y = []
with open('D:\\C++\\C++HOMEWORK\\Monthly_Temperature_and_LAI_Columns.txt', 'r') as file:
    next(file)
    for line in file:
        parts = line.split()
        if len(parts) >= 2:
            x.append(float(parts[0]))
            y.append(float(parts[1]))
# print(x)
# print(y)

print(correlation(x, y))
