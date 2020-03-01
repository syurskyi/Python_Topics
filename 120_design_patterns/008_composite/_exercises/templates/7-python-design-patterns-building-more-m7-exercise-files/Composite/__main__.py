from datetime import date
from person import Person
from tree import Tree

def main():
    hitchhikers = Tree([
        Person('Trillian', date(1970, 3, 14)),
        Person('Arthur', date(1965, 7, 4)),
        Person('Ford', date(1995, 2, 2)),
        Person('Zaphod', date(1997, 5, 1)),
        Person('Douglas', date(1999, 4, 2))
    ])

    singles = Tree([
        Person('Marvin', date(1991, 1, 1)),
        Person('Slarti', date(1993, 9, 9))
    ])

    loner = Person('Dirk', date(1990, 6, 6))

    tree1 = Tree([hitchhikers])
    tree2 = Tree([singles, loner])
    tree3 = Tree([tree1, tree2])

    for tree in tree1, tree2, tree3:
        oldest = tree.get_oldest()
        max_age = (date.today() - oldest.birthdate).days / 365.2425
        print('Oldest person: {}; Age: {:6.2f}'.format(oldest.name, max_age))

if __name__ == '__main__':
    main()
