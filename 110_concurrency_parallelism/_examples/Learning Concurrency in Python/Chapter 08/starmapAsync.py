____ m.. ______ P..
______ ti..

___ myTask(x, y):
  time.sleep(x)
  return y*2

___ main():
  with Pool(4) as p:
     print(p.starmap_async(myTask, [(4,3),(2,1)]).get())

if __name__ == '__main__':
  main()
