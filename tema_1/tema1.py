# tema_capitol_1.py
# Tema: Scrieți un program care să conțină 4 variabile cu valori introduse de utilizator folosind funcția input().
# În funcția input() trebuie scrise întrebări adresate utilizatorului, astfel încât răspunsurile să corespundă tipurilor variabilelor:
# - una de tip str (text)
# - una convertită cu int()
# - una cu float()
# - una cu bool()
# Programul va afișa apoi fiecare variabilă împreună cu tipul acesteia, folosind funcțiile print() și type().


nume = input("Care este numele tau? ")

varsta = int(input("Ce vârstă ai? (introdu un număr întreg) "))

inaltime = float(input("Ce înălțime ai? (în metri, ex: 1.75) "))

este_student_input = input("Ești student? (da/nu) ").strip().lower()
este_student = True if este_student_input == "da" else False

     
nume = "Darian"
varsta = 18
inaltime = 1.84
este_student = True


print(nume, type(nume))
print(varsta, type(varsta))
print(inaltime, type(inaltime))
print(este_student, type(este_student))
