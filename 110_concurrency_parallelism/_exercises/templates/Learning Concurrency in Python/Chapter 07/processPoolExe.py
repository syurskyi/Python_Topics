____ c__.f.. ______ PPE..

___ task(n):
  print("Processing {}".format(n))

___ main():
  print("Starting ThreadPoolExecutor")
  with ProcessPoolExecutor(max_workers=3) as executor:
    future = executor.submit(task, (2))
    future = executor.submit(task, (3))
    future = executor.submit(task, (4))
    
  print("All tasks complete")
    
if __name__ == '__main__':
  main()