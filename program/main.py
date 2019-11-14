import DecisionTree

def main():
    #Insert input file
    """
    IMPORTANT: Change this file path to change training data 
    """
    #file = open('BananasTraining.csv')
    #file = open('TomatoesTraining.csv')
    #file = open('AvocadosTraining.csv')
    file = open('StrawberryTraining.csv')
	
    """
    IMPORTANT: Change this variable too change target attribute 
    """
    target = "class"
    data = [[]]
    for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))
    data.remove([])
    attributes = data[0]
    data.remove(attributes)
    #Run ID3
    tree = DecisionTree.makeTree(data, attributes, target, 0)
    print( "generated decision tree")
    #Generate program
	
    #file = open('programBananas.py', 'w')
    #file = open('programTomatoes.py', 'w')
    #file = open('programAvocados.py', 'w')
    file = open('programStrawberry.py', 'w')
	
    file.write("import Node\n")
    file.write("import kivy\n")
    file.write("from kivy.app import App\n")
    file.write("from kivy.uix.label import Label\n")
    file.write("import globalfile\n\n")
	
    file.write("def main():\n")
    #open input file
    file.write("\tdata = [[]]\n")
    """
    IMPORTANT: Change this file path to change testing data 
    """
	
    #file.write("\tf = open('bananas.csv')\n")
    #file.write("\tf = open('Tomatoes.csv')\n")
    #file.write("\tf = open('Avocados.csv')\n")
    file.write("\tf = open('Strawberrys.csv')\n")
	
    #gather data
    file.write("\tfor line in f:\n\t\tline = line.strip(\"\\r\\n\")\n\t\tdata.append(line.split(','))\n")
    file.write("\tdata.remove([])\n")
    #input dictionary tree
    file.write("\ttree = %s\n" % str(tree))
    file.write("\tattributes = %s\n" % str(attributes))
    file.write("\tcount = 0\n")
    file.write("\tfor entry in data:\n")
    file.write("\t\tcount += 1\n")
    #copy dictionary
    file.write("\t\ttempDict = tree.copy()\n")
    file.write("\t\tresult = \"\"\n")
    #generate actual tree
    file.write("\t\twhile(isinstance(tempDict, dict)):\n")
    file.write("\t\t\troot = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])\n")
    file.write("\t\t\ttempDict = tempDict[tempDict.keys()[0]]\n")
    #this must be attribute
    file.write("\t\t\tindex = attributes.index(root.value)\n")
    file.write("\t\t\tvalue = entry[index]\n")
    #ensure that key exists
    file.write("\t\t\tif(value in tempDict.keys()):\n")
    file.write("\t\t\t\tchild = Node.Node(value, tempDict[value])\n")
    file.write("\t\t\t\tglobalfile.resultRIPE = tempDict[value]\n")
    file.write("\t\t\t\ttempDict = tempDict[value]\n")
    #otherwise, break
    file.write("\t\t\telse:\n")
    file.write("\t\t\t\tprint( \"can't process input %s\" % (count))\n")
    file.write("\t\t\t\tresult = \"?\"\n")
    file.write("\t\t\t\tbreak\n")
    #print solutions 
    file.write("\t\tprint (\"entry%s = %s\" % (count, globalfile.resultRIPE))\n")
    print("written program")
    
    
if __name__ == '__main__':
    main()
