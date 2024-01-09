n = int(input())
gifts = input().split()
arr = [int(a) for a in gifts]
sent = {arr[i]:i+1 for i in range(n)}

received = [str(sent[i+1]) for i in range(n)]
print(" ".join(received))
