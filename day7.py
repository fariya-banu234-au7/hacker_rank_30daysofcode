#https://www.hackerrank.com/challenges/30-arrays/problem

n = int(input())

arr = list(map(int, input().rstrip().split()))

arr.reverse()
print(arr)
for x in range(len(arr)): 
    print(arr[x], end = " ")