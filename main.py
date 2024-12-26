punktzahl = float(input("punktzahl: "))
programmiererfahrung = int(input("programmiererfahrung (1-5): "))

if punktzahl > 90 or (programmiererfahrung == 5 and punktzahl >= 70):
  print("einstellen")
elif punktzahl >= 70 and programmiererfahrung == 4:
  print("zum Gesprach einladen")
else:
       print("ablehnen")