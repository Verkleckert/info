import numpy as np

class Compiler:
  def __init__(self) -> None:
    pass
  
  def bin2dec(self, input_number) -> int:
    input_number = "0b" + str(input_number)
    output = int(input_number, 2)
    return output
  
  def dec2bin(self, input_number) -> int:
    output = bin(input_number)
    return output



class Processor:
  def __init__(self) -> None:
    pass

  def add() -> int:
    pass
  
  def subtract() -> int:
    pass
  
  def multiply() -> int:
    pass
  
  def divide() -> int:
    pass



    
if __name__ == "__main__":
  compiler = Compiler()
  print(compiler.bin2dec(10101010001010))
  print(compiler.bin2dec(1100))
  print(compiler.dec2bin(65))
