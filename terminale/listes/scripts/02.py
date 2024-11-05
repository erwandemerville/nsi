t = [2,5,1,9,8]
# Insérer 5 au début :
t.append(None)
for i in range(len (t) - 1, 0, -1):
    t[i] = t[i - 1]
t[0] = 5

print(f't = {t}')