Text="Привет,ты кто?"
print(Text)
Name=input()
Text = "Так значит, ты " + Name
print(Text)
print("А как у тебя дела?")
Answer = input()
if Answer == 'хорошо':
   print('Это радует!')
elif Answer == 'плохо':
    print('Это огорчает!')
else :
    print("Не понимаю, тебя бро")

