# Linked Lists

## Overview
Linked lists can be difficult to understand and difficult to understand why they are even useful at all. As always, a great way to visualize a data structure is a simple graphic. As seen in the below graphic, a linked list is a list where each data value points to the next one. You may be asking... So what? Why do I care? How can it help me make cool games/apps? That is an excellent question! One possible scenario which we will experiment with below is creating a playlist for a music player such as Spotify. A linked list can be just the data structure we need for such an occasion!
![image info](./Linkedlist.png)

## Advantages
One of the main ways linked lists are actually useful is that inserting and deleting is really easy! This is why I brought up a playlist as a great example for why a linked list can be useful. If we were to use a regular list, we may have to traverse through an entire list just to be able to add one song to the list. This is why linked lists are so useful!

## Disadvantages
As with any data structure there are certainly disadvantages to linked lists! Linked lists can be real memory hogs which can lead to them not being useful for certain applications where an array or regular list might be more suitable. 

## Example 1
Below is a simple example of how a linked list can be created in Python. There is no Linked List module that we can use so we can create our own. You may use this for the project 

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    class LinkedList:
        def __init__(self):
            self.head = None
    first_item = Node("First")
    second_item = Node("Second")
    third_item = Node("Third")
    
    ## Creating the linked list
    the_list = LinkedList()
    the_list.head = first_item
    first_item.next = second_item
    second_item.next = third_item
    node = the_list.head
    #prints first node data
    
    while node is not None:
        print(node.data)
        node = node.next


## Example 2: 
Train cars are a classic real world example of what a linked list is like. Multiple cars are attached together and new cars can be added at any place in the train. In this problem, find the best place to hitch a new train. In this example we are going to assume that the best place is between two values that have the smallest average value (weight). For example, consider a linked list of 600, 700, 100, 800, 400, 300, 200, 500. The best place would be between 300 and 200 because the average value of 300 and 200 is 250 which is less than any other car. Return the two cars in a list. In the above example the output should be [300, 200]


## Sample Code:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    class LinkedList:
        def __init__(self):
            self.head = None
    def main():
        first_car = Node(600)
        second_car = Node(700)
        third_car = Node(100)
        fourth_car = Node(800)
        fifth_car = Node(400)
        sixth_car = Node(300)
        seventh_car = Node(200)
        eighth_car = Node(500)
    
        #Creating the linked list
        the_list = LinkedList()
        the_list.head = first_car
        first_car.next = second_car
        second_car.next = third_car
        third_car.next = fourth_car
        fourth_car.next = fifth_car
        fifth_car.next = sixth_car
        sixth_car.next = seventh_car
        seventh_car.next = eighth_car
        node = the_list.head
        print(find_min_values(node))
    #prints first node data
    def find_min_values(node):
        min_so_far = 10000
        min = []
        while node.next is not None:
            if node.data + node.next.data <min_so_far:
                min = [node.data, node.next.data]
                min_so_far = node.data + node.next.data
            else:
                node = node.next
        return min
    main()



## Challenge:
Song Player
Imagine you are working for a company like Spotify before it became Spotify! One of the problems that you must solve is creating a constantly updating linked list of songs that are playing/have played/will be played. Write a linked list that allows the user to select "Previous Song" and "Next Song" along with showing what song is playing. 
Stretch challenge: Actually play the songs using a module of your choice.

## Sample Soultion:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None
    class LinkedList:
        def __init__(self):
            self.head = None
    def main():
        first_song = Node("Elevation- U2")
        second_song = Node("Hey You- Dope Lemon")
        third_song = Node("Rainbow Valley- Matt Corby")
        fourth_song = Node("I found- Amber Run")
        fifth_song = Node("Brother- Matt Corby")
        l_list = LinkedList()
        l_list.head = first_song
        first_song.next = second_song
        second_song.next = third_song
        third_song.next = fourth_song
        fourth_song.next = fifth_song
        fifth_song.previous = fourth_song
        fourth_song.previous = third_song
        third_song.previous = second_song
        second_song.previous = first_song
        playing = True
        current_song = first_song
        while playing == True:
            print("Current Song: " + current_song.data)
            user_input = int(input("1 Keep listening, 2 Next Song, 3 Previous Song"))
            if user_input == 1:
                pass
            elif user_input == 2:
                current_song = current_song.next
            elif user_input == 3:
                current_song = current_song.previous
    main()



### Stretch:
Play actual songs!