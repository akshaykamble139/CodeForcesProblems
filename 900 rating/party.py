n = int(input())

count = 0
ans = 0

arr = [0 for a in range(n+9)]
for i in range(1,n+1):
    arr[i] = int(input())

for i in range(1,n+1):
    count = 0
    x = arr[i]
    while x != -1:
        x = arr[x]
        count+=1

    ans = max(count,ans)

print(ans+1)

#
# graph = {
#     -1:[]
# }
# rank=[-1 for i in range(n)]
# for i in range(1,n+1):
#     e = int(input())
#     if e == -1:
#         graph[-1].append(i)
#         rank[i-1] = 1
#     else:
#         if e in graph:
#             graph[e].append(i)
#         else:
#             graph[e] = [i]
#         if rank[e-1] != -1:
#             rank[i-1] = rank[e-1] + 1
#
# # print(graph)
# for a in graph[-1]:
#     if rank[a - 1] == -1:
#         rank[a - 1] = 1
#
# arr=[-1 for i in range(n)]
#
#
# def func(key):
#     global graph
#     global rank
#     global arr
#     # print(f"key = {key} arr = {arr}")
#     if key in graph and ((key != -1 and arr[key-1] == -1) or key == -1):
#         # print(f"key now = {key}")
#         values = graph[key]
#         if key != -1:
#             arr[key-1] = 0
#         if key == -1:
#             curr_rank = 1
#         else:
#             curr_rank = rank[key-1]
#         for a in values:
#             # print(f"values of key = {key} : {a}")
#             if rank[a-1] == -1:
#                 rank[a-1] = curr_rank + 1
#             func(a)
#
#
# func(-1)
# # for (key, value) in graph.items():
# #     current = rank[key-1]
# #     for a in value:
# #         if rank[a-1] == -1:
# #             rank[a-1] = current + 1
#
# print(max(rank))
