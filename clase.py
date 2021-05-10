
class conjunto:

   def __init__(self, c = []):
    self.__cos = []
    if len(c) != 0:
     for x in range(0,len(c)):
      self.__cos.append(c[x])
    else:
     a = 0
     print('ingresar elementos del conjunto')
     while a != 'no':
      a = input()
      if a != 'no':
       b = int(a)
      if b in self.__cos:
        print('elemento repetido')
      else:
       self.__cos.append(b)

   def __add__(self, con2):
    con1 = []
    for x in range(0, len(self.__cos)):
     con1.append(self.__cos[x])
    for x in range(0, len(con2.__cos)):
     if not con2.__cos[x] in con1:
       con1.append(con2.__cos[x])
    return conjunto(con1)

   def __sub__(self, con2):
       con1 = []
       for x in range(0, len(self.__cos)):
           if not self.__cos[x] in con2.__cos:
               con1.append(self.__cos[x])
       return conjunto(con1)

   def __eq__(self, con2):
     band = True
     for x in range(0, len(self.__cos)):
         if not self.__cos[x] in con2.__cos:
            band = False

     return band


   def mostrar(self):
    print(self.__cos)