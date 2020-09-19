import csv
import matplotlib.pyplot as plt
import numpy as np

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

file = "IL_employee_salary.csv"
keys = ["Name", "Position", "Annual Salary"]

salary_array = []
with open(file, "r", newline="\n") as f:
    csv_reader = csv.DictReader(f)

    for i in csv_reader:
        salary_array.append(int(i[keys[2]].strip()[1:].replace(",","")))

# Creating the buckets for the salaries
buckets = {}
for i in range(50000, 100000, 10000):
    buckets[i] = 0
for i in salary_array:
    if i >= 50000 and i < 60000:
        buckets[50000] += 1
    elif i >= 60000 and i < 70000:
        buckets[60000] += 1
    elif i >= 70000 and i < 80000:
        buckets[70000] += 1
    elif i >= 80000 and i < 90000:
        buckets[80000] += 1
    else:
        buckets[90000] += 1

n = list(buckets.values())
bins = list(buckets.keys())

# Creating the e-differential dataset
hist1 = []
hist2 = []
hist3 = []
for i in n:
    hist1.append(max(0, int(i + np.random.laplace(0., 1/0.05, 1))))
    hist2.append(max(0, int(i + np.random.laplace(0., 1/0.1, 1))))
    hist3.append(max(0, int(i + np.random.laplace(0., 1/5, 1))))


# plotting the baseline dataset
labels = bins
fig, ax = plt.subplots()
x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars
rects4 = ax.bar(x, n, width/2, label='Original Employee Numbers')
ax.set_ylabel('Number of Employees')
ax.set_title('Employee Salary Range')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects4)
fig.tight_layout()


#Plotting the e-differential histograms with the baseline reference
fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.75*width, hist1, width/2, label='e=0.05')
rects2 = ax.bar(x - 0.25*width, hist2, width/2, label='e=0.1')
rects3 = ax.bar(x + 0.25*width, hist3, width/2, label='e=5.0')
rects4 = ax.bar(x + 0.75*width, n, width/2, label='Original Employee Numbers')

ax.set_ylabel('Number of Employees')
ax.set_title('E-differentially Private Employee Salary Range')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
fig.tight_layout()

#Dsiplay both plots
plt.show()

