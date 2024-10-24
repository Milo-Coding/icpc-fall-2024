print(sum(i for i in range(30) if not i%2))

print(list(zip((i for i in range(20)), (i for i in range(30)))))

long_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(list(enumerate(long_list)))