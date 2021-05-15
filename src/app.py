import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add():
    # Add a phone number 
    add_telephone_number = input("I need your phone number: ")
    queue.enqueue(add_telephone_number)
    print("We have added your phone number")
    #pass

def dequeue():
    # delete 
    number = queue.dequeue()
    send(body="its your turn", to=number)
    print(number)
    
    #pass

def save():
    data = queue.get_queue()
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)
    #pass

def load():
    global queue
    with open("queue.json", 'r') as f:
        data = json.load(f)
        f.close()
        queue = Queue(mode="FIFO" ,current_queue=data)
    #pass 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 1:
        add()
    elif option == 2:
        dequeue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
