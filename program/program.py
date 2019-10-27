import Node
import kivy
from kivy.app import App
from kivy.uix.label import Label
import globalfile


data = [[]]
f = open('bananas.csv')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'color1R': {'3': 'NOT RIPE', '2': 'NOT RIPE', '5': {'color1B': {'5': {'color1G': {'3': {'color2R': {'3': 'RIPE', '4': {'color2B': {'3': 'OVERRIPE', '4': 'RIPE'}}}}, '2': {'color2R': {'5': 'RIPE', '4': {'color2B': {'3': 'RIPE', '4': 'NOT RIPE'}}}}}}, '4': 'RIPE'}}, '4': 'OVERRIPE'}}
attributes = ['color1R', 'color1B', 'color1G', 'color2R', 'color2B', 'color2G', 'color3R', 'color3B', 'color3G', 'class']
count = 0
for entry in data:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
		tempDict = tempDict[tempDict.keys()[0]]
		index = attributes.index(root.value)
		value = entry[index]
		if(value in tempDict.keys()):
			child = Node.Node(value, tempDict[value])
			globalfile.resultRIPE = tempDict[value]
			tempDict = tempDict[value]
		else:
			print "can't process input %s" % count
			result = "?"
			break
	print ("entry%s = %s" % (count, globalfile.resultRIPE))
	