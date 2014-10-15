def opamp(v1, v2, r1, r2=10000):
    v1, v2, r1 ,r2 = float(v1), float(v2), float(r1), float(r2)
    return (v1-v2)*(r1+r2)/r2 + v2

def opamp2(v1, v2, r1, r2=10000):
    v1, v2, r1 ,r2 = float(v1), float(v2), float(r1), float(r2)
    return -r1/r2*(v2-v1)+v1

for r1 in [5000, 20000]:
    for v2 in [10, 7, 5, 3, 0]:
        print opamp2(5, v2, r1)

