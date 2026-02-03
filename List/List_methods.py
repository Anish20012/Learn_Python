play_list = ['oru pere varalaru','God mode', 'Oorum blood']
print(play_list)
play_list.append('Nallaru po')
print('after append :',play_list)

play_list.insert(1,'kanukulla')
print('after insert :',play_list)

play_list.remove("Oorum blood")
print('after remove :',play_list)

play_list.pop()
print('after pop :',play_list)

print('count : ', play_list.count('God mode'))

#slicing

print('only top 2 in list : ',play_list[0:2])

print('last 2 in list',play_list[-2:])

print('between - 2 & 3  rd song',play_list[2:4])