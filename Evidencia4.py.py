#Operadores

#Ejercicio 1
def area_triangle():
    print ("====Calcular el area de un triangulo===\n")
    base = int(input("Ingrese la base del triangulo: "))
    height = int(input("Ingrese la altura del triangulo: "))
    area = (base * height) / 2
    print (f"El area del triangulo es {area}\n")
  
#Ejercicio 2

def addition ():
  print ("===Suma de dos números===\n")
  number_1 = int(input("Ingrese el primer número: "))
  number_2 = int(input("Ingrese el segundo número: "))
  suma = number_1 + number_2
  print (f"La suma de los dos números ingresados es: {suma}\n")

#Ejercicio 3

def squared_number():
  print ("===Elevar un número al cuadrado===\n")
  number_1 = int(input("Ingrese el número: "))
  operation = number_1 ** 2
  print (f"El número elevado al cuadrado es: {operation}\n")

#Ejercicio 4

def addition_2 ():
  print ("===Realizar la suma de los números 1234 y 532===\n")
  number_1= 1234
  number_2= 532
  operation = number_1 + number_2
  print (f"La suma de los números es {operation} \n")

#Ejercicio 5

def subtraction ():
  print ("===Realizar la resta de los números 1234 y 532===\n")
  number_1= 1234
  number_2= 532
  operation = number_1 - number_2
  print (f"La resta de los dos numeros es: {operation} \n")
  
#Ejercicio 6

def multiplication ():
  print ("===Realizar la multiplicación de los números 1234 y 532===\n")
  number_1= 1234
  number_2= 532
  operation = number_1 * number_2
  print (f"La multiplicación de los dos numeros es: {operation}\n ")

#Ejercicio 7

def division ():
  print ("===Realizar la división de los números 1234 y 532===\n")
  number_1= 1234
  number_2= 532
  operation = number_1 * number_2
  print (f"La división de los dos numeros es: {operation}\n ")

#Ejercicio 8

def module ():
  print ("===Calcular el modulo de los números 1234 y 532===\n")
  number_1= 1234
  number_2= 532
  operation = number_1 % number_2
  print (f"El modulo de los dos numeros es: {operation} \n")

#Ejercicio 9

def convert ():
  print ("===Convertir euros a dolares===\n")
  money = float(input("Ingrese la cantidad de euros que desea convertir: "))
  dolar = 0.911202
  operation = money / dolar
  print (f"La cantidad de euros ingresados es {money} que corresponde a {operation} dolares.\n")

#Ejercicio 10

def area_rectangle ():
  print ("===Calcular el area de un rectangulo===\n")
  base = float(input("Ingrese la base del rectangulo: "))
  height = float(input("Ingrese la altura del rectangulo: "))
  area = base * height
  print (f"El area del rectangulo es : {area} \n")

#Ejercicio 11

def area_perimeter_square ():
  print ("===Calcular el area y el perimetro de un cuadrado===\n")
  side = int(input("Ingrese la medida de un lado del cuadrado: "))
  area = side * side
  perimeter = side + side + side + side
  print  (f"El area del cuadrado es {area} y su perimetro es {perimeter}\n ")

#Ejercicio 12

def area_volume_cylinder ():
  print ("===Calcular el area y volumen de un cilindro===\n")
  radio = int(input("Ingrese la medida del radio del cilindro: "))
  height = int(input("Ingrese altura del cilindro: "))
  pi = 3.1416
  volume = (pi * radio ** 2) * height
  perimeter = (2 * pi * radio)
  area_1= perimeter * height
  area = (2 * radio ** 2) * pi + area_1
  print (f"El volumen del cilindro es: {volume} y su area es {area}\n ")

#Ejercicio 13

def area_length_circumference ():
  print ("===Calcular el area y longitud de una circunferencia===\n")
  radio = int(input("Ingrese la medida del radio de la circunferencia: "))
  pi = 3.1416
  diameter = 2 * radio
  length = diameter * pi
  area = pi * radio ** 2
  print (f"La longitud de la circunferencia es {length} y su area corresponde {area}\n")

#Ejercicio 14

def average ():
  print ("===Calcular el promedio de tres números===\n")
  number_1 = int(input("Ingrese el primer número: "))
  number_2 = int(input("Ingrese el segundo número: "))
  number_3 = int(input("Ingrese el tercer número: "))
  operation = (number_1 + number_2 + number_3) / 3
  print (f"El promedio de los números ingresados es : {operation}\n")

#Condicionales

#Ejercicio 1 condicionales

def number_negative ():
  print ("===Este programa sirve para saber si un numero es positivo o negativo===\n")
  number1 = int(input("Ingrese el número: "))
  if number1 > 0:
    print (f"El numero {number1} es positivo")
  elif number1 < 0:
    print (f"El numero {number1} es negativo")
  else:
    print (f"El numero ingresado es {number1} el cual se considera como numero neutro\n")

