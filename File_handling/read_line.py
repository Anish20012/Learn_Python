with open("notes.txt","r") as note:
    print(note.readline().strip())
    print(note.readline().strip())
 


with open("notes.txt","r") as note1:
    for line in note1:
        print(line.strip())