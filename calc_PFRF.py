# Эта программа расчитывает страховые взносы
# в ней фиксированные проценты
# создана для экономии времини работы на калькуляторе

from tkinter import *

root = Tk()
root.title('Умножение на %')
root.geometry('200x220+100+100')
root.resizable(False, False)  # блокирует изменение размеров окна
# root.iconbitmap('ico_calc_PFRF.ico') #если нужна иконка

number_1 = Entry(root, width=12)  # Entry ввести одну строку текста
number_1.grid(column=1, row=0, columnspan=2, sticky=W)
number_2 = Entry(root, width=12)  # Entry ввести одну строку текста
number_2.grid(column=1, row=3, columnspan=2, sticky=W)

Label(root, text='Введи число A').grid(column=0, row=0)
Label(root, text='A x 10 % =').grid(column=0, row=1)
Label(root, text='A x 5 % =').grid(column=0, row=2)
Label(root, text='Введи число Б').grid(column=0, row=3)
Label(root, text='Б x 22 % =').grid(column=0, row=4)
Label(root, text='Б x 5.1 % =').grid(column=0, row=5)
Label(root, text='Б x 2.9 % =').grid(column=0, row=6)
Label(root, text='Сумма А + Б').grid(column=0, row=7)
Label(root, text='(А+Б) x 0,2 % =').grid(column=0, row=8)

result_10 = Label(root, text=[], font=('Arial', 9, 'bold'))
result_10.grid(column=1, row=1)
result_5 = Label(root, text=[], font=('Arial', 9, 'bold'))
result_5.grid(column=1, row=2)
result_22 = Label(root, text=[], font=('Arial', 9, 'bold'))
result_22.grid(column=1, row=4)
result_51 = Label(root, text=[], font=('Arial', 9, 'bold'))
result_51.grid(column=1, row=5)
result_29 = Label(root, text=[], font=('Arial', 9, 'bold'))
result_29.grid(column=1, row=6)
result_1_2 = Label(root, text=[], font=('Arial', 9, 'bold'))
result_1_2.grid(column=1, row=7)
result_02 = Label(root, text=[], font=('Arial', 9, 'bold'))
result_02.grid(column=1, row=8)


def result_number_1():
    res10 = number_1.get()
    try:
        res10 = float(number_1.get().replace(',', '.'))
        res10 = round((res10 * 0.1), 2)
        result_10.config(text=(f"{res10:,}"))
        res5 = float(number_1.get().replace(',', '.'))
        res5 = round((res5 * 0.05), 2)
        result_5.config(text=(f"{res5:,}"))
    except:
        return None


def result_number_2():
    res22 = number_2.get()
    try:
        res22 = float(number_2.get().replace(',', '.'))
        res22 = round((res22 * 0.22), 2)
        result_22.config(text=(f"{res22:,}"))
        res05 = float(number_2.get().replace(',', '.'))
        res05 = round((res05 * 0.051), 2)
        result_51.config(text=(f"{res05:,}"))
        res29 = float(number_2.get().replace(',', '.'))
        res29 = round((res29 * 0.029), 2)
        result_29.config(text=(f"{res29:,}"))
    except:
        return None


def result_number_1_2():
    num_1 = number_1.get()
    num_2 = number_2.get()
    try:
        if num_1 == '':
            num_2 = round((float(number_2.get().replace(',', '.'))), 2)
            res_1_2 = num_2
            result_1_2.config(text=(f"{res_1_2:,}"))
            res_02 = res_1_2
            res_02 = round((res_02 * 0.02), 2)
            result_02.config(text=(f"{res_02:,}"))
        elif num_2 == '':
            num_1 = round((float(number_1.get().replace(',', '.'))), 2)
            res_1_2 = num_1
            result_1_2.config(text=(f"{res_1_2:,}"))
            res_02 = res_1_2
            res_02 = round((res_02 * 0.02), 2)
            result_02.config(text=(f"{res_02:,}"))
        else:
            num_1 = round((float(number_1.get().replace(',', '.'))), 2)
            num_2 = round((float(number_2.get().replace(',', '.'))), 2)
            res_1_2 = num_1 + num_2
            result_1_2.config(text=(f"{res_1_2:,}"))
            res_02 = res_1_2
            res_02 = round((res_02 * 0.02), 2)
            result_02.config(text=(f"{res_02:,}"))
    except:
        return None


def perform():
    result_number_1()
    result_number_2()
    result_number_1_2()


def performE(self):
    perform()


def delet():
    number_1.delete(0, END)
    number_2.delete(0, END)
    result_10.config(text=[])
    result_5.config(text=[])
    result_22.config(text=[])
    result_51.config(text=[])
    result_10.config(text=[])
    result_29.config(text=[])
    result_1_2.config(text=[])
    result_02.config(text=[])


def deletE(self):
    delet()


root.bind('<Return>', performE)
root.bind('<Delete>', deletE)

button1 = Button(root, text='learn', command=perform,
                 font=('Arial', 9, 'bold'),
                 height=1, width=5).grid(column=1, row=9)

button2 = Button(root, text='del', command=delet,
                 font=('Arial', 9, 'bold'),
                 height=1, width=5).grid(column=2, row=9)

root.mainloop()