#Ejercicio 2 condicionales

def number_mayor():
  print ("===Este programa sirve para identificar el numero mayor y menor entre dos numeros.===\n")
  number1 = int(input("Ingrese el primer número: "))
  number2 = int(input("Ingrese el segundo número: "))
  if number1 > number2:
    mayor = number1
    menor = number2
  else:
    menor = number1
    mayor = number2
  print (f"El numero mayor es {mayor} y el numero menor es {menor}\n")

#Ejercicio 3 condicionales

def numbers_mayor():
  print ("===Este programa sirve para identificar el numero mayor y menor entre tres numeros positivos.===\n")
  number1 = int(input("Ingrese el primer número postivo: "))
  number2 = int(input("Ingrese el segundo número positivo: "))
  number3 = int(input("Ingrese el tercer número positivo: "))
  if (number1 > number2) and (number1 > number3):
    mayor = number1
  elif (number2 > number1) and (number2 > number3):
    mayor = number2
  else:
    mayor = number3
  if (number1 < number2) and (number1 < number3):
    menor = number1
  elif (number2 < number1) and (number2 < number3):
    menor = number2
  else:
    menor = number3
   
  print (f"El numero mayor es {mayor} y el numero menor es {menor}\n")

#Ejercicio 4 condicionales

def salary ():
  print ("===Calcula el sueldo de los empleados de la empresa===\n")
  name = input("Por favor ingrese su nombre: ")
  hours_worked = int(input("Por favor ingrese el total de horas trabajadas: "))
  hour_value = 4
  if hours_worked > 48:
    hour_extra= hours_worked - 48
    salary = (hours_worked * hour_value) + (hour_extra * 
    hour_value) * 2
  else:
    salary = (hours_worked * hour_value)
  print (f"El salario devengado del empleado {name} en la semana laborada es {salary}\n")

# Ejercicio 5 condicionales

def addition_subtraction ():
  print ("===Dado dos numeros A y B sumarlos si A es menor a B si no restarlos===\n")
  number_a= int(input("Ingrese el número A: "))
  number_b= int(input("Ingrese el número B: "))
  if number_a < number_b:
    operation = number_a + number_b
  else:
    operation = number_a - number_b
  print (f"El resultado de la operación es {operation}\n")

# Ejercicio 6 condicionales

def quotient1 ():
  print ("===Muestra el conciente entre dos numeros ===\n")
  number_a= int(input("Ingrese el número A: "))
  number_b= int(input("Ingrese el número B: "))
  if number_b == 0:
    print ("La división por cero no esta definida")
  else:
    operation = number_a / number_b
    print (f"El cociente entre A y B es: {operation}\n")

# Ejercicio 7 condicionales

def weekdays ():
  print ("===Muestra el dia de la semana que corresponde al valor ingresado ===\n")
  number_day = int(input("Ingresa un número del 1 al 7: "))
  if number_day == 1:
    print ("Lunes")
  elif number_day == 2:
    print ("Martes")
  elif number_day == 3:
    print ("Miercoles")
  elif number_day == 4:
    print ("Jueves")
  elif number_day == 5:
    print ("Viernes")
  elif number_day == 6:
    print ("Sabado")
  elif number_day == 7:
    print ("Domingo")
  else:
    print ("EL numero ingresado no es valido. Debe ser un número entre 1 y 7.\n")

# Ejercicio 8 condicionales

def equilateral_triangle ():
  print ("===Muestra si un triangulo es equilatero o no ===\n")
  side_1= int(input("Ingrese la medida del primer lado: "))
  side_2= int(input("Ingrese la medida del segundo lado: "))
  side_3= int(input("Ingrese la medida del tercer lado: "))
  if (side_1 == side_2 == side_3):
    print ("El triángulo es equilatero")
  else:
    print ("El triángulo no es equilatero\n")

# Ejercicio 9 condicionales

def addition_multiplication ():
  print ("===Dado dos numeros A y B sumarlos si alguno de ellos es negativo en caso contrario multiplicarlos===\n")
  number_a = int(input("Ingrese el primer número: "))
  number_b = int(input("Ingrese el segundo número: "))
  if number_a < 0 or number_b < 0:
    operation = number_a + number_b
  else:
    operation = number_a * number_b
  print (f"El resultado de la operacion es {operation}\n")

# Ejercicio 10 condicionales

