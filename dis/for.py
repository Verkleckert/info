import dis
import sys
from io import StringIO  

def program_for():
    for number in range(1, 1001):
      print(number)

def program_while():
  counter = 1
  while counter<= 1000:
    print(counter)
    counter += 1
    

out = StringIO()
stdout = sys.stdout
sys.stdout = out
try:
    dis.dis(program_for)
finally:
    sys.stdout = stdout
out = out.getvalue()

f = open("./dis/forcode.txt", "w")
f.write(str(out))
f.close()


out = StringIO()
stdout = sys.stdout
sys.stdout = out
try:
    dis.dis(program_while)
finally:
    sys.stdout = stdout
out = out.getvalue()

f = open("./dis/whilecode.txt", "w")
f.write(str(out))
f.close()