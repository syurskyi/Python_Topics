______ lo..
____ m.. ______ P..

______.basicConfig(filename='myapp.log', level=______.INFO,
  format='%(processName)-10s %(asctime)%s %(levelname)s %(message)s')

___ myTask(n):
  ______.info("{} being processed".format(n))
  ______.info("Final Result: {}".format(n*2))
  return n*2

___ main():
  with Pool(4) as p:
    p.map(myTask, [2,3,4,5,6,])

if __name__ == '__main__':
  main()