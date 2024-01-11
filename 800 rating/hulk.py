n = int(input())

ans = "I hate "
end = "it"
count = 1
while count < n:
    if count % 2 == 1:
        ans += "that I love "
    else:
        ans += "that I hate "
    count+=1

ans += end

print(ans)
