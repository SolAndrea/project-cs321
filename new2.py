import subprocess
import sys
import tkinter as tk
import tkinter.filedialog as tkFileDialog
import os
from PIL import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
sys.path.append("program/colorificmaster/colorific")
sys.path.append("program/colorificmaster")
sys.path.append("")
sys.path.append("program")

import csv
from palette import *
from config import *
import kivy
from kivy.app import App
from kivy.uix.label import Label
import globalfile
globalfile.init()
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty

root = tk.Tk()
root.withdraw()

def open_file():
	root.filename = tkFileDialog.askopenfilename(initialdir = os.getcwd(), title="Select file", filetypes = (("jpeg files", "*.jpg"), ("png files", "*.png"), ("All files", "*")))
	return root.filename

#uses the extracted colors from the picture to write the color data points to a file
def get_str_rgb(colors, file):
	colors = colors.split(",")
	data = [0,0,0,0,0,0,0,0,0]
	ind = 0
	ctr = 0
	while (ctr < 3 and ctr < len(colors)):
		hexcolor = colors[ctr].lstrip('#')
		rgbcolor = tuple(int(hexcolor[i:i+2], 16) for i in (0, 2, 4))
		ctr2 = 0
		while ctr2 < 3:
			i = rgbcolor[ctr2]
			num = 0
			if (i<=51):
				num = 1
			elif (i>51 and i<=102):
				num = 2
			elif (i>102 and i<=153):
				num = 3
			elif (i>153 and i<=204):
				num = 4
			elif (i>204 and i<=255):
				num = 5
			data[ind] = num
			ind = ind + 1
			ctr2 = ctr2 + 1
		ctr = ctr + 1
	print(data)
	data = [data]
	#myFile = open('bananas.csv', 'w')
	myFile = open(file, 'w')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(data)

def get_colors(self, image, file, program):
	#bananas_test.jpg will be the user's input file in the future. TODO: must change later
	#filename = "bananas_test.jpg"
	filename = image
	image_pil = Image.open(filename)
	palette = extract_colors(image_pil)
	""":type : colorific.palette.Palette"""


	colors = ','.join(rgb_to_hex(c.value) for c in palette.colors)
	print("colors: "+colors)

	#feed the extracted colors
	get_str_rgb(colors, file)

	#import main
	#main.main()

	if(program == 1):
		import programBananas
		programBananas.main()
	if(program == 2):
		import programTomatoes
		programTomatoes.main()
	if(program == 3):
		import programAvocados
		programAvocados.main()

	#Outputs result to label on the UI
	self.outputText = "result: "+ globalfile.resultRIPE


	if palette.bgcolor:
		print("Background: ", rgb_to_hex(palette.bgcolor.value))





class BananasCla(GridLayout, Screen):
    outputText = StringProperty()

    def __init__(self, **kwargs):
        super(BananasCla, self).__init__(**kwargs)
        self.outputText = "result: No Result"


	#start the whole process
    def pressed(self, instance):
        file = open_file()
		#old input parameter: "bananas_test.jpg"
        try:
            result = get_colors(self, file, 'bananas.csv', 1)
        except AttributeError:
            self.outputText = "result: No Result"
            self.manager.current = "main"

        for key, val in self.ids.items():
            if (val == 'innerBoxLayout'):
                self.outputText = str(result)



class TomatoesCla(GridLayout, Screen):
    outputText = StringProperty()

    def __init__(self, **kwargs):
        super(TomatoesCla, self).__init__(**kwargs)
        self.outputText = "result: No Result"

	#start the whole process
    def pressed(self, instance):
        result = get_colors(self, "tomatoes_test.jpg", 'Tomatoes.csv', 2)
        for key, val in self.ids.items():
            if (val == 'innerBoxLayout'):
                self.outputText = str(result)

class AvocadosCla(GridLayout, Screen):
    outputText = StringProperty()
    def __init__(self, **kwargs):
        super(AvocadosCla, self).__init__(**kwargs)
        self.outputText = "result: No Result"

	#start the whole process
    def pressed(self, instance):
        result = get_colors(self, "avocados_test.jpg", 'Avocados.csv', 3)
        for key, val in self.ids.items():
            if (val == 'innerBoxLayout'):
                self.outputText = str(result)


class MainScreen(Screen):
	pass

class Guide(Screen):
	pass

class Classifier(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

presentation = Builder.load_file("main.kv")


class MyApp(App):
	def build(self):
		return presentation




if __name__ == "__main__":
	MyApp().run()
