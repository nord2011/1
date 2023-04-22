pers = {"имя": "?",
        "лет":"?",
        "способнасть":"?"
        }

print(pers)
comand = input("введите команду!")

while comand != "выход":
    if comand == "+":
        app = input("какой ключ добавить?")
        snac = input("знаение?")
        pers[app] = snac        
    elif comand == "замена":
        Key = input("что заменить?")
        isExist = False
        for key in pers:
            if key == Key:
                isExist = True  
                break
    
        if isExist == True:
            cnac = input("на что заменить")
            pers[key] = cnac
        else:
            print("нет такого ключа!")
    elif comand == "вывод":
        print(pers)
    elif comand == "-":
            dell = input("что удалить?")
            del pers[dell]
    comand = input("введите команду!")pers = {"имя": "?",
        "лет":"?",
        "способнасть":"?"
        }

print(pers)
comand = input("введите команду!")

while comand != "выход":
    if comand == "+":
        app = input("какой ключ добавить?")
        snac = input("знаение?")
        pers[app] = snac        
    elif comand == "замена":
        Key = input("что заменить?")
        isExist = False
        for key in pers:
            if key == Key:
                isExist = True  
                break
    
        if isExist == True:
            cnac = input("на что заменить")
            pers[key] = cnac
        else:
            print("нет такого ключа!")
    elif comand == "вывод":
        print(pers)
    elif comand == "-":
            dell = input("что удалить?")
            del pers[dell]
    comand = input("введите команду!")
