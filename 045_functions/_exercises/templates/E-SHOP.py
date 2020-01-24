# This is an E-SHOP
from getpass import getpass


def invalid_name(list, element_name):
    global name_dic
    for dic in list:
        try:
            if dic['user_name'] == element_name:
                name_dic = dic
                return True
        except:
            if dic['product_name'] == element_name:
                return True
    return False


def print_elements_names(list):
    for dic in list:
        try:
            print('\t' + dic['user_name'])
        except:
            print('\t' + dic['product_name'])


def add_user():
    global logged_user
    if admin_previliges:
        user_name = input('Enter the user_name (b: return to the menu): ')
        if user_name == 'b':
            return admin_menu()
    else:
        user_name = input('Please enter a user name: ')
    while invalid_name(users, user_name):
        user_name = input('user_name already exists, Enter a new user_name: ')
    password = getpass('Enter the password: ')
    logged_user = len(users)
    users.append({
        'user_id': len(users),
        'user_name': user_name,
        'password': password,
        'products': []
    })
    if admin_previliges:
        admin_menu()
    else:
        user_menu()


def remove_user():
    print('This is the users list: ')
    print_elements_names(users)
    user_name = input('Enter the user name that you want to remove(b: return to the menu): ')
    if user_name == 'b':
        return admin_menu()
    remove_id = None
    for user in users:
        if user['user_name'] == user_name:
            remove_id = user['user_id']
            print(user)
            break
    if remove_id is None:
        print('\nThere is no such user name')
    else:
        answer = input('Are you sure that you want to remove ' + str(user_name) + ' (y:Yes/n:No): ').lower()
        if answer == 'y':
            del users[remove_id]
    admin_menu()


def add_product():
    product_name = input('Enter product_name(b: return to the menu): ')
    if product_name == 'b':
        return admin_menu()
    if invalid_name(products, product_name):
        answer = input('product name already exists, do you want to increase the quantity,'
                       ' or choose \nan other name(i: increase the quantity/c: choose an other '
                       'name): ').lower()
        if answer == 'c':
            return admin_menu()
        elif answer == 'i':
            quantity_to_add = int(input('How much units to add?: '))
            name_dic['product_quantity'] += quantity_to_add
            return admin_menu()
        else:
            print('wrong answer!')
            add_product()
    product_price = int(input('Enter product_price: '))
    product_quantity = int(input('Enter product quantity: '))
    products.append({'product_id': len(products),
                     'product_name': product_name + '                  ',
                     # You will understand why I have added the white spaces at the end
                     # in the last video of this chapter
                     'product_price': product_price,
                     'product_quantity': product_quantity
                     })
    admin_menu()


def remove_product():
    print('This is the products list: ')
    print_elements_names(products)
    product_name = input('Enter the product name that you want to remove(b: return to the menu): ')
    if product_name == 'b':
        return admin_menu()
    remove_id = None
    for product in products:
        if product['product_name'].strip() == product_name:
            # We will need the white spaces in the last video of the section, but we don't need
            # them in comparision, just please wait till the last video of the section and you will
            # Understand
            remove_id = product['product_id']
            print(product)
            break
    if remove_id is None:
        print('\nThere is no such product name')
    else:
        answer = input('Are you sure that you want to remove ' + str(product_name) + ' (y:Yes/n:No): ').lower()
        if answer == 'y':
            del products[remove_id]
    admin_menu()


def check_lists(list):
    i = 1
    for dic in list:
        print('(' + str(i) + ') ', dic)
        i += 1


def check_users():
    check_lists(users)
    admin_menu()


def check_products():
    check_lists(products)
    admin_menu()


def finish():
    print("Thanks for choosing us!")
    quit()


def admin_menu():
    task_number = input('_______________________________\n(1)Add a user \n'
                        '(2)Remove a user\n'
                        '(3)Add a product\n'
                        '(4)Remove a product\n'
                        '(5)Check users\n'
                        '(6)Check products\n'
                        '(7)Quit\n'
                        'Please choose an operation: ')
    while int(task_number) not in range(1, 8):
        task_number = input('Incorrect operation, Enter an other number: ')
    return {
        '1': add_user,
        '2': remove_user,
        '3': add_product,
        '4': remove_product,
        '5': check_users,
        '6': check_products,
        '7': quit,
    }[task_number]()


