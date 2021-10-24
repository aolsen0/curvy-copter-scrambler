import random
phase1=[]
phase2=[]
phase3=[]
phase4=[]
a=open("phase1.txt")
i=0
for line in a:
    if i==1:
        phase1.append(line)
    i=1-i
a.close()
b=open("phase2.txt")
i=0
for line in b:
    if i==1:
        phase2.append(line)
    i=1-i
b.close()
c=open("phase3.txt")
i=0
for line in c:
    if i==1:
        phase3.append(line)
    i=1-i
c.close()
d=open("phase4.txt")
i=0
for line in d:
    if i==1:
        phase4.append(line)
    i=1-i
d.close()
print("Ready!")

while True:
    a=input()
    try:
        yay=int(a)
    except:
        continue
    if yay==0:
        break
    for i in range(yay):
        sol=" ".join([random.choice(phase1),random.choice(phase2),random.choice(phase3),random.choice(phase4)])
        scramble=" ".join(reversed(sol.split()))
        print(i+1,scramble)