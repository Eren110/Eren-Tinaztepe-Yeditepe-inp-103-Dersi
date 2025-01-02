sayi1 = int(input("sayi1"))
sayi2 = int(input("sayi2"))
if sayi1<sayi2:
  for i in range(sayi1, sayi2 + 1):
    print(i)
elif sayi1>sayi2:
 for i in range(sayi2, sayi1 + 1):
   print(i)
else:
  print("geçersiz")