def zodiac_sign ():
  print ("===Muestra tu signo zodiacal segun tu fecha de nacimiento===\n")
  month = int(input("Ingresa el mes de tu nacimiento: "))
  day = int(input("Ingresa el día de tu nacimiento: "))
  if (month ==1 and day >=21) or (month ==2 and day <=19):
    print ("Tu signo zodiacal es Acuario.")
  elif (month ==2 and day >=20) or (month ==3 and day <=20):
    print ("Tu signo zodiacal es Piscis.")
  elif (month ==3 and day >=21) or (month ==4 and day <=20):
    print ("Tu signo zodiacal es Aries.")
  elif (month ==4 and day >=21) or (month ==5 and day <=21):
    print ("Tu signo zodiacal es Tauro.")
  elif (month ==5 and day >=22) or (month ==6 and day <=21):
    print ("Tu signo zodiacal es Géminis.")
  elif (month ==6 and day >=22) or (month ==7 and day <=22):
    print ("Tu signo zodiacal es Cancer.")
  elif (month ==7 and day >=23) or (month ==8 and day <=22):
    print ("Tu signo zodiacal es Leo.")
  elif (month ==8 and day >=23) or (month ==9 and day <=22):
    print ("Tu signo zodiacal es Virgo.")
  elif (month ==9 and day >=23) or (month ==10 and day <=22):
    print ("Tu signo zodiacal es Libra.")
  elif (month ==10 and day >=23) or (month ==11 and day <=22):
    print ("Tu signo zodiacal es Escorpio.")
  elif (month ==11 and day >=23) or (month ==12 and day <=21):
    print ("Tu signo zodiacal es Sagitario.")
  elif (month ==12 and day >=22) or (month ==1 and day <=20):
    print ("Tu signo zodiacal es Capricornio.\n")

# Ejercicio 11 condicionales

def square_rectangle ():
  print ("===Muestra segun lo datos ingresados si la figura es un cuadrado o un rectangulo y muestra en area y el perimetro de la figura===\n")
  base = int(input("Ingrese la base del cuadrilátero: "))
  height = int(input("Ingrese la altura del cuadrilátero: "))
  if base == height:
    print ("El cuadrilatero es un cruadrado")
    figure = "cuadrado"
  else:
    print ("El cuadrilátero es un rectangulo")
    figure = "rectangulo"
  perimetro = (base * 2) + (height * 2)
  area = base * height
  print (f"El perimetro del {figure} es {perimetro}\n")
  print (f"El area de {figure} es {area}\n")

# Ejercicio 12 condicionales

def sale_discount ():
  print ("===Muestra el descuento de venta de un negocio===\n")
  price = int(input("Ingrese el valor de su compra: "))
  if price < 100:
    discount = price * 0.05
  elif price < 200:
    discount = price * 0.1
  else:
    discount = price * 0.15
    
  price_final = price - discount
  print (f"El descuento realizado a su compra es de {discount} % y el precio final menos el descuento realizado es de {price_final}\n")

#Ciclos

# Ejercicio 1

def multiples_3 ():
  print ("===Muestra todos los múltiplos de 3 que hay entre 1 y 100.===\n")
  for x in range (1,100):
    if x % 3 == 0:
      print (f"Los numeros multiplos de 3 son : {x} \n")

# Ejercicio 2 ciclos

def odd_numbers ():
  print ("===Muestra los números impares entre 0 y 100.===\n")
  for x in range (0,100):
    if x % 2 == 1:
      print (f"Los numeros impares entre 0 y 100 son : {x}\n")

# Ejercicio 3 ciclos

def pair_numbers():
  print ("===Muestra los números pares entre 0 y 100.===\n")
  for x in range(0,100):
    if x % 2 == 0:
     print (f"Los numeros pares entre 0 y 100 son : {x}\n")

# Ejercicio 4 ciclos

def numbers_1():
  print ("===Muestra en pantalla los numeros del 1 al 3===\n")
  lista = [1,2,3]
  for x in lista:
    print (x)

# Ejercicio 5 ciclos

def numbers_2():
  print ("===Muestra en pantalla los numeros del 1 al 9===\n")
  for x in range (1,10):
    print (x)

# Ejercicio 6 ciclos

def numbers_3():
  print ("===Muestra en pantalla los numeros del 1 al 10000===\n")
  for x in range (1,10001):
    print (x)

# Ejercicio 7 ciclos

def numbers_4():
  print ("===Muestra en pantalla los numeros del 5 al 10===\n")
  for x in range (5,11):
    print (x)

# Ejercicio 8 ciclos

def numbers_5():
  print ("===Muestra en pantalla los numeros del 5 al 15===\n")
  for x in range (5,16):
    print (x)

# Ejercicio 9 ciclos

def numbers_6():
  print ("===Muestra en pantalla los numeros del 5 al 15000===\n")
  for x in range (5,15001):
    print (x)

# Ejercicio 10 ciclos

def hello ():
  print ("===Muestra un programa en Java que imprima 200 veces la palabra \"hola\".===\n")
  for x in range (1,201):
    print ("Hola")

