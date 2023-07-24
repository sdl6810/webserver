import random
import openpyxl as xl

activeList = []
queueList = []

for i in range(0,100):
	activeList.append(random.randint(0,500))

j = len(activeList)
while j > 0:
		pickAnElement = random.randint(0,len(activeList)-1)
		#print(activeList[pickAnElement])
		print(j,len(activeList),len(queueList))
		queueList.append(activeList[pickAnElement])
		activeList.remove(activeList[pickAnElement])
		j = j - 1

print(activeList)
print(queueList)