def shopping():
    i = 0
    print('Products list:')
    for product in products:
        print('(' + str(i) + ')', product['product_name'], str(product['product_price']) + '$',
              str(product['product_quantity']) + 'u')
        i += 1
    product_number = int(input('Enter the product number that you want to add to your cart'
                               '(-1: return to the menu): '))
    if product_number == -1:
        return user_menu()
    if product_number in range(0, len(products)):
        users[logged_user]['products'].append(products[product_number])
        products[product_number]['product_quantity'] -= 1
    else:
        print("The number choosed doesn't exist in the products list")
        shopping()
    user_menu()


def check_cart():
    try:
        sum = 0
        i = 0
        for product in users[logged_user]['products']:
            print('(' + str(i) + ')', product['product_name'], '\t', str(product['product_price']) + '$')
            sum += product['product_price']
            i += 1
        print('\n\tThe sum is:', str(sum) + '$', end='\n___________________________________________________________\n')
    except:
        print('Your cart is empty', end='\n___________________________________________________________\n')
    user_menu()


def remove_product_from_cart():
    try:
        i = 0
        for product in users[logged_user]['products']:
            print('(' + str(i) + ')', product['product_name'], '\t', product['product_price'], "$")
            i += 1
    except:
        print('You cart is empty', end='\n___________________________________________________________\n')
        return user_menu()
    product_to_remove = int(input('Please enter the number of the product that you want to remove: '))
    if product_to_remove in range(0, len(users[logged_user]['products'])):
        answer = input('Are you sure that you want to remove '
                       + users[logged_user]['products'][product_to_remove]['product_name'].strip()
                       + '(y:Yes/n:No): ').lower()
        if answer == 'y':
            users[logged_user]['products'][product_to_remove]['product_quantity'] += 1
            del users[logged_user]['products'][product_to_remove]

        else:
            return user_menu()
    else:
        print("Product number choosed doesn't exist in your cart")
    return user_menu()


def user_menu():
    answer = input('\t(1)Shopping\n'
                   '\t(2)check your cart\n'
                   '\t(3)Remove a product from the cart\n'
                   '\t(4)Finish\n'
                   'Please choose an operation: ')
    while int(answer) not in range(1, 5):
        answer = input('\t(1)Shopping\n'
                       '\t(2)check your cart\n'
                       '\t(3)Remove a product from the cart\n'
                       '\t(4)Finish\n'
                       'Please choose an operation: ')
    return {
        '1': shopping,
        '2': check_cart,
        '3': remove_product_from_cart,
        '4': finish
    }[answer]()


products = [{
    'product_id': 0,
    'product_name': 'Adidas Shoes                 ',
    'product_price': 100,
    'product_quantity': 50,
},
    {
        'product_id': 1,
        'product_name': 'Nike T-shirt                 ',
        'product_price': 30,
        'product_quantity': 150,
    },
    {
        'product_id': 2,
        'product_name': 'Hat                          ',
        'product_price': 25,
        'product_quantity': 30,
    },
    {
        'product_id': 3,
        'product_name': 'Jeans pants                  ',
        'product_price': 60,
        'product_quantity': 55,
    }]
users = [{
    'user_id': 0,
    'user_name': 'admin',
    'password': 'admin1234'
},
    {
        'user_id': 1,
        'user_name': 'Jimmy',
        'password': 'Jimmy1234',
        'products': [products[0], products[3]]
    },
    {
        'user_id': 2,
        'user_name': 'John',
        'password': 'John1234',
        'products': [products[1], products[2]]
    }]

name_dic = None
logged_user = None
admin_previliges = False
tries = 5
answer = input('(1) Register \n(2) Sign in \nPlease choose an option: ')
while int(answer) not in range(1, 3):
    answer = input('(1) Register \n(2) Sign in \nPlease chose an option: ')
if answer == '1':
    add_user()
elif answer == '2':
    while tries > 0:
        user_name = input('Please enter your name: ')
        user_password = getpass('Please enter your password: ')
        for user in users:
            if user_name == user['user_name'] and user_password == user['password']:
                print('Hello', user_name, '!')
                logged_user = user['user_id']
                tries = -1
                break
        if tries != -1:
            print('The information entered are incorrect')  # The information entered by the user are false
            tries -= 1
        if tries == 0:
            print('You have passed 5 tries!')
            quit()
if user_name == 'admin':
    admin_previliges = True
    admin_menu()
else:
    user_menu()
