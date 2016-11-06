import csv

def category_link(filename, n):
	csvData = []
	with open(filename, 'rb') as csvfile:
		data = csv.reader(csvfile)
		for row in data:
			if(n > 0):
				row = ','.join(row).strip(' ')
				csvData.append(row)
				n -= 1
			else:
				break
	return csvData

def tags(filename):
	tagsData = []
	with open(filename, 'r') as csvfile:
		data = csv.reader(csvfile)
		for row in data:
			row = ','.join(row).strip(' ')
			tagsData.append(row)
	return tagsData
