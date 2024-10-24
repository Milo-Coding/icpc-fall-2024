evens = [num for num in range(20) if not num%2]
print(evens)

coords = [(x,y) for x in range(3) for y in range(3)]
print(coords)

mat = [[1,2,3],[4,5,6],[7,8,9]]
            #does this one first
flat = [val for row in mat for val in row]
                           #does this one second
print(flat)