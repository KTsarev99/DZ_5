# "aaaabc" = 4a2b1c
text = "aaaabbbbcccctttttv1111" # если символы не по порядку то не работает :( 
print(text)
def pack(): # сжатие
    pack=[]
    for i,item, in enumerate(text):
        if text[i:i+1] != text[i+1:i+2]:
            a=(text.count(text[i]))
            if text[i] not in pack:
                pack.append(item)
                pack.append(a)
        pack1=("".join(map(str, pack)))
    return pack1
     
print(pack())
repack=(pack())

i=0
g=1
while i < len(repack):
    while g < len(repack):
        a = repack[i]
        i+=2
        b = int(repack[g])
        g+=2
        q=a*b
        print(q,end="")
