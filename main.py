# Primero mostramos la pantalla de Bienvenida para quien juegue la trivia
print ("Bienvenido a una trivia sobre mascotas.\nSe pondra a prueba tus conocimientos sobre nuestros amigos peludos.\n")

# Preguntamos el nombre del jugador

nombre = input("Ingresa tu nombre: ")

# Damos las instrucciones sobre como responder las preguntas
print ("\nHola",nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
print ("Por cada respuesta correcta conseguiras 4 puntos, con al menos 12 puntos se te considera 'Aprobado', aunque respondas incorrectamente no se te descontaran puntos, asi que puedes responder sin temor.\n")

# Creamos la variable donde almacenaremos los puntos

puntos = 0

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
  print("\nRespuesta Correcta! +4 puntos\n")
  puntos = puntos + 4
else:
  print("\nRespuesta Incorrecta +0 puntos\n")

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
  print("\nRespuesta Correcta! +4 puntos\n")
  puntos = puntos + 4
else:
  print("\nRespuesta Incorrecta +0 puntos\n")


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
  print("\nRespuesta Correcta! +4 puntos\n")
  puntos = puntos + 4
else:
  print("\nRespuesta Incorrecta +0 puntos\n")


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
  print("\nRespuesta Correcta! +4 puntos\n")
  puntos = puntos + 4
else:
  print("\nRespuesta Incorrecta +0 puntos\n")


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
  print("\nRespuesta Correcta! +4 puntos\n")
  puntos = puntos + 4
else:
  print("\nRespuesta Incorrecta +0 puntos\n")

print("Jugador:", nombre)
print("Puntaje Total:", puntos, "puntos")
if puntos >= 12:
  print("Estado: Aprobado")
  print("Felicidades! Espero que hayas disfrutado esta pequeña trivia")
else:
  print("Estado: Reprobado")
  print("No te preocupes si no aprobaste, puedes reintentar la trivia todas las veces que quieras")