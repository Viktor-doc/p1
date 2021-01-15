from tkinter import *
from tkinter import messagebox
import kurs_valut 


def pr_kv():
    # '''тестироване извлечения выбранных курсов валют'''
    kv1 = vubor_valuty1.get()
    kv2 = vubor_valuty2.get()
    
    if kv1 == 1 and kv2 == 1:      # doll-doll
        zz = 1
    elif kv1 == 1 and kv2 == 2:    # doll-euro
        zz = kurs_valut.kurs_dollar_euro()
    elif kv1 == 1 and kv2 == 3:    # doll-hrn
        zz = kurs_valut.kurs_doll_grn()
    elif kv1 == 2 and kv2 == 1:    # euro-doll
        zz = 1/kurs_valut.kurs_dollar_euro()
    elif kv1 == 2 and kv2 == 2:    # euro-euro
        zz = 1
    elif kv1 == 2 and kv2 == 3:    # euro-hrn
        zz = kurs_valut.kurs_euro_grn()
    elif kv1 == 3 and kv2 == 1:    # hrn-dol
        zz = 1/kurs_valut.kurs_doll_grn()
    elif kv1 == 3 and kv2 == 2:    # hrn-euro
        zz = 1/kurs_valut.kurs_euro_grn()       
    elif kv1 == 3 and kv2 == 3:    # hrn-hrn
        zz = 1

    return(zz)


def resultat_operacia():
    ''' функция производит вычесление: берет число из valuta1_entry и: по выбранной валюте из радиокнопок делит на курс из modul kurs_valut(на сегодня: только грн\доллар) и выводит данные в поле valuta2_entry'''
    x = float(valuta1_entry.get()) # подстановка валюты1 (ошибка если поле пустое)
    z = float(pr_kv())  # подстановка курса валюты
    y = x * z
    # otvet['text']= f"{y} maney {k}."
    valuta2_entry.delete(0, END)
    valuta2_entry.insert(0, f"{y} {k}.")
    
k = '$'

root = Tk()
root.title('обмен валют 1.0')
root.geometry('400x300')
 

kurs_valut_label = Label( text='тут курс валют и дата')
# предложение ввести суммму для обмена
valuta1_label = Label(text='сколько дашь: ')
valuta2_label = Label(text='столько и получишь: ')

kurs_valut_label.grid(row=0, column=0, sticky='w')
valuta1_label.grid(row=2, column=0, sticky='w')
valuta2_label.grid(row=2,column=1, sticky='w')

    
# ф выбора кураса валют
def vubrana_valuta_1():
    if vubor_valuty1.get() == 1:   # берет значение из ряда радиокнопок vubor_valuty1 = IntVar()     
        otvet['text'] = 'red'      # создает словарь в otvet = Label в виде [text=red]
    elif vubor_valuty1.get() == 2:
        otvet['text'] = 'green'
    elif vubor_valuty1.get() == 3:
        otvet['text'] = 'blue'
  

def vubrana_valuta_2():
    if vubor_valuty2.get() == 1:   # берет значение из ряда радиокнопок vubor_valuty1 = IntVar()     
        otvet['text'] = 'red1'      # создает словарь в otvet = Label в виде [text=red]
    elif vubor_valuty2.get() == 2:
        otvet['text'] = 'green1'
    elif vubor_valuty2.get() == 3:
        otvet['text'] = 'blue1'  



# кнопки выбора валют 1
vubor_valuty1 = IntVar()
vubor_valuty1.set(0)

doll1 = Radiobutton(text='doll', value=1, variable=vubor_valuty1)
doll1.grid(row=6,column=0, sticky='w')

euro1 = Radiobutton (text='euro', value=2, variable=vubor_valuty1)
euro1.grid(row=7,column=0, sticky='w')

hrn1 = Radiobutton (text='hrn', value=3, variable=vubor_valuty1)
hrn1.grid(row=8,column=0, sticky='w')


# кнопки выбора валют 2
vubor_valuty2 = IntVar()
vubor_valuty2.set(0)

doll2 = Radiobutton (text='doll', value=1, variable=vubor_valuty2)
doll2.grid(row=6,column=1, sticky='w')

euro2 = Radiobutton (text='euro', value=2, variable=vubor_valuty2)
euro2.grid(row=7,column=1, sticky='w')

hrn2 = Radiobutton (text='hrn', value=3, variable=vubor_valuty2)
hrn2.grid(row=8,column=1, sticky='w')


# вывод результата выбора радиокнопками
vybrono =Label(textvariable=vubor_valuty1)
vybrono.grid(row=9,column=0, sticky='w')

vybrono1 =Label(textvariable=vubor_valuty2)
vybrono1.grid(row=9,column=1, sticky='w')

# из vybrono и vybrono1 брать результат выбора радиокнопок.
# работать с ним как со списком.
# подставлять в функцию resultat_operacia

# тут же дописать ветвление при выборе двух валют


# ввод суммы для обмена
valuta1_entry = Entry()
valuta1_entry.grid(row=3, column=0, padx=5, pady=5)

# вывод суммы обмена
valuta2_entry = Entry()
valuta2_entry.grid(row=3, column=1, padx=5, pady=5)


# кнопка выполнения скрипта конвертации
message_button = Button(text='конвертировать', command=resultat_operacia)
message_button.grid(row=10, column=0, padx=5, pady=5,sticky='e')



# для теста
otvet = Label(text='не выбрано ничего')
otvet.grid(row=11,column=0, sticky='w')
# кнопка тестирования скрипта конвертации
test_button = Button(text='test', command=vubrana_valuta_2)
test_button.grid(row=12, column=0, padx=5, pady=5,sticky='e')



root.mainloop()