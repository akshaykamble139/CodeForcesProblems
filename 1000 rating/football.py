n = int(input())

team1 = input()
if n == 1:
    print(team1)
else:
    team_one = 1
    team_two = 0
    team2 = ""
    for _ in range(n-1):
        t = input()
        if team1 == t:
            team_one += 1
        else:
            team_two += 1
            team2 = t

    if team_one > team_two:
        print(team1)
    else:
        print(team2)