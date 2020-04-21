____ m.. ______ P..

___ task(n):
    print(n)

___ main():
    with Pool(4) as p:
        print(p.map(task, [2,3,4]))

if __name__ == '__main__':
    main()