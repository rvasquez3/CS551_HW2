import matplotlib.pyplot as plt
import csv

#create array to append data column values as single integers
array = []
#load csv data and extract row, col values 
with open('MNISTRawData.csv','rb') as csvfile:
	read = csv.reader(csvfile, delimiter = ',')	
	for row in read:
		for col in row:
			array.append(col)	
print len(array)

#plot data
plt.plot(array)
plt.show()