# Ejercicio 11 ciclos

def squared_numbers1 ():
  print ("===Muestra los cuadrados de los numeros del 1 al 30===\n")
  for x in range (1,31):
    x **= 2
    print (x)

# Ejercicio 12 ciclos

def multplication_natural ():
  print ("===Muestra la multiplicación de los 20 primeros números naturales (1*2*3*4*5…).===\n")
  operation = 1
  for x in range (1,21):
    operation *= x
  print (f"La multiplicacion de los primeros 20 numeros naturales es : {operation}\n")

# Ejercicio 13 ciclos

def squared_addition ():
  print ("===Muestra la suma de los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla.===\n")
  suma = 0
  for x in range (1,101):
    x **= 2
    suma = suma + x
  print (f"La suma de los primeros 100 números naturales es {suma}\n")

# Ejercicio 14 ciclos

def addition_int ():
  print ("===Ingrese un número entero y el programa realizara la suma de los 100 números siguientes, mostrando el resultado en pantalla. (Ejemplo: el usuario digita 5, se debe sumar 5+6+7+8+… hasta que complete 100 números).\n")
  number = int(input("Ingrese el número: "))
  for x in range (number,number + 101):
    x +=1
    number = number + x
  print (f"La suma de los números es: {number}\n")

# Ejercicio 15 ciclos

def odd_numbers1 ():
  print ("===Ingrese un número entero y el programa mostrara todos los números impares menores que él.===\n")
  number = int(input("Ingrese el número: "))
  for x in range(1,number):
    if x % 2 == 1:
      print (f"Los números impares menores son : {x}\n""")

# Ejercicio 16

def factorial():
  print ("===Muestra el número factorial del número ingresado===\n")
  number = int(input("Ingrese el número: "))
  operation = 0
  if number < 0:
    print ("El numero debe ser tipo entero positivo")
  elif number == 0 or number == 1:
    operation = 1
    print (f"el numero factorial de {number} es : {operation} ")
  else:
    operation = 1
    for x in range (1,number+1):
      operation *=x
    print (f"El factorial del numero {number} es : {operation} ")

# Ejercicio 17

def degrees ():
  while True:
    print ("===Este programa convertira grados fahrenheit a grados celsius - Salir del programa ingrese 999 ===\n")
    degreesf = int(input("Ingrese los grados fahrenheit a conventir: "))
    if degreesf == 999:
      break
    else:
      operation = (degreesf - 32) * 5 / 9
      print (f"\nLa temperatura ingresada en grados fahrenheit es {degreesf} que corresponde a {operation} grados celsius.\n") 

#Ejercicio 18

def numbers_prime ():
  print ("===Muestra los números primos hasta un número ingresado por el usuario.===")
  number = int(input("Ingrese un numero : "))
  for x in range (2,number + 1):
    prime = True
    for j in range (2,x):
      if x % j == 0:
        prime = False
        break
    if prime:
      print (x)
      

# Ejercicio 19

def multiplication_number ():
  print ("Muestra la tabla de multiplicar que desees: \n")
  multiplication = int(input("Ingrese el número de la tabla de multiplicación : "))
  for x in range (1,11):
    operation = x * multiplication
    print (f"{multiplication} * {x} = {operation}")

# Ejercicio 20

def average_positive ():
  print ("===Ingrese la cantidad de numeros positivos que desee y haremos el promedio de los números:\"ingrese valores negativos para salir===\"")
  addition = 0
  counter = 0
  while True:
    number = int (input("Ingrese números: "))
    if number < 0:
      break
    addition += number
    counter += 1
  if counter > 0:
    average = addition / counter
    print (f"El promedio de los números ingresados es: {average}")
  else:
    print ("No se ingresaron números positivos")

# Ejercicio 21

def numbers_7 ():
  print ("===Muestra los números comprendidos entre los números ingresados")
  number_1 = int(input("Ingrese el primer número: "))
  number_2 = int(input("Ingrese el segundo número: "))
  for x in range (number_1,number_2 + 1):
    print (x)

# Ejercicio 22

def domino ():
  for x in range (7):
    for j in range (7):
      print (x , "-" , j)

# Listas

#Ejercicio 1

def list_1():
  print ("===Suma de elementos: Escribe una función que tome una lista de números como entrada y devuelva la suma de todos los elementos de la lista.===\n")
  print ("===Escriba la palabra \"salir\" para realizar la suma de los números ingresados.===\n")
  addition = []
  while True:
    number = input("Ingrese un número: ")
    if number.lower() == "salir":
      break
    number = int(number)
    addition.append(number)
  operattion = 0
  for i in addition:
    operattion += i
  print (f"La suma de los números ingresados en la lista es de : {operattion}")

