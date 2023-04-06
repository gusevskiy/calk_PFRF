# Эта программа расчитывает страховые взносы
# в ней фиксированные проценты
# создана для экономии времини работы на калькуляторе

from tkinter import *

root = Tk()
root.title('Умножение на %')
root.geometry('200x280+100+100')
root.resizable(False, False)  # блокирует изменение размеров окна
# root.iconbitmap('ico_calc_PFRF.ico') #если нужна иконка

numberA = Entry(root, width=17)  # Entry ввести одну строку текста
numberA.grid(column=1, row=0, columnspan=2, sticky=W)
numberB = Entry(root, width=17)  # Entry ввести одну строку текста
numberB.grid(column=1, row=4, columnspan=2, sticky=W)

Label(root, text='Число A').grid(column=0, row=0)
Label(root, text='A x 10% =').grid(column=0, row=1)
Label(root, text='A x 5% =').grid(column=0, row=2)
Label(root, text='A x 15% =').grid(column=0, row=3)
Label(root, text='Число Б').grid(column=0, row=4)
Label(root, text='Б x 22% =').grid(column=0, row=5)
Label(root, text='Б x 5.1% =').grid(column=0, row=6)
Label(root, text='Б x 2.9% =').grid(column=0, row=7)
Label(root, text='Б x 30% =').grid(column=0, row=8)
Label(root, text='Сумма А+Б').grid(column=0, row=9)
Label(root, text='(А+Б) x 0,2% =').grid(column=0, row=10)

result_10 = Label(root, text='', font=('Arial', 9, 'bold'))
result_10.grid(column=1, row=1)
result_5 = Label(root, text='', font=('Arial', 9, 'bold'))
result_5.grid(column=1, row=2)
result_15 = Label(root, text='', font=('Arial', 9, 'bold'))
result_15.grid(column=1, row=3)
result_22 = Label(root, text='', font=('Arial', 9, 'bold'))
result_22.grid(column=1, row=5)
result_51 = Label(root, text='', font=('Arial', 9, 'bold'))
result_51.grid(column=1, row=6)
result_29 = Label(root, text='', font=('Arial', 9, 'bold'))
result_29.grid(column=1, row=7)
result_30 = Label(root, text='', font=('Arial', 9, 'bold'))
result_30.grid(column=1, row=8)
result_1_2 = Label(root, text='', font=('Arial', 9, 'bold'))
result_1_2.grid(column=1, row=9)
result_02 = Label(root, text='', font=('Arial', 9, 'bold'))
result_02.grid(column=1, row=10)


def result_number_1():
    res10 = numberA.get()
    try:
        res10 = float(numberA.get().replace(',', '.'))
        res10 = round((res10 * 0.1), 2)
        result_10.config(text=f"{res10:,}".replace(',', ' '))
        res5 = float(numberA.get().replace(',', '.'))
        res5 = round((res5 * 0.05), 2)
        result_5.config(text=f"{res5:,}".replace(',', ' '))
        res15 = float(numberA.get().replace(',', '.'))
        res15 = round((res15 * 0.15), 2)
        result_15.config(text=f"{res15:,}".replace(',', ' '))
    except:
        return None


def result_number_2():
    res22 = numberB.get()
    try:
        res22 = float(numberB.get().replace(',', '.'))
        res22 = round((res22 * 0.22), 2)
        result_22.config(text=f"{res22:,}".replace(',', ' '))
        res05 = float(numberB.get().replace(',', '.'))
        res05 = round((res05 * 0.051), 2)
        result_51.config(text=f"{res05:,}".replace(',', ' '))
        res29 = float(numberB.get().replace(',', '.'))
        res29 = round((res29 * 0.029), 2)
        result_29.config(text=f"{res29:,}".replace(',', ' '))
        res30 = float(numberB.get().replace(',', '.'))
        res30 = round((res30 * 0.30), 2)
        result_30.config(text=f"{res30:,}".replace(',', ' '))
    except:
        return None


def result_number_1_2():
    num_1 = numberA.get()
    num_2 = numberB.get()
    try:
        if num_1 == '':
            result_10.config(text='')
            result_5.config(text='')
            num_2 = round((float(numberB.get().replace(',', '.'))), 2)
            res_1_2 = num_2
            result_1_2.config(text=f"{res_1_2:,}".replace(',', ' '))
            res_02 = round((num_2 * 0.002), 2)
            result_02.config(text=f"{res_02:,}".replace(',', ' '))
        elif num_2 == '':
            result_22.config(text='')
            result_51.config(text='')
            result_29.config(text='')
            num_1 = round((float(numberA.get().replace(',', '.'))), 2)
            res_1_2 = num_1
            result_1_2.config(text=f"{res_1_2:,}".replace(',', ' '))
            res_02 = res_1_2
            res_02 = round((res_02 * 0.002), 2)
            result_02.config(text=f"{res_02:,}".replace(',', ' '))
        else:
            num_1 = round((float(numberA.get().replace(',', '.'))), 2)
            num_2 = round((float(numberB.get().replace(',', '.'))), 2)
            res_1_2 = round((num_1 + num_2), 2)
            result_1_2.config(text=f"{res_1_2:,}".replace(',', ' '))
            res_02 = res_1_2
            res_02 = round((res_02 * 0.002), 2)
            result_02.config(text=f"{res_02:,}".replace(',', ' '))
    except:
        return None


def perform():
    result_number_1()
    result_number_2()
    result_number_1_2()


def performE(self):
    perform()



def delet():
    numberA.delete(0, END)
    numberB.delete(0, END)
    result_10.config(text='')
    result_5.config(text='')
    result_15.config(text='')
    result_22.config(text='')
    result_51.config(text='')
    result_29.config(text='')
    result_30.config(text='')
    result_1_2.config(text='')
    result_02.config(text='')


def deletE(self):
    delet()


root.bind('<Return>', performE)
root.bind('<Delete>', deletE)

Button(root, text='расчитать', command=perform, bg='green',
       font=('Arial', 9, 'bold'),
       height=1, width=8).grid(column=1, row=11)

Button(root, text='очистить', command=delet, bg='yellow',
       font=('Arial', 9, 'bold'),
       height=1, width=8).grid(column=0, row=11)

root.mainloop()
