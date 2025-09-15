meeting =[
    ["Monday", "3:30 PM", "Joe", "Sam"] ,
    ["Monday", "4:30 PM", "Bob", "Alice"] ,
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"] ,
    ["Tuesday", "9:30 AM", "Joe", "Bob"],
]

info_meeting ={}

for i in meeting:
    for x in i[2:]:
        if x not in info_meeting:
            info_meeting[x]={}
            info_meeting[x][i[0]] = [i[1]]
        if x in info_meeting:
            if i[0]  in info_meeting[x]:
                if not i[1] in info_meeting[x][i[0]]:
                    info_meeting[x][i[0]].append(i[1])
            else :
                info_meeting[x][i[0]] = [i[1]]



for i in info_meeting:
    for x in info_meeting[i]:
      if len(info_meeting[i][x]) == 2 :
          for j in info_meeting[i][x]:
            print(f'{x} {i} has a meeting {j}')
      else:
          print(f'{x} {i} has a meeting {info_meeting[i][x][0]}')

