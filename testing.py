import subprocess
import sys
import os
from PIL import Image
sys.path.append("program/colorificmaster/colorific")
sys.path.append("program/colorificmaster")
sys.path.append("")
sys.path.append("program")
import globalfile
globalfile.init()
import csv
from palette import *
from config import *

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
	#print(data)
	data = [data]
	#myFile = open('bananas.csv', 'w')
	myFile = open(file, 'w')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(data)

def get_colors(image, file, program):
	globalfile.resultRIPE = ""
	#bananas_test.jpg will be the user's input file in the future. TODO: must change later
	#filename = "bananas_test.jpg"
	filename = image
	image_pil = Image.open(filename)
	palette = extract_colors(image)
	""":type : colorific.palette.Palette"""


	colors = ','.join(rgb_to_hex(c.value) for c in palette.colors)
	#print("colors: "+colors)

	#feed the extracted colors
	get_str_rgb(colors, file)
	if(program == 1):
		import programBananas
		programBananas.main()
	if(program == 2):
		import programTomatoes
		programTomatoes.main()
	if(program == 3):
		import programAvocados
		programAvocados.main()
	if(program == 4):
		import programStrawberry
		programStrawberry.main()
	#Outputs result to label on the UI

	#try:
	#	print(globalfile.resultRIPE)
	#	return globalfile.resultRIPE
	#except:
	#	print("here\n")
	#	globalfile.resultRIPE = "Try a different one."
	#	return globalfile.resultRIPE
	if (globalfile.resultRIPE == '?'):
		globalfile.resultRIPE = "CANNOT ANALIZE IMAGE"
	#if palette.bgcolor:
	#	print("Background: ", rgb_to_hex(palette.bgcolor.value))

ctr = 0
ctr2 = 0
get_colors("test_banana/1.jpg", "bananas.csv", 1)
print("\n\n--------------CLASSIFIER TESTING FOR ALL FOUR FRUITS---------------\n")
print("BANANAS:\n")
print("test 1: correct answer is: RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/2.jpg", "bananas.csv", 1)
print("test 2: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/3.jpg", "bananas.csv", 1)
print("test 3: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/4.jpg", "bananas.csv", 1)
print("test 4: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/5.jpg", "bananas.csv", 1)
print("test 5: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/6.jpg", "bananas.csv", 1)
print("test 6: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/7.jpg", "bananas.csv", 1)
print("test 7: correct answer is OVERRIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "OVERRIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/8.jpg", "bananas.csv", 1)
print("test 8: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/9.jpg", "bananas.csv", 1)
print("test 9: correct answer is OVERRIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "OVERRIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_banana/10.jpg", "bananas.csv", 1)
print("test 10: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
print("Correct answers for bananas: %i/10\n" % ctr)
print("Images not being able to be processed : %i/10\n" % ctr2)

ctr = 0
ctr2 = 0
get_colors("test_tomato/1.jpg", "Tomatoes.csv", 2)
print("TOMATOES:\n")
print("test 1: correct answer is: RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/2.jpg", "Tomatoes.csv", 2)
print("test 2: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/3.jpg", "Tomatoes.csv", 2)
print("test 3: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/4.jpg", "Tomatoes.csv", 2)
print("test 4: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/5.jpg", "Tomatoes.csv", 2)
print("test 5: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/6.jpg", "Tomatoes.csv", 2)
print("test 6: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/7.jpg", "Tomatoes.csv", 2)
print("test 7: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/8.jpg", "Tomatoes.csv", 2)
print("test 8: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/9.jpg", "Tomatoes.csv", 2)
print("test 9: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_tomato/10.jpg", "Tomatoes.csv", 2)
print("test 10: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
print("Correct answers for tomatoes: %i/10\n" % ctr)
print("Images not being able to be processed : %i/10\n" % ctr2)

ctr = 0
ctr2 = 0
get_colors("test_avocado/1.jpg", "Avocados.csv", 3)
print("AVOCADOS:\n")
print("test 1: correct answer is: NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT  RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/2.jpg", "Avocados.csv", 3)
print("test 2: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/3.jpg", "Avocados.csv", 3)
print("test 3: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT  RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/4.jpg", "Avocados.csv", 3)
print("test 4: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/5.jpg", "Avocados.csv", 3)
print("test 5: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/6.jpg", "Avocados.csv", 3)
print("test 6: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT  RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/7.jpg", "Avocados.csv", 3)
print("test 7: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/8.jpg", "Avocados.csv", 3)
print("test 8: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT  RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/9.jpg", "Avocados.csv", 3)
print("test 9: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT  RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_avocado/10.jpg", "Avocados.csv", 3)
print("test 10: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
print("Correct answers for avocados: %i/10\n" % ctr)
print("Images not being able to be processed : %i/10\n" % ctr2)

ctr = 0
ctr2 = 0
get_colors("test_strawberry/1.jpg", "Strawberrys.csv", 4)
print("STRAWBERRIES:\n")
print("test 1: correct answer is: RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/2.jpg", "Strawberrys.csv", 4)
print("test 2: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/3.jpg", "Strawberrys.csv", 4)
print("test 3: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/4.jpg", "Strawberrys.csv", 4)
print("test 4: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/5.jpg", "Strawberrys.csv", 4)
print("test 5: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/6.jpg", "Strawberrys.csv", 4)
print("test 6: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/7.jpg", "Strawberrys.csv", 4)
print("test 7: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/8.jpg", "Strawberrys.csv", 4)
print("test 8: correct answer is RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/9.jpg", "Strawberrys.csv", 4)
print("test 9: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
get_colors("test_strawberry/10.jpg", "Strawberrys.csv", 4)
print("test 10: correct answer is NOT RIPE. classifier said: %s\n" % (globalfile.resultRIPE))
if (globalfile.resultRIPE == "NOT RIPE"):
	ctr += 1
if (globalfile.resultRIPE == "CANNOT ANALIZE IMAGE"):
	ctr2 += 1
print("Correct answers for straberries: %i/10\n" % ctr)
print("Images not being able to be processed : %i/10\n" % ctr2)
	

