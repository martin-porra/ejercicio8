from clase import  conjunto
import os
def menu():
 os.system('cls') # NOTA para windows tienes que cambiar clear por cls
 print ("Selecciona una opción")
 print ("\t1 - unir conjuntos")
 print ("\t2 - diferencia de conjuntos")
 print ("\t3 - chekear igualdad de conjuntos")

if __name__ == '__main__':
 a = conjunto()
 b = conjunto()
 a.mostrar()
 b.mostrar()
 l = True
 while l == True:
  menu()
  opcion = input()
  if opcion == '1':
   v = a.__add__(b)
   v.mostrar()
  elif opcion == '2':
   m = a.__sub__(b)
   m.mostrar()
  elif opcion == '3':
   if a.__eq__(b) == True:
    print('son iguales')
   else:
    print('son distintos')
  else:
   l = False
   print('opcion incorrecta')
 print('programa terminado')



