def find_room(cur_number,rooms):
    if cur_number not in rooms:
        rooms[cur_number]=cur_number+1
        return cur_number

    parent = find_room(rooms[cur_number],rooms)
    rooms[cur_number] = parent+1
    return parent







#def check_room(number):
 #   global room_after
#    if number not in room_after:
#        room_after.append(number)
#        return
#    else:
#        check_room(number+1)
k=10
room_number=[1,1,1,5,3,1] #배정받고싶어하는 방

room={}
answer=[]

# o   o
#[4,5,6,7,8,9,10]

for number in room_number:
    tmp_room = find_room(number,room)
    answer.append(tmp_room)


print(answer)







