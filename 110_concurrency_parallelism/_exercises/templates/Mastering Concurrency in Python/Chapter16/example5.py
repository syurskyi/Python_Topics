# ch16/example5.py

____ network ______ Network
______ th..

___ print_network_primary_value():
    g.. my_network

    print(f'Current primary value: {my_network.get_primary_value()}.')

my_network _ Network('A', 1)
print(f'Initial network: {my_network}')
print()

my_network.add_node('B', 1)
my_network.add_node('C', 1)
print(f'Full network: {my_network}')
print()

thread1 _ ?.T..(target_print_network_primary_value)
thread2 _ ?.T..(target_my_network.refresh_primary)

thread1.s..
thread2.s..

thread1.j..
thread2.j..

print(f'Final network: {my_network}')
print()

print('Finished.')
