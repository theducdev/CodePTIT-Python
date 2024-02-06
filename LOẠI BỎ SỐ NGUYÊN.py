f = open("DATA.in", "r")
ds = []
for x in f.read().split():
    try: 
        a = int(x)
        if a <-2**32 or a >2**32: ds.append(x)
    except Exception as e:
        ds.append(x)
ds.sort()
for x in ds:
    print(x, end = " ")
   