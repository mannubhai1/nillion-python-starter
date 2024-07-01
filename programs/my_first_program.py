from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    height_m = SecretInteger(Input(name="my_int1", party=party1))
    weight_kg = SecretInteger(Input(name="my_int2", party=party1))

    # write the computation for your program here - use my_int1 and my_int2 as inputs
    # make sure you change the output below to be your new output

    height_squared = height_m * height_m
    bmi = weight_kg / height_squared
    
    # return bmi
  

    return [Output(bmi, "my_output", party1)]
