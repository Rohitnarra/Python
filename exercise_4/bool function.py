def divisible(numerator: int, denominator: int)->bool:
#values for numreator and denominator are integers
 return numerator % denominator == 0
print(divisible(30,4))
#30 is not divisible by 4 so, the output is false.