# Ejercicio 2

def list_2():
  print ("===Promedio de valores: Escribe una función que tome una lista de números como entrada y calcule el promedio de todos los valores de la lista.===\n")
  print ("===Ingrese la palabra \"salir\" para realizar el promedio de los números ingresados.===\n")
  average = []
  while True:
    numbers = input("Ingrese un número: ")
    if numbers.lower() == "salir":
      break
    numbers= int(numbers)
    average.append(numbers)
  amount = len(average)
  operattion = 0
  for i in average:
    operattion += i
  operattion /= amount
  print (f"El promedio de los números ingresados es : {operattion}")

# Ejercicio 3

def list_3():
  print ("===Eliminación de duplicados: Escribe una función que tome una lista como entrada y elimine todos los elementos duplicados, dejando solo una aparición de cada elemento en la lista final.===\n")
  print ("===Ingrese la palabra \"salir\" para eliminar los duplicados de los datos ingresados.===\n")
  date = []
  while True:
    income = input("Ingrese un dato: ")
    if income.lower() =="salir":
     break
    try:
      date.append(int(income))
    except ValueError:
      try:
        date.append(float(income))
      except ValueError:
        date.append(income)
  date = list(set(date))
  print(f"Lista sin valores duplicados: {date}")

# Ejercicio 4

def list_4():
  print ("===Ordenar lista: Escribe una función que tome una lista de números como entrada y la ordene de menor a mayor. No utilices la función de ordenación incorporada en Python.===\n")
  print ("===Ingrese la palabra \"salir\" para ordenar la lista ingresada.===\n")  
  list = []  
  while True:
    numbers = input("Ingrese un número: ")
    if numbers.lower() == "salir":
      break
    try: 
      list.append(int(numbers))
    except ValueError:
      list.append(float(numbers))
  
  print (f"Muestra la lista original {list}")
  
  for i in range (len(list)):
    for j in range (len(list)-i-1):
      if list[j] > list[j+1]:
        list[j] , list[j+1] = list[j+1] , list[j]
  print(f"Muestra los numeros ingresados de menor a mayor: {list}")
  
# Ejercicio 5

def list_5():
  print ("===Palabras más largas: Escribe una función que tome una lista de palabras como entrada y devuelva la palabra más larga de la lista. Si hay varias palabras con la misma longitud máxima, devuelve la primera que aparezca en la lista.===\n")  
  print ("===Escribe la palabra salir para organizar las palabras por longitud===")  
  list = []  
  while True:
    words = input ("Ingrese una palabra: ")
    if words.lower() == "salir":
      break
    if words.isalpha():
      list.append(words)
    else:
      print ("Por favor ingrese solo palabras")
  
  longest_word=""
  first_longest_word=""
  for i in list:
    if len(i) > len(longest_word):
      longest_word = i
      first_longest_word = i
    elif len(i) == len(longest_word) and first_longest_word == "":
      first_longest_word = i
  print (f"la palabra mas larga encontrada en los datos ingresados es: {first_longest_word}")

# tuplas
  
# Ejercicio 1

def tuple_exercises_1():  
  print ("===Producto de elementos: Escribe una función que tome una tupla de números como entrada y devuelva el producto de todos los elementos de la tupla.===\n")  
  print ("===Escribe la palabra 'salir' para que el aplicativo muestre el producto de los números ingresados.===")  
  list = []  
  while True:
    numbers = input("Ingresa un numero: ")
    if numbers.lower() == "salir":
      break
    if numbers.isdigit():
      list.append(int(numbers))
    else:
      print ("Por favor Ingresa solo números")
  
  tuple_1 = tuple(list)
  operation = 1
  for i in tuple_1:
    operation *= i
  print (f"El producto de los números ingresados es : {operation}")
  
# Ejercicio 2

def tuple_exercises_2():  
  print ("===Mayor y menor elemento: Escribe una función que tome una tupla de números como entrada y devuelva el valor máximo y mínimo de la tupla.===\n")  
  print ("===Escribe la palabra 'salir' para que el número mayor y el número menor de los datos ingresados.===\n")  
  list = []  
  while True:
    numbers = input("Ingresa un numero: ")
    if numbers.lower() == "salir":
      break
    if numbers.isdigit():
      list.append(int(numbers))
    else:
      print ("Por favor Ingresa solo números")
  
  tuple_2 = tuple(list)
  maximum = tuple_2[0]
  minimum = tuple_2[0]
  for i in tuple_2[1:]:
    if i > maximum:
      maximum = i
    if i < minimum:
      minimum = i
  print (f"El número menor ingresado es {minimum} y el mayor es {maximum}")
  
# Ejercicio 3

