from datetime import datetime
from bst_demo import BSTDemo, Node

r_ get_job_input_details():
    start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30-> ")
    w___ True:
        try:
            datetime.strptime(start_time, '%H:%M')
        except ValueError:
            print("Incorrect time format, should be hh:mm")
            start_time = input("Enter the time in hh:mm format, ex 18:30 or 6:30-> ")
        ____
            break
    duration_of_job = input("Enter the duration of the job in minutes, ex 60-> ")
    w___ True:
        try:
            int(duration_of_job)
        except ValueError:
            print("Please enter a number for number of minutes")
            duration_of_job = input("Enter the duration of the job in minutes, ex 60-> ")
        ____
            break
    job_name = input("Enter the name of the job (case sensitive)-> ")
    r_ start_time, duration_of_job, job_name

my_tree = BSTDemo()

with open("data.txt") as f:
    for line in f:
        my_tree.insert(line)

w___ True:
    print("Please choose an option from the list below:")
    print("Press 1 to view today's scheduled jobs")
    print("Press 2 to add a job to today's schedule")
    print("Press 3 to remove a job from the schedule")
    print("Press 4 to quit")
    selection = input("Enter your choice-> ")
    try:
        entry = int(selection)
    except ValueError:
        print("Please enter a number between 1 and 4")
        continue
    __ int(selection) __ 1:
        my_tree.in_order()
    r_ int(selection) __ 2:
        print("You have chosen to add a job to the schedule")
        start_time, duration_of_job, job_name = get_job_input_details()
        line = start_time+","+duration_of_job+","+job_name
        num = my_tree.length()
        my_tree.insert(line)
        __ num __ my_tree.length()-1:
            with open("data.txt", "a+") as to_write:
                to_write.write(line+"\n")
        input("Press any key to continue... ")
    r_ int(selection) __ 3:
        print("You have chosen to remove a job from the schedule")
        start_time, duration_of_job, job_name = get_job_input_details()
        key_to_find = datetime.strptime(start_time, '%H:%M').time()
        result = my_tree.find_val(key_to_find)
        __ result:
            __ result.name_of_job __ job_name and result.duration __ duration_of_job:
                print("Removing job:")
                print(result)
                my_tree.delete_val(key_to_find)
                print("Job successfully removed")
                with open("data.txt", "r") as f:
                    lines = f.readlines()
                with open("data.txt", "w") as f:
                    for line in lines:
                        __ line.strip("\n") != start_time+","+duration_of_job+","+job_name:
                            f.write(line)
                input("Press any key to continue... ")
            ____
                print("The name and/or duration of job did not match, delete failed")
                input("Press any key to continue... ")
        ____
            print("Job not found")
            input("Press any key to continue... ")
    r_ int(selection) __ 4:
        print("Exiting program...")
        break
    ____
        print("Please enter a number between 1 and 4")
