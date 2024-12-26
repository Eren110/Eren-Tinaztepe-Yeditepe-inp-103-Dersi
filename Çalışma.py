konto = 1000

print("1: Einzahlen (Einzahlung)")
print("2: Auszahlen (Auszahlung)")

menu = int(input("wahlen sie eine option (1 oder 2): " ))
if menu == 1:
  
  geld = float(input("geben sie den betrag ein. den sie einzahlen möchten: "))
  konto += geld
  print("Neues Guthaben:", konto)
  
elif menu == 2:
  geld = float(input("geben sie den betrag ein, den sie abheben möcthen"))
  if geld <= konto:
      konto -= geld
      print("neues guthaben:", konto)
  else:
      print("fehler: nicht genügend guthaben auf dem konto!")
      
else:
   print("ungültige auswahl!")
   
print("karte wurde entnommen.")