def tuple_exercises_3():  
  print ("===Contar ocurrencias: Escribe una función que tome una tupla como entrada y cuente cuántas veces aparece cada elemento en la tupla, devolviendo un diccionario con los elementos como claves y las ocurrencias como valores.===\n")
  print ("===Escribe la palabra 'salir' para mostrar la duplicidad de cada elemento y cuantas veces se repiten.===\n")  
  list = []  
  while True:
    data = input ("Ingrese un dato: ")
    if data.lower() == "salir":
      break
    list.append(data)
  
  tuple_3 = tuple(list)
  ocurrences = {}
  for i in tuple_3:
    if i in ocurrences:
      ocurrences[i] +=1
    else:
      ocurrences[i] = 1
  print (f"Muestra las veces que se repite un elemeto:\n {ocurrences}")
  
# Ejercicio 4

def tuple_exercises_4():
  print ("===Buscar índices: Escribe una función que tome una tupla y un elemento como entrada, y devuelva una lista con todos los índices en los que aparece el elemento en la tupla.===\n")  
  print ('===Ingrese la palabra "salir" para buscar los indices de los datos ingresados.===\n')  
  list = []  
  while True:
    data = input("Ingrese un dato: ")
    if data.lower() == "salir":
      break
    list.append(data)  
  
  tuple_4 = tuple(list)
  element = input("Ingrese el elemento que desea buscar: ")
  list_1 = []
  for i in range(len(tuple_4)):
    if tuple_4[i] == element:
      list_1.append(i)
  
  print (f"Los indices del elemento {element} en la lista son : {list_1}")
  
# Ejercicio 5

def tuple_exercises_5():
  print ("===Separar elementos: Escribe una función que tome una tupla de cadenas como entrada y devuelva dos tuplas separadas: una con todas las cadenas que empiezan con una vocal y otra con las que no.===\n")
  print ('===Ingrese la palabra "salir" para mostrar las tuplas de los datos ingresados.===\n')  
  data = []  
  while True:
    words = input("Ingrese una palabra: ")
    if words.lower() == "salir":
      break
    if words.isalpha():
      data.append(words)
    else:
      print ("Por favor ingrese palabras")
  
  tuple_5 = tuple(data)
  words_with_vowels = ()
  words_without_vowels = ()
  vowels = ("a" , "e" , "i" , "o" , "u" )
  for i in tuple_5:
    i=i.lower()
    if i.startswith(vowels):
      words_with_vowels += (i,)
    else:
      words_without_vowels += (i,)
  
  print (f"Palabras que comienzan por vocal : {words_with_vowels}")
  print (f"Palabras que no comienzan con vocal : {words_without_vowels}")

# Diccionarios

# Ejercicio 1

def diccionary_exercise_1():
  print ("===Contar palabras: Escribe una función que tome una lista de palabras como entrada y devuelva un diccionario que cuente cuántas veces aparece cada palabra en la lista.===\n")  
  print ("===Escriba la palabra 'salir' para contar cuantas veces aparece cada palabra.===\n")  
  data = []  
  while True:
    words = input("Ingrese una palabra: ")
    if words.lower() == "salir":
      break
    if words.isalpha():
      data.append(words)
    else:
      print ("Por favor ingrese palabras")
  
  diccionary = {}
  for i in data:
    if i in diccionary:
      diccionary[i] += 1
    else:
      diccionary[i] = 1
  print (f"La cuenta de las veces que ingresaste el mismo elemento es el siguiente: {diccionary}")
  
# Ejercicio 2

def diccionary_exercise_2():
  print ("===Calcular promedio de calificaciones: Escribe una función que tome un diccionario de estudiantes y sus calificaciones como entrada, y calcule el promedio de calificaciones de todos los estudiantes.===\n")
  
  diccionary = {}
  
  while True:
    name= input("Ingrese el nombre del estudiante (o ' salir'para finalizar): ")
    if name.lower() == "salir":
      break
    qualifications = []
    while True:
      qualification = input("Ingrese la califación del alumno (o 'fin' para salir):")
      if qualification.lower() == "fin":
        break
      qualifications.append(float(qualification))
    diccionary[name]=(qualifications)
    print (diccionary)
  total_calificaciones = 0
  cantidad_calificaciones = len(diccionary)
  
  for qualifications in diccionary.values():
      total_calificaciones += sum(qualifications)
      cantidad_calificaciones += len(qualifications)
  
  promedio = total_calificaciones / cantidad_calificaciones
  promedio = diccionary_exercise_2()
  print("El promedio de calificaciones es:", promedio)
  return (promedio)  

  
