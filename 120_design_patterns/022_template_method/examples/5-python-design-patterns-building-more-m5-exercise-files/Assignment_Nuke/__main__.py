from bread import Bread
from cake import Cake

def main():
    print('Making a baguette:')
    Bread('baguette').bake_product()
    print('Baking a cake:')
    Cake('chocolate cake').bake_product()

main()
