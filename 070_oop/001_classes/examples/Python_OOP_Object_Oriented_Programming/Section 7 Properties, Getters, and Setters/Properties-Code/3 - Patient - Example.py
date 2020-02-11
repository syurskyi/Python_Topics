class Patient:
    
    def __init__(self, name, age, id_num, num_children=0):
        self.name = name
        self.age = age
        self._id_num = id_num
        self._num_children = num_children

    def get_id_num(self):
        return self._id_num

    def set_id_num(self, new_id):
        if isinstance(new_id, str):
            self._id_num = new_id
        else:
            print("Please enter a valid id")

    def get_num_children(self):
        return self._num_children

    def set_num_children(self, num_children):
        if isinstance(num_children, int) and 0 < num_children < 70:
            self._num_children = num_children
        else:
            print("Please enter a valid number of children")
        

        
