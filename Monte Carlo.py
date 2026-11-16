import random
import matplotlib.pyplot as plt

random.seed(10)
N = 1000
accepted_x, accepted_y = [], []
rejected_x, rejected_y = [], []

for _ in range(N):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if y <= x ** 2:
        accepted_x.append(x)
        accepted_y.append(y)
    else:
        rejected_x.append(x)
        rejected_y.append(y)

area = (len(accepted_x) / N) * 1
print("Estimated area:", area)
print("Exact area:    ", 1 / 3)

x_curve = [i / 100 for i in range(101)]
y_curve = [x ** 2 for x in x_curve]

plt.scatter(rejected_x, rejected_y, color="red",
            s=12, label="Rejected")
plt.scatter(accepted_x, accepted_y, color="green",
            s=12, label="Accepted")
plt.plot(x_curve, y_curve, color="blue",
         label="f(x) = x^2")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Area Estimation")
plt.legend()
plt.grid()
plt.show()