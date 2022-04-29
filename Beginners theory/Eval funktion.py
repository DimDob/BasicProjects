res=input("Въведете стойността на израза: ") #В инпут-а се въвежда текст, съответно в променлива res се запазва текстова стойност
print("стойността на израза е: ", eval(res))

txt="1+2+3" #Променливата txt е зададена като текст (string). Eval() интерпретира всякакъв тип данни.
print(txt, "=", eval(txt))
res=input("Please insert the required equation: ")
print("The result of the equation looks like this: ", eval(res))

nums="5*5"
print(" Value of 5*5", "=", eval(nums))
