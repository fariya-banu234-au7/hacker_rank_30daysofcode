# d = dict()
# n = int(input( ))

# for i in range(n):
     
#     key, value = input().split()
#     d[key] = value
# # print(d)

# for i in range(n):
#     name = input()
#     if name in d:
#         print(f'{name}={d[name]}')
#     else:
#         print("Not found")





# n = int(input())
# d = dict()

# for i in range(0, n):
#     name, number = input().split()
#     d[name] = number
# #print(d) Check if your dictionary  is ready

# for i in range(0, n):
#     name = input()
#     if name in d:
#         print(f'{name}={d[name]}')
#     else:
#         print("Not found")



d = dict()
n = int(input( ))

for i in range(n):
     
    key, value = input().split()

    d[key] = value

while True:

    try:
        name = input()
        if name in d:
            print(f'{name}={d[name]}')
        else:
            print("Not found")
    except EOFError:
        break