while True:
  menu = int(input("""MENU PRINCIPAL
  
Elige una de las siguientes opciones:

1.Operadores
2.Condicionales
3.Ciclos
4.Arreglos
5.Salir
\n"""))
  print (f"\nIngresaste la opción numero: {menu}\n")
  if menu == 1:
    while True:
      submenu= int(input("""Escoge el ejercicio de Operadores que deseas. 
    
1.Calcular el área de un triangulo.
2.Ingresar dos números y realizar suma.
3.Ingresar un numero y elevarlo al cuadrado.
4.Realizar la suma de los números 1234 y 532.
5.Realizar la resta de los números 1234 y 532.
6.Realizar la multiplicación de los números 1234 y 532.
7.Realizar la división de los números 1234 y 532.
8.Modulo de los números 1234 y 532.
9.Convertir euros a dólares.
10.Calcular el area de un rectangulo.
11.Calcular el area y perimero de un cuadrado.
12.Calcular el área y volumen de un cilindro.
13.Calcular el area y longitud de una circunferencia.
14.Calcular el promedio de 3 números.
15.Salir de Operadores.
    
"""))
      print (f"La operacion que realizara el aplicativo es :{submenu}\n\n")
      while True:
        if submenu == 1:
          area_triangle()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 2:
          addition()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 3:
          squared_number()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 4:
          addition_2()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 5:
          subtraction()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 6:
          multiplication()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 7:
          division()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 8:
          module()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 9:
          convert()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 10:
          area_rectangle()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 11:
          area_perimeter_square()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 12:
          area_volume_cylinder()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 13:
          area_length_circumference()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 14:
          average()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu >= 15:
          break
      break     
  elif menu == 2:
    while True:
      submenu= int(input("""Escoge el ejercicio de Condicionales que deseas.

1.Codigo para saber si un numero es positivo o negativo.
2.Comparar dos numeros y decir cual es mayor o menor.
3.Comparar tres numeros positivos y decir cual es mayor y menor entre ellos.
4.Calcular el sueldo de los empleados de una empresa.
5.Dado dos números A y B sumarlos si A es menor a B sino restarlos.
6.Dado dos números A y B encontrar el cociente entre A y B.
7.Muestra el nombre del día de la semana que corresponde al valor ingresado.
8.Muestra si un triangulo es equilatero o no.
9.Dado dos números A y B sumarlos si alguno de ellos es negativo en caso contrario multiplicarlos.
10.Ingrese el dia y el mes de nacimiento y mostrara tu signo zodiacal.
11.Indica si es un cuadrado o un rectangulo para cualquiera de los dos casos mostrara el perimetro y la superficie.
12.Mostrara el descuento que ofrece la tienda por la compra realizada.
13.Salir de condionales.
\n"""))

      print (f"\nEscogiste la opcion : {submenu}\n")
      while True:
        if submenu == 1:
          number_negative()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 2:
          number_mayor()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 3:
          numbers_mayor()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 4:
          salary()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 5:
          addition_subtraction()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 6:
          quotient1()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 7:
          weekdays()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 8:
          equilateral_triangle()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 9:
          addition_multiplication()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 10:
          zodiac_sign()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 11:
          square_rectangle()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu == 12:
          sale_discount()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break     
        elif submenu >= 13:
          break
      break
             
  elif menu == 3:
    while True:
      submenu = int(input("""Escoge el ejercicio de Ciclos que deseas.

1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100.
2.Imprimir los números impares entre 0 y 100.
3.Imprimir los números pares del 0 al 100.
4.Programa que muestra por pantalla los números del 1 al 3.
5.Programa que muestra por pantalla los números del 1 al 9.
6.Programa que muestra por pantalla los números del 1 al 10.000.
7.Programa que muestra por pantalla los números del 5 al 10.
8.Programa que muestra por pantalla los números del 5 al 15.
9.Programa que muestra por pantalla los números del 5 al 15.000.
10.Programa que muestra 200 veces la palabra “hola”.
11.Programa que muestra por pantalla los cuadrados de los números del 1 al 30.
12.Programa que multiplique los 20 primeros número naturales (1*2*3*4*5…).
13.Programa que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla.
14.Programa que lea un número entero desde teclado y realiza la suma de los 100 número siguientes, mostrando el resultado en pantalla. (Ejemplo: el usuario digita 5, se debe sumar 5+6+7+8+… hasta que complete 100 números).
15.Programa que lea un número entero por el teclado e imprima todos los números impares menores que él.
16.Halle el número factorial de un número ingresado.
17.Programa que lea temperaturas expresadas en grados Fahrenheit y las convierta a grados Celsius mostrándola. El programa finalizará cuando lea un valor de temperatura igual a 999. La conversión de grados Fahrenheit (F) a Celsius (C) está dada por C = 5/9(F - 32).
18.Muestra los números primos hasta un número ingresado por el usuario.
19.Muestra por pantalla la tabla de multiplicar que el usuario desee.
20.Se dispone de un conjunto de números positivos. Calcular y escribir su promedio sabiendo que se ingresará un valor menor a 0 para indicar el fin del conjunto de valores
21.Dados dos números naturales, el primero menor al segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente.
22.Realizar un algoritmo que muestre los valores de todas las piezas del domino de forma ordenada: 0-0 0-1 1-1 0-2 1-2 2-2
\n"""))
      print (f"La operacion que realizara el aplicativo es :{submenu}\n\n")
      while True:
        if submenu == 1:
          multiples_3()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 2:
          odd_numbers()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 3:
          pair_numbers ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 4:
          numbers_1 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 5:
          numbers_2 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 6:
          numbers_3 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 7:
          numbers_4 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 8:
          numbers_5 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 9:
          numbers_6 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 10:
          hello ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 11:
          squared_numbers1 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 12:
          multplication_natural ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 13:
          squared_addition ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 14:
          addition_int ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 15:
          odd_numbers1 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 16:
          factorial ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 17:
          degrees ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 18:
          numbers_prime ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 19:
          multiplication_number ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 20:
          average_positive ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 21:
          numbers_7 ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 22:
          domino ()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu >= 23:
           break
      break
  elif menu == 4:
    while True:
      submenu = int(input("""Escoge el ejercicio de listas (1-5), tuplas (6-10) y diccionarios (11-15) que deseas.

1.Suma de elementos: Escribe una función que tome una lista de números como entrada y devuelva la suma de todos los elementos de la lista.
2.Promedio de valores: Escribe una función que tome una lista de números como entrada y calcule el promedio de todos los elementos de la lista.
3.Eliminación de duplicados: Escribe una función que tome una lista como entrada y elimine todos los elementos duplicados, dejando solo una aparición de cada elemento en la lista final.
4.Ordenar lista: Escribe una función que tome una lista de números como entrada y la ordene de menor a mayor. No utilices la función de ordenación incorporada en Python.
5.Palabras más largas: Escribe una función que tome una lista de palabras como entrada y devuelva la palabra más larga de la lista. Si hay varias palabras con la misma longitud máxima, devuelve la primera que aparezca en la lista.
6.Producto de elementos: Escribe una función que tome una tupla de números como entrada y devuelva el producto de todos los elementos de la tupla.
7.Mayor y menor elemento: Escribe una función que tome una tupla de números como entrada y devuelva el valor máximo y mínimo de la tupla.
8.Contar ocurrencias: Escribe una función que tome una tupla como entrada y cuente cuántas veces aparece cada elemento en la tupla, devolviendo un diccionario con los elementos como claves y las ocurrencias como valores.
9.Buscar índices: Escribe una función que tome una tupla y un elemento como entrada, y devuelva una lista con todos los índices en los que aparece el elemento en la tupla.
10.Separar elementos: Escribe una función que tome una tupla de cadenas como entrada y devuelva dos tuplas separadas: una con todas las cadenas que empiezan con una vocal y otra con las que no.
11.Contar palabras: Escribe una función que tome una lista de palabras como entrada y devuelva un diccionario que cuente cuántas veces aparece cada palabra en la lista.
12.Calcular promedio de calificaciones: Escribe una función que tome un diccionario de estudiantes y sus calificaciones como entrada, y calcule el promedio de calificaciones de todos los estudiantes.
13.Filtrar por valor: Escribe una función que tome un diccionario y un valor como entrada, y devuelva un nuevo diccionario que contenga solo las parejas clave-valor del diccionario original cuyo valor sea igual al valor dado.
14.Combinar diccionarios: Escribe una función que tome dos diccionarios como entrada y los combine en uno solo, sumando los valores de las claves que sean comunes en ambos diccionarios.
15.Palabras más frecuentes: Escribe una función que tome un texto como entrada y devuelva un diccionario que cuente cuántas veces aparece cada palabra en el texto, ignorando el caso (mayúsculas y minúsculas).
16.Salir al menu principal.
\n"""))
      print (f"La operacion que realizara el aplicativo es :{submenu}\n\n")
      while True:
        if submenu == 1:
          list_1()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 2:
          list_2()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 3:
          list_3()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 4:
          list_4()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 5:
          list_5()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 6:
          tuple_exercises_1()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 7:
          tuple_exercises_2()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 8:
          tuple_exercises_3()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 9:
          tuple_exercises_4()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 10:
          tuple_exercises_5()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 11:
          diccionary_exercise_1()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 12:
          diccionary_exercise_2()
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 13:
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
            break
        elif submenu == 14:
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu == 15:
          answer = input ("¿Deseas continuar? (s/n): ")
          if answer.lower() != "s":
           break
        elif submenu >= 16:
           break
      break
  else:
    print ("Hasta pronto!!")
    break