def activity():
    activitys = []
    print("**Welcome to the To-Do List App**")

    total_activity = int(input("Enter the total number of activities you want to add: "))
    for i in range(1,total_activity+1):
        activity_name = input(f"Enter the activity {i}: ")
        activitys.append(activity_name)
        print(f"Today's activitys are\n{activitys}")

    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        if operation == 1:
            add = input("Enter the activity you want to add: ")
            activitys.append(add)
            print(f"activity {add} has been successfully added.")
        elif operation == 2:
            update = input("Enter the activity that  you want to update")
            if update_act in activitys:
                ind = activitys.index(update_act)
                new_activity = input("Enter the new activity: ")
                activitys[index] = new_activity
                ativitys[ind] = up
                print(f"Updated task '{updated_val}' to '{up}'.")

            else:
                print(f"Activity '{update_act}' not found.")
        elif operation == 3:
            del_act = input("Enter the activity you want to delete: ")
            if del_act in activitys:
                    ind = activitys.index(del_act)
                    del activitys[ind]
                    print(f"Activity '{del_act}' has been successfully deleted.")  
            else:
                    print(f"Activity '{del_act}' not found.")
        elif operation == 4:
            print(f"Total activitys = {activitys}")
        elif operation == 5:
            print("Closing the program....")
            break
        else:
            print("Invalid Input. Please enter a number from 1 to 5.")
     
activity()              
                          

