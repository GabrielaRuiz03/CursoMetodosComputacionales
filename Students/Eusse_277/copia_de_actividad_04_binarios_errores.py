# -*- coding: utf-8 -*-
"""Actividad_04_Binarios_Errores.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3HzQzBoTP_mZqAfjGuRS7x0G09Pzvxg

<a href="https://colab.research.google.com/github/hernansalinas/autogrades/blob/main/Actividades_clase/Actividad_04_Binarios_Errores.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>



# Actividad 4
### Métodos computacionales para físicos  y astrónomos
### Universidad de Antioquia
### Prof: Hernan D. Salinas Jiménez
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/hernansalinas/autogrades.git
#path="libs"
path="autogrades/Actividades_clase/libs"
# %run -i {path}/libUnitTest.py

"""### Activity 1.0: 

Implement a function that get the binary representation of an integer with name mybin, the algorithm should return 
a string with 8 characters, the maximun number that represent the funcition is integer of 8 bit. The name of function is 
mybin

Ejexample : 

b=mybin(x)

b='00101000'
"""

def mybin(n):
  entero = n
  lista=[]
  while True:

    if entero==1:
      lista.append(str(entero))
      break
    elif entero>3:
      cosiente= entero//2
      res = entero%2
      entero= cosiente
      lista.append(str(res))
    elif entero==2:
      res= entero%2
      lista.append(str(res))
      lista.append(str(entero//2))
      break
    elif  entero==3:
      res=entero%2
      lista.append(str(res))
      lista.append(str(entero//2)) 
      break
  
  lista.reverse()
  binary_string = ''.join(lista)
  while len(binary_string) < 8:
        binary_string = '0' + binary_string
    
    # Truncar la cadena a ocho caracteres si es mayor a ocho
  if len(binary_string) > 8:
        binary_string = binary_string[:8]
    
  return binary_string
  
print(mybin(1))

##!/usr/bin/env python3
def mybin(x):
    print('__name__ = {}'.format(__name__))
   # Write your code here and change the next line as required
    return "111"

# Commented out IPython magic to ensure Python compatibility.
# %run -i {path}/Act_02/test01.py

"""### Activity 2.0: 

With the binary representation please try to implement the formula to recover the number.

Hint: Use as input the binary representation as a string and invert its order

```
number32(BIN):

```

Where BIN is a string with the binary number

Example: 


Test your solution for the next number:

number32("00111110001000000000001000010000")
"""

import numpy as np

def number32(BIN):


  BIN= np.array(list(BIN)[::-1]).astype(int)
  s= BIN[31]
  b_expo=BIN[23:31]
  i= np.arange(b_expo.size)
  e= (b_expo*(2**i)).sum()
  b_fra=BIN[0:23]
  i_inver= np.arange(1,b_fra.size+1)[::-1]


  numero= ( (-1)**s/2**(127-e) )*( 1+ (b_fra/2**i_inver).sum() )

  return numero

b="00111110001000000000001000010000"
number32("00111110001000000000001000010000")

# Commented out IPython magic to ensure Python compatibility.
# %run -i {path}/Act_02/test02.py

"""### Activity 3.0:
1. Write a python script that calculates the double precision number represented by a 64-bits binary.

the name of function should be: 
```
number64(BIN):

```

2. What is the number represented by:

BIN="0 10000000011 1011100100001111111111111111111111111111111111111111"
"""

def number64(BIN):

  bin= np.array(list(BIN)[::-1]).astype(int)
  s=bin[63]
  bin_exp= bin[52:63]
  i=np.arange(bin_exp.size)
  e= ( bin_exp*(2**i) ).sum()
  bin_fra=bin[0:52]
  i_inv= np.arange(1,bin_fra.size+1)#[::-1]

  numero = ((-1)**s)*( 1+ (bin_fra/(2**i_inv)).sum() )*(2**(e-1023))

  return numero

BIN="0100000000111011100100001111111111111111111111111111111111111111"
number64(BIN)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {path}/Act_02/test03.py
