import math
cateto_oposto = int(input())
cateto_adjacente = int(input())

tg = ((cateto_oposto/2)/(cateto_adjacente/2))
arctg = math.atan(tg)
degrees = arctg * (180/math.pi)
print(round(degrees), "\N{DEGREE SIGN}",sep='')



