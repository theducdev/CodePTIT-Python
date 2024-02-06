import pickle

def check(a):
    n = str(a)
    if len(n) < 2:
        return False
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True


try:
    f1 = open("DATA1.in", "rb")
    ds1 = pickle.load(f1)
    used1 = [0] * 10001
    for x in ds1:
        used1[x] += 1
    f1.close()

    f2 = open("DATA2.in", "rb")
    ds2 = pickle.load(f2)
    used2 = [0] * 10001
    for x in ds2:
        used2[x] += 1
    f2.close()

    for i in range(10, 10000):
        if used1[i] and used2[i] and check(i):
            print(i, used1[i], used2[i])


except FileNotFoundError:
    pass
except pickle.UnpicklingError:
    pass
except Exception as e:
    pass

