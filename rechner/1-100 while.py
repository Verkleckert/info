import time

start_time = time.time()

counter = 1
while counter<= 100:
  print(counter)
  counter += 1

end_time = time.time()

execution_time = end_time - start_time
print(f"Die Ausführung des Programms hat {execution_time} Sekunden gedauert.")