import random  # Importamos la librería random

import time  # Importamos la librería time

iniciar_trivia = True  # Iniciamos la variable en True

intentos = 0  # variable que almacenará el número de veces que el usuario usara la trivia

# Asignamos Constantes con Colores

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
RESET = '\033[39m'

print ("Cargando la Trivia: Esto tomara 3 Segundos\n")
time.sleep(2) # Espera 1 segundos antes de continuar.
print ("3")
time.sleep(1) # Espera 1 segundos antes de continuar.
print ("2")
time.sleep(1) # Espera 1 segundos antes de continuar.
print ("1\n")

time.sleep(1) # Espera 1 segundos antes de continuar.

# Mostramos la pantalla de Bienvenida para quien juegue la trivia
print ("Bienvenido a una trivia sobre mascotas.\nSe pondra a prueba tus conocimientos sobre nuestros amigos peludos.\n")

# Preguntamos el nombre del jugador

nombre = input("Ingresa tu nombre: ")

# Damos las instrucciones sobre como responder las preguntas
print ("\nHola", CYAN + nombre + RESET,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando", MAGENTA + ""'Enter'"" + RESET ,"para enviar tu respuesta:\n")
print ("Por cada respuesta", GREEN + "correcta" + RESET ,"conseguiras 4 puntos, con al menos 12 puntos se te considera", GREEN + "'Aprobado'" + RESET,"aunque respondas", RED + "incorrectamente" + RESET, "no se te descontaran puntos, asi que puedes responder sin temor.\n")

# Creamos la variable donde almacenaremos los puntos

while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntos = 0

  time.sleep(1) # Espera 1 segundos antes de continuar.
  
  print ("La Trivia empezara en 5 Segundos\n")
  
  time.sleep(5) # Espera 1 segundos antes de continuar.

  print(CYAN + "Cantidad de veces que has jugado esta trivia:" + RESET, intentos)
  
  print ("\nMuy bien, comencemos la Trivia!\n")
  
  # Pregunta 1
  print ("Pregunta 1:\n¿Que mascota es conocida como 'el mejor amigo del hombre'?")
  print ("a) Gatos")
  print ("b) Hamsters")
  print ("c) Perros")
  print ("d) Conejos")
  
  # Guardamos la respuesta del jugador en la variable "rpta_1"
  rpta_1 = input("\nTu respuesta: ")
  
  # Nos aseguramos de que el jugador responda de forma correcta
  
  while rpta_1 not in ("a", "b", "c", "d"):
    rpta_1 = input("\nDebes responder con 'a', 'b', 'c' o 'd' en minuscula.\nIngresa nuevamente tu respuesta: ")
  
  # Se le asigna los puntos correspondientes según la respuesta dada
  
  if rpta_1 == "c":
    print(GREEN + "\nRespuesta Correcta!: +4 puntos\n" + RESET)
    puntos = puntos + 4
  else:
    print(RED + "\nRespuesta Incorrecta: +0 puntos\n" + RESET)
  
  # Pregunta 2
  print ("Pregunta 2:\n¿Generalmente en que situación los gatos ronronean?")
  print ("a) Cuando tienen calor")
  print ("b) Cuando están tristes")
  print ("c) Cuando tienen hambre")
  print ("d) Cuando están felices")
  
  # Guardamos la respuesta del jugador en la variable "rpta_2"
  rpta_2 = input("\nTu respuesta: ")
  
  # Nos aseguramos de que el jugador responda de forma correcta
  
  while rpta_2 not in ("a", "b", "c", "d"):
    rpta_2 = input("\nDebes responder con 'a', 'b', 'c' o 'd' en minuscula.\nIngresa nuevamente tu respuesta: ")
  
  # Se le asigna los puntos correspondientes según la respuesta dada
  
  if rpta_2 == "d":
    print(GREEN + "\nRespuesta Correcta!: +4 puntos\n" + RESET)
    puntos = puntos + 4
  else:
    print(RED + "\nRespuesta Incorrecta: +0 puntos\n" + RESET)
  
  
  # Pregunta 3
  print ("Pregunta 3:\n¿Cual de estas mascotas viven más años?")
  print ("a) Tortugas")
  print ("b) Perros")
  print ("c) Gatos")
  print ("d) Loros")
  
  # Guardamos la respuesta del jugador en la variable "rpta_3"
  rpta_3 = input("\nTu respuesta: ")
  
  # Nos aseguramos de que el jugador responda de forma correcta
  
  while rpta_3 not in ("a", "b", "c", "d"):
    rpta_3 = input("\nDebes responder con 'a', 'b', 'c' o 'd' en minuscula.\nIngresa nuevamente tu respuesta: ")
  
  # Se le asigna los puntos correspondientes según la respuesta dada
  
  if rpta_3 == "a":
    print(GREEN + "\nRespuesta Correcta!: +4 puntos\n" + RESET)
    puntos = puntos + 4
  else:
    print(RED + "\nRespuesta Incorrecta: +0 puntos\n" + RESET)
  
  
  # Pregunta 4
  print ("Pregunta 4:\nEn el Antiguo Egipto ¿Cuales de estas mascotas eran adoradas como animales sagrados?")
  print ("a) Cuys")
  print ("b) Gatos")
  print ("c) Conejos")
  print ("d) Perros")
  
  # Guardamos la respuesta del jugador en la variable "rpta_4"
  rpta_4 = input("\nTu respuesta: ")
  
  # Nos aseguramos de que el jugador responda de forma correcta
  
  while rpta_4 not in ("a", "b", "c", "d"):
    rpta_4 = input("\nDebes responder con 'a', 'b', 'c' o 'd' en minuscula.\nIngresa nuevamente tu respuesta: ")
  
  # Se le asigna los puntos correspondientes según la respuesta dada
  
  if rpta_4 == "b":
    print(GREEN + "\nRespuesta Correcta!: +4 puntos\n" + RESET)
    puntos = puntos + 4
  else:
    print(RED + "\nRespuesta Incorrecta: +0 puntos\n" + RESET)
  
  
  # Pregunta 5
  print ("Pregunta 5:\nDe las siguientes mascotas ¿Cual vive menos tiempo?")
  print ("a) Gatos")
  print ("b) Perros")
  print ("c) Conejos")
  print ("d) Tortugas")
  
  # Guardamos la respuesta del jugador en la variable "rpta_5"
  rpta_5 = input("\nTu respuesta: ")
  
  # Nos aseguramos de que el jugador responda de forma correcta
  
  while rpta_5 not in ("a", "b", "c", "d"):
    rpta_5 = input("\nDebes responder con 'a', 'b', 'c' o 'd' en minuscula.\nIngresa nuevamente tu respuesta: ")
  
  # Se le asigna los puntos correspondientes según la respuesta dada
  
  if rpta_5 == "c":
    print(GREEN + "\nRespuesta Correcta!: +4 puntos\n" + RESET)
    puntos = puntos + 4
  else:
    print(RED + "\nRespuesta Incorrecta: +0 puntos\n" + RESET)
  
  print("Jugador:", CYAN + nombre + RESET)
  
  if puntos >= 12:
    print("Puntaje Total:", MAGENTA + str(puntos) ,"puntos" + RESET)
    print("Estado:", GREEN + "Aprobado" + RESET)
    print("Felicidades!")
  else:
    print("Puntos Actuales: ", MAGENTA + str(puntos) ,"puntos" + RESET)
    print("\nDe momento no tienes puntos suficientes para aprobar, si deseas puedes acceder a una ruleta que te puede dar de forma aleatoria desde 0 hasta 12 puntos bonus")
    
    print("Pulsa 'y' si quieres usar la ruleta o pulsa 'n' si no quieres usarla\n")
    rpta_bonus = input ("¿Usaras la Ruletas?: ")
    
    while rpta_bonus not in ("y", "n"):
      rpta_bonus = input("\nDebes responder con 'y' o 'n' en minuscula.\nIngresa nuevamente tu respuesta: ")
  
    if rpta_bonus == "y":
      puntos_bonus = random.randint(0, 12)
      print("\nGirando la Ruleta...")
      print(MAGENTA + "La Ruletas te dio al azar:", puntos_bonus, "puntos!" + RESET, "se agregara a tu puntaje actual\n")
      puntaje_final = puntos + puntos_bonus
      
      print("Jugador:", CYAN + nombre + RESET)
      print("Puntaje Total:", MAGENTA + str(puntaje_final), "puntos" + RESET)
      
      if puntaje_final >= 12:
        print("Estado:", GREEN + "Aprobado" + RESET)
        print("Felicidades!")
      else:
        print("Estado:", RED + "Reprobado" + RESET)
        print("No te preocupes si no aprobaste, puedes reintentar la trivia todas las veces que quieras")
  
  
    else:  
      print("\nJugador:", CYAN + nombre + RESET)
      print("Puntaje Total:", MAGENTA + str(puntos) ,"puntos" + RESET)
      print("Estado:", RED + "Reprobado" + RESET)
      print("No te preocupes si no aprobaste, puedes reintentar la trivia todas las veces que quieras")

  print("\n¿Deseas intentar la trivia nuevamente?")

  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier otro texto para finalizar: ").lower()
  
  if repetir_trivia != "si":  # != significa "distinto"
     print("\nGracias por jugar esta trivia" , CYAN + nombre + RESET ,"espero que lo hayas pasado bien, nos vemos!")
     iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
