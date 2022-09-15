# map => semua ELEMEN kena
def dobelkan(n):
    return n + n
  
numbers = (1, 2, 3, 4)

result = map(dobelkan, numbers)
print(list(result))


#filter => sesuai namanya, ELEMEN ada yg disingkirin
umur = [5, 12, 17, 18, 24, 32]
def cekUmur(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(cekUmur, umur)
print(list(adults))


# nb: ini func biasa diganti pake lambda juga bisa

