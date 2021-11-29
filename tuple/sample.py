n = int(input())
lst = [int(i) for i in input().split()][:n]
tpl = tuple(lst)

print(hash(tpl))

