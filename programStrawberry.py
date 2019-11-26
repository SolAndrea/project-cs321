import Node
import kivy
from kivy.app import App
from kivy.uix.label import Label
import globalfile

def main():
	data = [[]]
	f = open('Strawberrys.csv')
	for line in f:
		line = line.strip("\r\n")
		data.append(line.split(','))
	data.remove([])
	tree = {'color1R': {'1': 'RIPE', '3': 'RIPE', '2': 'NOT RIPE', '5': {'color1B': {'1': 'RIPE', '5': 'NOT RIPE'}}, '4': {'color1B': {'1': 'RIPE', '3': 'NOT RIPE', '4': {'color1G': {'1': 'NOT RIPE', '3': {'color2R': {'1': 'NOT RIPE', '4': 'RIPE'}}, '4': 'NOT RIPE'}}}}}}
	attributes = ['color1R', 'color1B', 'color1G', 'color2R', 'color2B', 'color2G', 'color3R', 'color3B', 'color3G', 'class']
	count = 0
	for entry in data:
		count += 1
		tempDict = tree.copy()
		result = ""
		while(isinstance(tempDict, dict)):
			root = Node.Node(list(tempDict.keys())[0], tempDict[list(tempDict.keys())[0]])
			tempDict = tempDict[list(tempDict.keys())[0]]
			index = attributes.index(root.value)
			value = entry[index]
			if(value in tempDict.keys()):
				child = Node.Node(value, tempDict[value])
				globalfile.resultRIPE = tempDict[value]
				tempDict = tempDict[value]
			else:
				#print( "can't process input %s" % (count))
				globalfile.resultRIPE = "?"
				break
		#print ("entry%s = %s" % (count, globalfile.resultRIPE))
