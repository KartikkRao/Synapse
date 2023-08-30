encoded_list=[
    [1,2,3,4,6],
    [5,7,8,9,15,18,19,20,21],
    [12,14,16,18],
    [10,11,12,13,16,17,18,20]
]
def explode_chains(list):
    temp=[]
    temp1=[]
    for i in range(len(list)):
        count=0
        for j in range(len(list[i])-1):
            if list[i][j+1]-list[i][j]==1:
                count += 1
            elif count>0:
                count -= 1
            if count == 2:
                temp.append(i)
                temp1.append(j)
                count = 0
    print(temp)
    print(temp1)
    for i in range(len(temp)):
        for j in range(3):
            if temp[i]==temp[i-1]:
                list[temp[i]].remove(list[temp[i]][temp1[i] - 1-3])
            else:
                list[temp[i]].remove(list[temp[i]][temp1[i]-1])
    return(list)
result=explode_chains(encoded_list)
print(result)



