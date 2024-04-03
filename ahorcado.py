import random
import string

from Palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    # Selecciona una palabra al azar de la lista de palabras
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()


def ahorcado():

    print("=================================")
    print("¡Bienvenid@ al juego del ahorcado!")
    print("=================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {''.join(letras_adivinadas)}")

        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        # Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        # Si la letra escogida por el usuario está en el abecedario y no esta en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si letra está en la palabra quitar la letra del conjunto de letras por adivinar. Si no está en la palabra, quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra")
        # Si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print('\nYa escogiste esa letra. Por favor escoge una letra nueva.')
        else:
            print("\nEsta letra no es válida.")
    # El juego llega a esta línea cuando se adivinan todas las letras de la palabra o cuando se agotan las vidas del jugador.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Has palmado! Wasted! La palabra era: {palabra}")
    else:
        print(f"Eres un maquina, has adivinado la palabra")

ahorcado()
