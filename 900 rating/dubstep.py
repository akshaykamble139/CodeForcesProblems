word = input()

song = word.replace("WUB", " ").split(" ")
print(" ".join([a for a in song if len(a) > 0]))