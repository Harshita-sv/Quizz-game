n=int(input("Enter a number"))
s= set(map(int, input(). split()))
N= int(input("Enter a number"))

for _ in range(N):
    command= input(). split()
    cmd= command[0]
    
    if cmd=="pop":
        if s:
            s.pop()
    elif cmd=="remove":
        value= int(command[1])
        if value in s:
            s.remove()
    elif cmd=="discard":
        value=int(command[1])
        s.discard()
print(sum(s))

