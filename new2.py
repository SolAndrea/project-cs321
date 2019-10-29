import subprocess
import sys
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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



def get_str_rgb(colors):
	colors = colors.split(",")
	data = [0,0,0,0,0,0,0,0,0]
	ind = 0
	ctr = 0
	while ctr < 3:
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
	myFile = open('bananas.csv', 'w')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(data)
		
def get_colors(self):
	filename = "bananas_test.jpg"
	image_pil = Image.open(filename)
	palette = extract_colors(image_pil)
	""":type : colorific.palette.Palette"""
		
		
	colors = ','.join(rgb_to_hex(c.value) for c in palette.colors)
	print("colors: "+colors)
		
		
	get_str_rgb(colors)
		
	#import main
	import program
	
	self.label.text = "result: "+globalfile.resultRIPE
	if palette.bgcolor:
		print("Background: ", rgb_to_hex(palette.bgcolor.value))
			
			
class BananasCla(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(BananasCla, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 1

        self.label=Label(text="Bananas classifier")
        self.inside.add_widget(self.label)


        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        get_colors(self)

class RedApplesCla(Screen):
	pass

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
