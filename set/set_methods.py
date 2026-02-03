play_list = {'oru pere varalaru','God mode', 500,"Nallaru po","Kannukulla","Nallaru po"}
play_list2 = {'saopaulo','light switch','Nallaru po'}

print(play_list.union(play_list2))

print(play_list.intersection(play_list2))

print(play_list.difference(play_list2))

play_list.add('Naa ready')
print(play_list)

play_list.remove(500)
print(play_list)

play_list.discard('Yalle') #discard to remove without throwing error
print(play_list)