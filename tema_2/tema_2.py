# 1. Calculator simplu
print("=== 1. Calculator simplu ===")
a = float(input("Introdu primul număr: "))
b = float(input("Introdu al doilea număr: "))
print("Suma:", a + b)
print("Diferența:", a - b)
print("Produsul:", a * b)
print("Împărțirea normală:", a / b)
print("Împărțirea întreagă:", a // b)
print("Restul împărțirii:", a % b)

# 2. Perimetru și arie dreptunghi
print("\n=== 2. Perimetru și Arie Dreptunghi ===")
lungime = float(input("Introdu lungimea: "))
latime = float(input("Introdu lățimea: "))
print("Perimetru:", 2 * (lungime + latime))
print("Arie:", lungime * latime)

# 3. Comparare numere
print("\n=== 3. Comparare numere ===")
x = float(input("Introdu primul număr: "))
y = float(input("Introdu al doilea număr: "))
print("Rezultat comparare:", x > y, x < y, x == y)

# 4. Par sau impar
print("\n=== 4. Par sau impar ===")
n = int(input("Introdu un număr: "))
print("Rest la împărțirea la 2:", n % 2)

# 5. Calcul vârstă
print("\n=== 5. Calcul vârstă ===")
an_nastere = int(input("Introdu anul nașterii: "))
import datetime
print("Vârsta:", datetime.datetime.now().year - an_nastere)

# 6. Conversia timpului
print("\n=== 6. Conversia timpului ===")
secunde_totale = int(input("Introdu numărul total de secunde: "))
print("Ore:", secunde_totale // 3600)
print("Minute:", (secunde_totale % 3600) // 60)
print("Secunde:", secunde_totale % 60)
