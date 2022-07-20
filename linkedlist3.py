
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
