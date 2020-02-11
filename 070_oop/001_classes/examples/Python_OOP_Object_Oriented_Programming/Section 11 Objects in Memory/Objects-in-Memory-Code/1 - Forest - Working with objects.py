from random import randint

class Forest:
    
    def __init__(self, latitude, longitude, code, aprox_num_trees):
        self.latitude = latitude
        self.longitude = longitude
        self.__code = code
        self.aprox_num_trees = aprox_num_trees
        # The list of trees that are being studied
        # is initially empty
        self.trees = []

    def populate_trees(self, num):
        if not isinstance(num, int):
            raise ValueError("Please enter a valid number")
        
        print(f"=== Adding {num} new trees to the forest ===")
        for i in range(num):
            print(f"\n-> Tree #{i+1}")
            tree = self.create_tree()
            self.trees.append(tree)

    def create_tree(self):
        while True:
            try:
                code = str(input("Code of this new tree (sequence of integers):\n"))
                height = int(input("Height of the tree (as an integer):\n"))
                num_rings = int(input("Number of rings of the tree (as an integer):\n"))
            except:
                print("Please try again. Enter a valid value.\n")
            else:
                break

        return Tree(code, height, num_rings)

    def display_trees_data(self):
        print("\n====== Trees in this forest ======")
        for tree in self.trees:
            tree.display_data()


class Tree:

    def __init__(self, code, height, num_rings):
        self.__code = code
        self._height = height
        self._num_rings = num_rings

    def display_data(self):
        print("\n===== Tree =====")
        print("Code:", self.__code)
        print("Height:", self._height)
        print("Number of rings:", self._num_rings)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if 0 < new_height < 100:
            self._height = new_height
        else:
            print("Please enter a valid tree height")

    @property
    def num_rings(self):
        return self._num_rings

    @num_rings.setter
    def num_rings(self, new_num_rings):
        if 0 < new_num_rings < 6000:
            self._num_rings = new_num_rings
        else:
            print("Please enter a valid number of rings")

# Create the instance and call the methods
forest1 = Forest(randint(-90, 90), randint(-180, 180), "453453", 34535)
forest1.populate_trees(2)
forest1.display_trees_data()


            
