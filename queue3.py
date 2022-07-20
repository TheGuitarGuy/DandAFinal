from queue import Queue
def main():
    my_orders = Queue()
    answer = ""
    while True:
        answer = input("Would you like to order? (Y/N)")
        order_status = input("Has the kitchen finished an order? (Y/N) ")
        if order_status == "Y" and my_orders.empty() == False:
            print(str(my_orders.get()) + "'s order is ready!")
        else:
            print("No order in queue!")
        if answer == "Y":
            name = input("What is your name? ")
            my_orders.put(name)
            print("Your food will be out shortly!")
        elif answer == "N":
            print("Have a great day!")
main()
