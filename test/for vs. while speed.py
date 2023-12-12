import matplotlib.pyplot as plt
import numpy as np
import time

iterations = 1

time_program_1 = np.array([])
time_program_2 = np.array([])

def program():
  time_program_1 = np.array([])
  time_program_2 = np.array([])
  for i in range(iterations):
    start_time = time.time()

    for number in range(1, 1001):
      print(number)

    end_time = time.time()
    execution_time = end_time - start_time
    time_program_1 = np.append(time_program_1, [execution_time])
      
    start_time = time.time()

    counter = 1
    while counter<= 1000:
      print(counter)
      counter += 1

    end_time = time.time()
    execution_time = end_time - start_time
    time_program_2 = np.append(time_program_2, [execution_time])
  return time_program_1, time_program_2

if __name__ == "__main__":
  time_program_1, time_program_2 = program()

  average_1 = np.mean(time_program_1)
  average_2 = np.mean(time_program_2)

  fig, ax = plt.subplots()
  

  ax.plot(np.arange(iterations), time_program_1, marker='o', linestyle='-')
  ax.plot(np.arange(iterations), time_program_2, marker='o', linestyle='-')

  ax.axhline(average_1, color='r', linestyle='--')
  ax.axhline(average_2, color='g', linestyle='--')

  ax.set_title('Missproving Mr. Frank')

  ax.set_xlabel('Iterations')
  ax.set_ylabel('Seconds')
  
  print(f"Durchchnitt for  : {average_1}")
  print(f"Durchchnitt while: {average_2}")

  plt.show()

