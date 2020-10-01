___ fibonacci(list_item):
    f1 _ f2 _ 1
    print(f1, f2, end_' ')
    w___ list_item > 2:
        num _ f2
        f2 _ f1 + f2
        f1 _ num
        print(f2, end_' ')
        list_item -_ 1
    print()

x _ in.(i..("Insert range of Fibonacci sequence: "))
fibonacci(x)