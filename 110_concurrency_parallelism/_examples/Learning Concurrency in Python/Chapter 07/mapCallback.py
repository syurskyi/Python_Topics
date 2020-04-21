______ ti..
____ c__.f.. ______ TPE..
____ c__.f.. ______ a_c..

values = [2,3,4,5,6,7,8]

___ multiplyByTwo(n):
  return 2 * n

___ done():
  print("Task Done")

___ main():
  with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(multiplyByTwo, values)

    for result in results:
      print(result)

if __name__ == '__main__':
  main()