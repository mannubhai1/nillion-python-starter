from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    a = SecretInteger(Input(name="my_int1", party=party1))
    b = SecretInteger(Input(name="my_int2", party=party1))

    # write the computation for your program here - use my_int1 and my_int2 as inputs
    # make sure you change the output below to be your new output

    while b != SecretInteger(0):
      temp = b
      b = a % b
      a = temp
    
    # return a
  

    return [Output(a, "my_output", party1)]
