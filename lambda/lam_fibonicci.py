fin = []
fin.append(0)
fin.append(1)
map(lambda i:fin.append(fin[i]+fin[i+1]), range(10))
print fin
