import numpy as np
from collections import Counter

train_dataset = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
test_dataset = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

def load_data_into_datasets():
	raw_data = open('train.txt', 'r').readlines()
	temp = []
	for line in raw_data:
		if len(line) != 3:
			temp.append([int(x) for x in line[:-1]])
		else:
			train_dataset[int(line)].append(temp)
			temp = []
	
	raw_data = open('testAll.txt', 'r').readlines()
	temp = []
	for line in raw_data:
		if len(line) != 3:
			temp.append([int(x) for x in line[:-1]])
		else:
			test_dataset[int(line)].append(temp)
			temp = []

def k_nearest_neighbours(train_data, test_data, k=5):
	distances = []
	for group in train_data:
		for pt in train_data[group]:
			temp_distance = 0
			for i in range(len(pt)):
				temp_distance += np.linalg.norm(np.array(pt[i]) - np.array(test_data[i]))
			distances.append([temp_distance, group])

	votes = [i[1] for i in sorted(distances)[:k]]
	ans = Counter(votes).most_common(1)
	return ans

#To check every instance of every digit, takes time!!
def funcAll():
	correct = incorrect = 0
	load_data_into_datasets()
	for group in test_dataset:
		for pt in test_dataset[group]:
			output= k_nearest_neighbours(train_dataset, pt, k = 5)
			if output[0][0] is group:
				correct += 1
			else:
				incorrect += 1
	accuracy = (correct/(correct+incorrect))*100
	print(accuracy, '\n', 'Total Cases Tried:', correct+incorrect)

#To check only one instance of each digit
def funcTests(k):
	load_data_into_datasets()
	print('Test-Case', 'Output', 'Confidence')
	for i in range(10):
		test_case = []
		file_name = 'testCheck' + str(i) + '.txt'
		raw_data = open(file_name, 'r').readlines()
		for line in raw_data:
			test_case.append([int(x) for x in line[:-1]])
		answer = k_nearest_neighbours(train_dataset, test_case,k)
		print(i, '\t ', answer[0][0], '\t', (answer[0][1]/k)*100)
				
funcTests(5)
#need more computational power to run funcAll() quickly:/
#funcAll()

		
		
	



 


		

