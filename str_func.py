from turtle import title

#Функция
def dunc(user_input):
    #Ввод строки пользователем
    user_input = input()
    #Вывод строки заглавными буквами
    return print(user_input.upper())


#Функция 2
def func_2(alf):
    #Ввод строки пользователем
    alf = input()
    #Вывод строки, где каждое слово будет с заглавной буквы
    return print(title(alf))
