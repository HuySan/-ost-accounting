from tkinter import*
from tkinter import messagebox
import datetime#Для работы со временем
from datetime import datetime
import pickle#Для сеарелизации и десеарилезации данных

my_window = Tk()
my_window.title('Журнал расходов')
my_window.geometry("500x350")

#Время сейчас
now = datetime.now()
month = now.month
day = now.day
def Date(bly):

	#Открываем файл и вставляем эти данные
	f = open('dateRate.txt',"a")#для дозаписи
	f.write(str(bly) + "=" + str(ent.get()) + ".00" + "=")#шифровать с помощью сериализации пока не будем
	f.close()
#----------------------------------------------------------------------
#Считываем строка за строкой и работаем с методом str_.splint(":")
f = open("dateRate.txt","r")
#Читаем строка за строкой
for line in f:
	result = line.split("=")
	result.pop()#удаляем последний элемент,т.к. туда проскакивала строка
print ()
f.close()

#расходы
x = 1
#дни
d = 0
#global sums
sums = 0
#Так мы перебераем только суммы расходов и выводим всю сумму
vaultWeek = 0
vaultMonth = 0
vaultDay = 0
allTime = 0
for i in range(int(len(result)/2)):
	#print (result[x])
	#x+=2
	days = result[d]

#Мы берём и отнимаем этот день с сегоднешним днём и если различается на один,значит переносим в следующие колонки и т.д. и т.п.
#Т.е сегодняшний день полюбому не меньши дня,когда создан расход,поэтому мы отнимаем его от days
	if int(day) - int(days) >= 0 and int(day) - int(days) < 8:
		vaultWeek+=float(result[x])
	if int(day) - int(days) > 0 and int(day) - int(days) < 31 or int(day) - int(days) < 32:
		vaultMonth+=float(result[x])
	if int(day) - int(days) == 0:
		vaultDay+=float(result[x])
	if int(day) - int(days) > -1:
		allTime+=float(result[x])
	d+=2
	x+=2

f.close()


lab1 = Label(my_window,text = "CЕГОДНЯ",fg = "green")
labMain1 = Label(my_window,text=vaultDay)#Тут текст будет равен тому значению,которое мы введём в следующем окне и будет суммироваться
lab1.grid(row = 0,column=0)
labMain1.grid(row=1,column=4)

lab1 = Label(my_window,text = "НЕДЕЛЯ",fg = "green")
labMain1 = Label(my_window,text=vaultWeek)#Тут текст будет равен тому значению,которое мы введём в следующем окне и будет суммироваться
lab1.grid(row = 2,column=0)
labMain1.grid(row=3,column=4)

lab1 = Label(my_window,text = "МЕСЯЦ",fg = "green")
labMain1 = Label(my_window,text=vaultMonth)#Тут текст будет равен тому значению,которое мы введём в следующем окне и будет суммироваться
lab1.grid(row = 4,column=0)
labMain1.grid(row=5,column=4)

butStart = Button(my_window,text = "Ещё расходы +",command = lambda:epta())
butStart.grid(row=6,column=10)

labAllTime = Label(my_window,text="За всё время:",fg = "red")
labAllTimeMain = Label(my_window,text=allTime,fg = "gray")
labAllTime.grid(row=7,column=10)
labAllTimeMain.grid(row=8,column=10)
#После нажатия на кнопку вызываем функцию,создающая окно с вводом данных расходов и комментарий,пока без категорий
def epta():
	my_window2 = Tk()
	my_window2.title("Ввод данных")
	my_window2.geometry("400x250")

	lab = Label(my_window2,text = "Расход составляет:",fg = "#E78055")
	lab.pack()

	global ent
	ent = Entry(my_window2,width=15)
	ent.pack()
#Отлично
	#labTwo = Label(my_window2,text = "Комментарий для пояснения:")

	#labTwo.pack()
	#ent2 = Entry(my_window2,width = 30)
	#ent2.pack()
	
	but = Button(my_window2,text="Погнали",command = lambda:Date(day))
	but.pack()


	my_window2.mainloop()

def update():
	my_window.update()


my_window.mainloop()

