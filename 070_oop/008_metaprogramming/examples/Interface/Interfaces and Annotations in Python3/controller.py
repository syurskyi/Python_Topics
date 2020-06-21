# First version, hard to test

# from renderer import Renderer
# from repository import SQLRepository
#
# class Controller:
#     def __init__(self):
#         self.repository = SQLRepository()
#         self.renderer = Renderer()
#
#     def view_employee(self, id):
#         employee = self.repository.get_employee_by_id(id)
#         res = self.renderer.render_employee(employee)
#         return res

# Same thing, we have a source code dependency between controller.py and repository.py.
#
# Now, let's invert the dependency:
#
# -from repository import SQLRepository
#
#  class Controller:
# -    def __init__(self):
# -        self.repository = SQLRepository()
# +    def __init__(self, repository):
# +        self.repository = repository
#          self.renderer = Renderer()