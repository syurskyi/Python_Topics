is_ready = True

# Присваиваем значение переменной в зависимости от условия
if is_ready:
    state_msg = 'Ready'
else:
    state_msg = 'Not ready yet'

print(state_msg)