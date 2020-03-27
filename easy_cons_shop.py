from getpass import getpass

def invalid_name(list, element):
    global name_dic
    for dic in list:
        try:
            if(dic['user_name'] == element):
                return True
        except:
            if (dic['product_name'] == element):
                name_dict = dic
                return True
    return False
def add_user():
    global logged_user
    if admin_privileges:
        user_name = input('Enter the user name (b: return to the menu): ')
        if user_name == 'b':
            return admin_menu()
    else:
        user_name = input('Please enter the user_name: ')
    while invalid_name(users, user_name):
        user_name = input('user name already exists enter a new: ')
    password = getpass('Enter the password')
    logged_user = len(users)
    users.append({
        'user_id': len(users),
        'user_name': user_name,
        'password': password,
        'Products': []
    })
    if admin_privileges:
         admin_menu()
    else:
        user_menu()
def print_elements_names(list):
    for dic in list:
        try:
            print('\t'+dic['user_name'])
        except:
            print('\t'+dic['product_name'])
def remove_user():

    print('This is the users list')
    print_elements_names(users)
    user_name = input('Enter the user_name you want to remove (b: back to menu): ')
    if user_name == 'b':
        return admin_menu()
    remove_id = None
    for user in users:
        if user['user_name'] == user_name:
            remove_id = user['user_id']
            print(user)
            break
    if remove_id is None:
        print('\nThere is no such user_name')
    else:
        answer = input('Do you really want to remove ' + str(user_name) + ' (y/n)?: ').lower()
        if answer == 'y':
            del users[remove_id]
    admin_menu()
def add_product():
    ''''''
    product_name = input('Enter product_name(b: return to the menu): ')
    if product_name == 'b':
        return admin_menu()
    if invalid_name(products, product_name):
        answer = input('product_name already exists, do you want to increase the quantity, or choose '
                       'and other name?(i: increase the quantity/ c: choose an other name):  ').lower()
        if answer == 'c':
            return admin_menu()
        elif answer == 'i':
            quantity_to_add = int(input('How much units to add?:  '))
            name_dic['product_quantity'] += quantity_to_add
            return admin_menu()
        else:
            print('Wrong answer')
            add_product()
    product_price = int(input('Enter the product price: '))
    product_quantity = int(input('Enter product quantity: '))
    products.append({
        'product_id': len(products),
        'product_name': product_name,
        'product_price': product_price,
        'product_quantity': product_quantity
    })
    admin_menu()
def remove_product():
    print('This products list: ')
    print_elements_names(products)
    product_name = input('Enter the product name(b: return to the menu): ')
    if product_name == 'b':
        return admin_menu()
    remove_id = None
    for product in products:
        if product['product_name'] == product_name:
            remove_id = product['product_id']
            print(product)
            break
    if remove_id is None:
        print('\nThere is no such product_name')
    else:
        answer = input('Are you sure that you want to remove this '+str(product_name) + ' y/n').lower()
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
def check_prod():
    check_lists(products)
    admin_menu()
def admin_menu():
    task_num = input('(1) Add a user.\n(2) Remove a user'
                      '\n(3) Add a product. \n(4) Remove a product\n5) Check users\n'
                      '(6)Check products\n(7)Quit\nPlease choose the number')
    while int(task_num) not in range(1, 8):
        task_num = input('Incorrect operation, try again: ')
    return {
        '1': add_user,
        '2': remove_user,
        '3': add_product,
        '4': remove_product,
        '5': check_users,
        '6': check_prod,
        '7': quit,
    }[task_num]()
def shopping():
    i = 0
    print('Products list:')
    for product in products:
        print('(' + str(i) + ')', product['product_name'], '\t', str(product['product_price']) + '$',
              '\t', str(product['product_quantity']) + 'u')
        i += 1
        product_number = int(input('Enter the product number that you want to add to your cart'
                                   '(-1: return to the menu: '))
        if product_number == -1:
            return user_menu()
        if product_number in range(0, len(products)):
            users[logged_user]['Products'].append(products[product_number])
            products[product_number]['product_quantity'] -= 1
        else:
            print('The number chase does not exist in the products list')
            shopping()
        user_menu()
