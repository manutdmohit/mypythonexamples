heroines=['Katrinakaif','Kareenakapoor','Anushka','Deepika','SunnyLeone','Mallika']
startswithK=list(filter(lambda name:name[0]=='K',heroines))
print(startswithK)
lendiv5=list(filter(lambda name:len(name)%5==0,heroines))
print(lendiv5)
odd=list(filter(lambda name:len(name)%2!=0,heroines))
print(odd)