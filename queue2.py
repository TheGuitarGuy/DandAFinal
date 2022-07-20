from queue import Queue
def main():
    my_orders = Queue()
    answer = 0
    while my_orders.qsize() <= 100:
        answer = input("Would you like to order or pickup? 1 to order 2 to pickup: ")
        if answer == 1:
            my_orders.put(order_number)
            order_number += 1
            print("Your order has been added to the queue! ")
            print("The estimated time is " + str(my_orders.qsize()) + " minutes!")
        elif answer == 2:
            my_orders.get()
main()