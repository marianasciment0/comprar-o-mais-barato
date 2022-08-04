produto1= float(input("digite o preço do produto: "))
produto2= float(input("digite o preço do produto: "))
produto3= float(input("digite o preço do produto: "))

if produto1>produto2 and produto1>produto3:
      print("o primeiro produto é o mais caro")
else:
      if produto2>produto3 and produto2>produto1:
            print("o segundo produto é o mais caro")
      else:
            if produto3>produto1 and produto3>produto2:
                  print("o terceiro produto é o mais caro")

if produto1<produto2 and produto1<produto3:
      print("o primeiro produto é o mais barato, compre esse")
else:
      if produto2<produto3 and produto2<produto1:
            print("o segundo produto é o mais barato, compre esse")
      else:
            if produto3<produto1 and produto3<produto2:
                  print("o terceiro produto é o mais barato, compre esse")
