#Utilizar la serie de Gregory-Leibniz
#para aproximar el valor de pi tras n iteraciones.

def main():
  #escribe tu código abajo de esta línea
  S=0
  k=0
  n=int(input("Introduzca el número de interaciones: "))
  for k in range(n):
    S=S+(((-1)**k)*(1/((2*k)+1)))
  pi=4*S
  print(pi)
if __name__ == '__main__':
    main()