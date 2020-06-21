
class NextClass:                            # Define class
    def printer(self, text):                # Define method
        self.message = text                 # Change instance
        print(self.message)                 # Access instance


print('#' * 23 + ' Make instance')
x = NextClass()                         # Make instance

print('#' * 23 + ' Call its method')
x.printer('instance call')              # Call its method

print('#' * 23 + ' Instance changed')
print(x.message)                               # Instance changed

print('#' * 23 + ' Direct class call')
NextClass.printer(x, 'class call')      # Direct class call

print('#' * 23 + ' Instance changed again')
print(x.message)                               # Instance changed again

# NextClass.printer('bad call')
# TypeError: unbound method printer() must be called with NextClass instance...
