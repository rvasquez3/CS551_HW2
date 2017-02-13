import matplotlib.pyplot as plt
import csv

array = []
with open('MNISTRawData.csv','rb') as csvfile:
	read = csv.reader(csvfile, delimiter = ',')	
	for row in read:
		for col in row:
			array.append(col)	
print len(array)

plt.plot(array)
plt.show()
