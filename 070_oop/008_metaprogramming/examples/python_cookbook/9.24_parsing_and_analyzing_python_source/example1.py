import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)

# Sample usage
if __name__ == '__main__':
    # Some python code
    code = '''
for i in range(10): 
    print(i)
del i
'''
    # Parse into an AST
    top = ast.parse(code, mode='exec')

    # Feed the AST to analyze name usage
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)

# Problem
# You want to write programs that parse and analyze Python source code.
# Solution
# Most programmers know that Python can evaluate or execute source code provided in
# the form of a string. For example:

# However, the ast module can be used to compile Python source code into an abstract
# syntax tree (AST) that can be analyzed. For example:

# Analyzing the source tree requires a bit of study on your part, but it consists of a collection
# of AST nodes. The easiest way to work with these nodes is to define a visitor
# class that implements various visit_NodeName() methods where NodeName() matches
# the node of interest. Here is an example of such a class that records information about
# which names are loaded, stored, and deleted.

# Discussion
# The fact that you can analyze source code and get information from it could be the start
# of writing various code analysis, optimization, or verification tools. For instance, instead
# of just blindly passing some fragment of code into a function like exec(), you could
# turn it into an AST first and look at it in some detail to see what it’s doing. You could
# also write tools that look at the entire source code for a module and perform some sort
# of static analysis over it.
# It should be noted that it is also possible to rewrite the AST to represent new code if you
# really know what you’re doing. Here is an example of a decorator that lowers globally
# accessed names into the body of a function by reparsing the function body’s source code,
# rewriting the AST, and recreating the function’s code object:

# In a performance test, it makes the function run about 20% faster.
# Now, should you go applying this decorator to all of your functions? Probably not.
# However, it’s a good illustration of some very advanced things that might be possible
# through AST manipulation, source code manipulation, and other techniques.
# This recipe was inspired by a similar recipe at ActiveState that worked by manipulating
# Python’s byte code. Working with the AST is a higher-level approach that might be a bit
# more straightforward. See the next recipe for more information about byte code.
