#Импорт нужных модулей
import json  # Модуль json для интегрирования json-файла в программу
from browser import *  # Модуль browser для взаимодействия с html

#Открытие файла json со всеми уровнями
file = open('levels.json', 'r')
config = json.load(file)

#Выбор и присваивание в переменные всех нужных элементов сайта для работы с ними
lvlCounter = 0
totalLvl = len(config)
totalText = document.select('.total')[0]
nextBtn = document.select('.next-btn')[0]
levels = document.select('.level')
currentLvl = document.select('.current')[0]
totalNumsOfLvls = document.select('.total')[0]
leftArrow = document.select('.left-arrow')[0]
rightArrow = document.select('.right-arrow')[0]
hintCode = document.select('.hint')[0]
hintAlert = document.select('.hint')[1]
theorytext = document.select('.exercise p')[1]
exercise = document.select('.exercise b')[0]
caption = document.select('.caption')[0]
example = document["example"]
changingText = document["text"]
code = document["code"]

#начальные данные
totalText.text = totalLvl
hintCode.src = config[0]['hintCode']
hintAlert.src = config[0]['hintAlert']
theorytext.text = config[0]['theorytext']
exercise.text = config[0]['exercise']
caption.text = config[0]['caption']
example.text = config[0]['example']
example.style.cssText = config[0]['exampleStyle']
changingText.text = config[0]['changingText']
changingText.style.cssText = config[0]['changingTextStyle']

#Основные действия программы

#Метод для смены уровня назад
def lvlBack(event):
	global currentLvl
	global lvlCounter
	if(lvlCounter == 0):
		pass
	else:
		lvlCounter -= 1
		currentLvl.text = lvlCounter+1
		lvlGen()

#Метод для смены уровня вперед
def lvlAhead(event):
	global currentLvl
	global lvlCounter
	global totalLvl
	if(lvlCounter == totalLvl-1):

		pass
	else:
		lvlCounter += 1
		currentLvl.text = lvlCounter+1
		lvlGen()

#метод для генерации уровня
def lvlGen():
	global lvlCounter
	global hintAlert
	global hintCode
	global theorytext
	global caption
	global example
	global changingText
	global config

	hintCode.src = config[lvlCounter]['hintCode']
	hintAlert.src = config[lvlCounter]['hintAlert']
	theorytext.text = config[lvlCounter]['theorytext']
	exercise.text = config[lvlCounter]['exercise']
	caption.text = config[lvlCounter]['caption']
	example.text = config[lvlCounter]['example']
	example.style.cssText = config[lvlCounter]['exampleStyle']
	changingText.text = config[lvlCounter]['changingText']
	changingText.style.cssText = config[lvlCounter]['changingTextStyle']
	code.style.cssText = config[lvlCounter]['codeStyle']

leftArrow.bind('click', lvlBack)
rightArrow.bind('click', lvlAhead)
nextBtn.bind('click', lvlAhead)