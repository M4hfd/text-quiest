username = input("Какого твое имя, странник? ")
print("Приветствую " + username + "!"+
    """ Предлагаю тебе пройти наш квест! Правила просты! 
    За 1 задание ты получишь 10 очков!
    За 2 задание ты получишь 20 очков!
    За 3 задание ты получишь 30 очков!
    Игру ты начинаешь с 0 очков!""")
score = 0
artifact_one = False
artifact_two = False
artifact_three = False
#1 вопрос
print("Итак начнем! Первый вопрос! Сколько будет 2+2?")
answer_one = input("Ответ: ")
if answer_one == "4":
        print("""Не знаю сосчитал ты или угадал, но ты прав! 
        +10 очков, + артефакт математика!""")
        score +=10
        artifact_one = True
        print("Твой счет:", + score)
else:
        print("Ты не прав! Поэтому за первый вопрос ты получаешь 0 очков!")
#2 вопрос
print("Второй вопрос! Сколько глаз у лисы?")
answer_two = input("Ответ: ")
if answer_two == "2":
        print("""Молодец! 
        +20 очков, + артефакт биолога!""")
        score +=20
        artifact_two = True
        print("Твой счет:", + score)
else:
        print("Ты не прав! Поэтому за второй вопрос ты получаешь 0 очков!")
#3 вопрос
print("Финальный вопрос! Сколько углов у треугольника?")
answer_three = input("Ответ: ")
if answer_three == "3":
        print("""Вау! Ты просто гений! 
        +30 очков, + артефакт геометрика!""")
        score +=30
        artifact_three = True
        print("Твой счет:", + score)
else:
        print("Ты не прав! Поэтому за третий вопрос ты получаешь 0 очков!")
print("""Ты почти у цели!
Можешь купить себе что нибудь в магазине!
1: Банка Колы - 15 points
2: Чипсы Сырколбас - 30 points
3: Фонарик с Лунтиком - 60 points
4: Не брать ничего""")
shop_choise = int(input("Твой выбор: "))
#Выборы в магазине
if shop_choise == 1:
    if score >=15:
       score -=15
       print("Ты выпил Колу и освежился! Четко!")
    else:
       print("Ты не смог позволить себе колу! Все так плохо?")
if shop_choise == 2:
    if score >=15:
         score +=10
         print("Ты открыл пачку и нашел там счастливую фишку! +10 поинтов")
    else:
         print("Тебе не хватило поинтов! Грустненько!")
if shop_choise == 3:
  if score >=60:
        score -=60
        print("""Фонарик конечно оказался прикольным, но кажется он того не стоил.""")
  else:
        print("Тебе не хватает поинтов! Может это знак не покупать хлам?")
if shop_choise == 4:
        print("""<Экономия - залог успеха> - Подумали вы и отказались от покупок""")
#Концовка
if artifact_one and artifact_two and artifact_three == True:
        print("Поздравляю с победой! Твой счет: " + str(score))
elif artifact_one and artifact_two == True:
        print("Молодец! Но с геометрией у тебя проблемы! Ты не нашел 3 артефакт! Счет: " + str(score))
elif artifact_three and artifact_two == True:
        print("Молодец! Но с математикой у тебя проблемы! Ты не нашел 1 артефакт! Счет: " + str(score))
elif artifact_three and artifact_one == True:
        print("Молодец! Но с биологией у тебя все плохо! Ты не нашел 2 артефакт! Счет: " + str(score))
elif artifact_three or artifact_two or artifact_one == True:
        print("Ты нашел только 1 артефакт! Не очень как то!")
else:
        print("Ты проиграл! Не нашел ни одного артефакта!")
