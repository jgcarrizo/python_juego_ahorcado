import random

def obtener_palabra() -> str:
    palabras = ["casa", "auto", "televisor", "reptil", "limonero"]
    return random.choice(palabras)


#Obtenemos como parametro  palabra_secreta y letras adivinadas de la
#funcion juego_ahorcado
def mostrar_avance(palabra_secreta, letras_adivinadas):
    adivinado = '' #Comienza vacio

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra  #Si esta, le agrego la letra adivinada
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra() #Llamo a funcion donde guardo la lista de las palabras
    letras_adivinadas = [] #Lista vacia, donde vamos rellenando las letras adivinadas
    intentos = 6
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_avance(palabra_secreta, letras_adivinadas), "La cantidad de letras de la palabra es: ",len(palabra_secreta)) #llamamos a la funcion para ver el progreso

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower() #aseguramos que sea en miniscula

        if len(adivinanza) != 1 or not adivinanza.isalpha(): #Nos aseguramos que sea 1 letra
            print("Por favor, introduce una letra válida.")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba otra.")
        else:
            letras_adivinadas.append(adivinanza) #Vamos agregando las letras adivinadas a la lista

            if adivinanza in palabra_secreta:
                print(f"¡Has acertado! La letra '{adivinanza}' está presente en la palabra.")
            else:
                intentos -= 1
                print("La letra no se encuentra en la palabra.")
                print(f"Te quedan {intentos} intentos.")

        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        print("......")

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Has ganado! La palabra correcta es: {palabra_secreta}")
    
    if intentos == 0:
        print(f"Se te han acabado los intentos. La palabra correcta era {palabra_secreta.upper()}.")

juego_ahorcado()