# Imprimir valores de 1 a 100
def rangeNum(val):
    rangeList = []
    i = 1
    while i <= val:
        rangeList.append(i)
        i += 1
    return rangeList
print("Rango: ", rangeNum(100))

# Calcular si es par o impar
def par(val):
    return val % 2 == 0
print("Par: ", par(2))

# Sumar dos valores
def sum(a, b):
    return a + b
print("Suma: ", sum(2, 3))

# Contar vocales de una palabra
def vowels(word):
    count = 0
    word = word.lower()
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count
print("Vocales: ", vowels("Murcielago"))

# Invertir una cadena
def reverse(val):
    reverse = ""
    for char in val:
        reverse = char + reverse
    return reverse
print("Reverso: ", reverse("Hola"))

# Validar palíndromo
def reverse(val):
    val = val.lower()
    reverse = ""
    for char in val:
        reverse = char + reverse
    return reverse == val
print("Palíndromo: ", reverse("Reconocer"))

# Generar serie de Fibonacci
def fibonacci(n):
    a = 0
    b = 1
    c = 0
    series = []
    if n < 0:
        return "Mal input"
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        while True:
            c = a + b
            a = b
            b = c
            if b <= n:
                series.append(b)
            else:
                break
        return series
print("Fibonacci: ", fibonacci(9))

# Calculadora
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Operador no válido"
print("Calculadora: ", calculator(2, 3, "+"))

# Ordernar lista de forma manual
def sort(val):
    for i in range(len(val)):
        for j in range(i + 1, len(val)):
            if val[i] > val[j]:
                val[i], val[j] = val[j], val[i]
    return val
print("Lista ordenada: ", sort([5, 2, 9, 1, 5, 6]))

# Tabla de multiplicar
def multiplication(val, range_):
    table = []
    i = 0
    while i <= range_:
        table.append(val * i)
        i += 1
    return table
print("Tabla de multiplicar: ", multiplication(2, 10))

# Lee un archivo .txt y cuenta las palabras
file = open("text.txt", "r")
def countWords(file):
    count = 0
    for line in file:
        words = line.split()
        count += len(words)
    return count
print("Palabras: ", countWords(file))
file.close()

# Usa una lista de diccionarios para almacenar alumnos con notas y calcula el promedio
def average(students):
    averages = {}
    for student, grades in students.items():
        sumN = 0
        avg = 0
        for grade in grades:
            sumN += grade
        avg = sumN / len(grades)
        averages[student] = avg
    return averages
students = {"Juan": [8, 9, 10], "Maria": [7, 8, 9], "Pedro": [6, 5, 4]}
print(average(students))

# Crea un programa que verifique contraseñas fuertes
def strongPassword(password):
    if len(password) < 12:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in "!@#$%^&*()-+" for char in password):
        return False
    return True
print("Contraseña fuerte: ", strongPassword("Contraseña123!"))

# Implementa un sistema de login con usuarios y contraseñas almacenadas en un diccionario
users = {
    "jsgonzalez": "Contraseña123!",
    "mrodriguez": "Contraseña124!",
    "jgarcia": "Contraseña124!",
}
cases = {0: "Login correcto", 1: "Contraseña incorrecta", 2: "Usuario no encontrado"}
def login(user, password):
    if user in users:
        if users[user] == password:
            return 0
        else:
            return 1
    else:
        return 2
# user = input('Usuario: ')
# password = input('Contraseña: ')
user = "jsgonzalez"
password = "Contraseña123!"
print("Login: ", cases[login(user, password)])

# Crea una función que reciba una lista de números y devuelva otra con solo los primos
import math
def primes(values):
    primes = []
    for val in values:
        if val < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(val)) + 1):
            if val % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(val)
    return primes
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Primos: ", primes(values))

# Simula el juego de adivinar un número entre 1 y 100
import random
def guessNumber(val):
    number = random.randint(1, 100)
    return number == val
print("Random:", guessNumber(50))

# Crea un script que detecte anagramas
def anagramas(a,b):
     return sorted(a) == sorted(b)
print("Anagramas: ", anagramas("amor", "roma"))

# Genera un archivo CSV con nombres y edades
def genCsv(filename, data):
     with open(filename, 'w') as file:
          for row in data:
               row_str = ','.join(map(str, row))
               file.write(row_str + '\n')

data = [
    ["Nombre", "Edad"],
    ["Juan", 25],
    ["Maria", 30],
    ["Pedro", 22]
]
genCsv("data.csv", data)

# Crea una función que reciba una fecha y diga cuántos días faltan para esa fecha
import datetime
def getDate(date):
    today = datetime.date.today()
    date = datetime.datetime.strptime(date, "%m/%d/%Y").date()
    return (date - today).days
print("Días restantes: ", getDate("05/01/2025"))

# Simula una pequeña agenda donde puedas agregar, buscar y eliminar contactos
contacts = {}
def addContact(name, phone):
    contacts[name] = phone
def searchContact(name):
     return contacts.get(name, "No encontrado")
def deleteContact(name):
     if name in contacts:
          del contacts[name]
          return "Eliminado"
     else:
          return "No encontrado"
addContact("Juan", "123456789")
addContact("Maria", "987654321")
print("Buscar contacto: ", searchContact("Juan"))
print("Eliminar contacto: ", deleteContact("Maria"))