# Ejercicio 1.29: Traductor (rustico) al lenguaje inclusivo
# inclusive.py

frase = 'todos somos programadores'
palabras = frase.split()
frase_t = ''
traduccion = []

for palabra in palabras:
    if len(palabra) >= 2 and palabra[-2] == 'o' or palabra[-2] == 'a':
        frase_t = palabra[:-2] + 'e' + palabra[-1]
    elif palabra[-1] == 'o' or palabra[-1] == 'a':
        frase_t = palabra[:-1] + 'e'
    else:
        frase_t = palabra
    traduccion.append(frase_t)
    nueva_frase = ' '.join(traduccion)
    if len(nueva_frase) == len(frase):
        print(nueva_frase)


def lenguaje_inclusivo(palabra):
    if len(palabra) >= 2 and palabra[-2] == 'o' or palabra[-2] == 'a':
        palabra_t = palabra[:-2] + 'e' + palabra[-1]
    elif palabra[-1] == 'o' or palabra[-1] == 'a':
        palabra_t = palabra[:-1] + 'e'
    else:
        palabra_t = palabra
    return palabra_t
