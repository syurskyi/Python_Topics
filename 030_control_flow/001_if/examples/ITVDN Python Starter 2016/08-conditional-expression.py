is_ready = True

# То же самое, что и в предыдущем примере, но используем
# условное выражение вместо условного оператора
state_msg = 'Ready' if is_ready else 'Not ready yet'
print(state_msg)