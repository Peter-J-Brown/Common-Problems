
inputstring = 'hello world'

substrings=[]

for i in range(0,len(inputstring)+1):
    for j in range(i+1,len(inputstring)+1):
        substring = inputstring[i:j]
        substrings.append(substring)
uniq=set()
for x in substrings:
    uniq.add(x)

print(substrings)