a = input()
b = input()
l = str(int(a)+int(b)).replace("0","")
k = str(int(a.replace("0",""))+int(b.replace("0","")))

if l == k:
    print("YES")
else:
    print("NO")