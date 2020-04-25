#Importing the necessary modules
______ ___
______ t__

____ ip_file_valid ______ ip_file_valid
____ ip_addr_valid ______ ip_addr_valid
____ ip_reach ______ ip_reach
____ ssh_connection ______ ssh_connection
____ create_threads ______ create_threads

#Saving the list of IP addresses in ip.txt to a variable
ip_list _ ip_file_valid

#Verifying the validity of each IP address in the list
___
    ip_addr_valid(ip_list)
    
______ K..
    print("\n\n* Program aborted by user. Exiting...\n")
    ___.e..

#Verifying the reachability of each IP address in the list
___
    ip_reach(ip_list)
    
______ K..
    print("\n\n* Program aborted by user. Exiting...\n")
    ___.e..

#Calling threads creation function for one or multiple SSH connections
w__ T..:
    create_threads(ip_list, ssh_connection)
    t__.s..(10)

#End of program