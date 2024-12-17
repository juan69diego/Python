import math
print("Deseas calcular el area de un tringulo por sus lados?")
pregunta = input()

def areaDeUnTriangulo_lados(lado1,lado2,lado3):
    p= (lado1 + lado2 + lado3)/2
    return math.sqrt(p*(p-lado1)*(p-lado2)*(p-lado3))



if pregunta =='si':
    l1 = input('lado 1: ')
    l2 = input('lado 2: ')
    l3 = input('lado 3: ')
    print('el lado de el triangulo es: ', (areaDeUnTriangulo_lados(float(l1),float(l2),float(l3))))
elif pregunta == 'No':
    print('Que tengas un buen dia')
else:
    print('Responde Si o No')
    

 