def check_cart():
    try:
        sum = 0
        i = 0
        for product in users[logged_user]['Product']:
            print('(' + str(i) + ')', product['product_name'], '\t', str(product['product_price']) + '$')
            sum += product['product_price']
            i += 1
        print('\n\tThe sum is: ', str(sum) + '$')
    except:
        print('Your cart is empty')
    user_menu()
def remove_product_from_cart():
    try:
        i = 0
        for product in users[logged_user]['Products']:
            print('(' + str(i) + ')', product['product_name'], '\t', product['product_price'])
            i += 1
    except:
        print('Your cart is empty')
        return user_menu()
    product_to_remove = int(input('Please enter the number of the product that you want to remove: '))
    if product_to_remove in range(0, len(users[logged_user]['Products'])):
        answer = input('Are you sure that you want to remove' + users[logged_user]['Products'][product_to_remove]['product_name']
                       + '(y/n): ').lower()
        if answer == 'y':
            users[logged_user]['Products'][product_to_remove]['product_quantity'] += 1
            del users[logged_user]['Products'][product_to_remove]
        else:
            return user_menu()
    else:
        print('Product number chase does not exists in your cart')
    return user_menu()
def finish():
    print('Thanks  for choosing us')
    quit()
def user_menu():
    answer = input('\t(1) Shopping.\n\t(2) Check your cart. \n\t(3)Remove a product from the cart\n\t'
                   '(4)Finish \nPlease choose the number: \n')
    while int(answer) not in range(0, 5):
        answer = input('\t(1) Shopping.\n\t(2) Check your cart. \n\t(3)Remove a product from the cart\n\t'
                       '(4)Finish \nPlease choose the number: \n')
    return {
        '1': shopping,
        '2': check_cart,
        '3': remove_product_from_cart,
        '4': finish
    }[answer]()


products = [{
    'product_id':1,
    'product_name': 'Adidas Shoes',
    'product_price': 100,
    'product_quantity': 50
},
    {
    'product_id':2,
    'product_name': 'Nike T-Shirt',
    'product_price': 30,
    'product_quantity': 150
},
    {
    'product_name': 'Hat',
    'product_price': 25,
    'product_quantity': 30
},
    {
    'product_id':3,
    'product_name': 'Jeans pants',
    'product_price': 60,
    'product_quantity': 55
}
]
users = [
    {
        'user_id': 0,
        'user_name': 'admin',
        'password': 'admin1234',
    },
{
         'user_id': 1,
         'user_name': 'Jimmy',
         'password': 'Jimmy12',
         'Products': [products[0], products[3]]
    },
{
          'user_id': 2,
          'user_name': 'John',
          'password': 'John12',
          'Products': [products[1], products[3]]
    }
]

name_dic = None
tries = 5
logged_user = None
admin_privileges = False

answer = input('(1) Register\n(2) Sign in\nPlease choose an option: ')
while int(answer) not in range(1, 3):
    answer = input('(1) Register\n(2) Sign in\nPlease choose an option: ')
if answer == '1':
    add_user()
elif answer == '2':
    while tries > 0:
        user_name = input('Please enter your name: ')
        user_password = getpass('Please enter your password: ')
        for user in users:
            if user_name == user['user_name'] and user_password == user['user_password']:
                print('Hello', user_name)
                logged_user = user['user_id']
                tries = -1
                break
        if tries != -1:
            print('Incorrect information')
            tries -= 1
        if tries == 0:
            print('You have lost 5 tries')
            quit()
if user_name == 'admin':
    admin_privileges = True
    admin_menu()
else:
    user_menu()
