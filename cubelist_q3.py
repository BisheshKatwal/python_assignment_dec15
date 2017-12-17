def cube(l):
    new_list=[]
    for each in l:
        new_list.append(each**3)
    return new_list

arbitary_list=[1,2,4,4,3,5,6]
print(cube(arbitary_list))