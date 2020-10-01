products _ {"Grape":5.9, "Guava": 4.5,
            "Mango":4.8, "Cashew":2.4,
            "Banana":3.0, "Pear": 5.8}

___ pro, price __ products.i..
    print(pro, " = ", price)
cost _ 0
w___ T..:
    pro _ i..("Select product (n=nothing): ")
    __ pro __ 'n':
        b..
    qty _ in.(i..("Number of product? "))
    cost +_ products[pro]*qty

print("Price of product(s): ",cost)