______ pa..
______ d_t_
______ __.pa__
______ t__
______ ___
______ __

#Checking username/password file
#Prompting user for input - USERNAME/PASSWORD FILE
user_file _ in__("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

#Verifying the validity of the USERNAME/PASSWORD file
__ __.pa__.i_f..(user_file) __ T..:
    print("\n* Username/password file is valid :)\n")

____
    print("\n* File @ does not exist :( Please check and try again.\n".f..(user_file))
    ___.e..
        
#Checking commands file
#Prompting user for input - COMMANDS FILE
cmd_file _ in__("\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

#Verifying the validity of the COMMANDS FILE
__ __.pa__.i_f..(cmd_file) __ T..:
    print("\n* Command file is valid :)\n")

____
    print("\n* File @ does not exist :( Please check and try again.\n".f..(cmd_file))
    ___.e..
    
#Open SSHv2 connection to the device
___ ssh_connection(ip
    
    g.. user_file
    g.. cmd_file
    
    #Creating SSH CONNECTION
    ___
        #Define SSH parameters
        selected_user_file _ o..(user_file, _)
        
        #Starting from the beginning of the file
        selected_user_file.s..(0)
        
        #Reading the username from the file
        username _ selected_user_file.r_l..[0].sp..(',')[0].rs..("\n")
        
        #Starting from the beginning of the file
        selected_user_file.s..(0)
        
        #Reading the password from the file
        p__swor. _ selected_user_file.r_l..[0].sp..(',')[1].rs..("\n")
        
        #Logging into device
        session _ ?.SSHClient
        
        #For testing purposes, this allows auto-accepting unknown host keys
        #Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(?.AutoAddPolicy)
        
        #Connect to the device using username and password          
        session.c..(ip.rs..("\n"), username _ username, p__swor. _ p__swor.)
        
        #Start an interactive shell session on the router
        connection _ session.invoke_shell
        
        #Setting terminal length for entire output - disable pagination
        connection.s..("enable\n")
        connection.s..("terminal length 0\n")
        t__.s..(1)
        
        #Entering global config mode
        connection.s..("\n")
        connection.s..("configure terminal\n")
        t__.s..(1)
        
        #Open user selected file for reading
        selected_cmd_file _ o..(cmd_file, _)
            
        #Starting from the beginning of the file
        selected_cmd_file.s..(0)
        
        #Writing each line in the file to the device
        ___ each_line __ selected_cmd_file.r_l..
            connection.s..(each_line + '\n')
            t__.s..(2)
        
        #Closing the user file
        selected_user_file.c..
        
        #Closing the command file
        selected_cmd_file.c..
        
        #Checking command output for IOS syntax errors
        router_output _ connection.r..(65535)
        
        __ __.s..(b"% Invalid input", router_output
            print("* There was at least one IOS syntax error on device @ :(".f..(ip))
            
        ____
            print("\nDONE for device @. Data sent to file at @.\n".f..(ip, st.(d_t_.d_t_.now)))
            
        #Test for reading command output
        #print(str(router_output) + "\n")
        
        #Searching for the CPU utilization value within the output of "show processes top once"
        cpu _ __.s..(b"%Cpu\(s\):(\s)+(.+?)(\s)* us,", router_output)
        
        #Extracting the second group, which matches the actual value of the CPU utilization and decoding to the UTF-8 format from the binary data type
        utilization _ cpu.group(2).d..("utf-8")
        
        #Printing the CPU utilization value to the screen
        #print(utilization)
        
        #Opening the CPU utilization text file and appending the results
        w__ o..("D:\\App3\\cpu.txt", "a") __ f:
            #f.write("{},{}\n".format(str(datetime.datetime.now()), utilization))
            f.w..(utilization + "\n")
        
        #Closing the connection
        session.c..
     
    ______ ?.AuthenticationE..:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")