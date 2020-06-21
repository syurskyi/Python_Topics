from cars.economy import Economy

def main():
    car1 = Economy('4 cyl', 'black', 'vinyl')
    car2 = Economy('6 cyl', 'red', 'leather')

    print('{}: ${}'.format(car1.description, car1.cost))
    print('{}: ${}'.format(car2.description, car2.cost))

if __name__ == '__main__':
    main()
