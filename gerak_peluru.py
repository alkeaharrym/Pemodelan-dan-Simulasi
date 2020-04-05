import math
# from prettytable import PrettyTable
import matplotlib.pyplot as plt

print(math.sin(math.radians(35))) #sin
print(math.cos(math.radians(35))) #cos

kec = input("V0: ")
v0 = int(kec)
num = input("sudut: ")
a = int(num)

D = 0.0013
m =  0.15
g = 9.806 #gravitasi
teta_sin = (math.sin(math.radians(a))) #nilai sin teta
print(teta_sin)
teta_cos = (math.cos(math.radians(a))) #nilai cos teta
print(teta_cos)

dT = 0.01
dT2 = 0

vy_n = v0*teta_sin
vx_n = v0*teta_cos
v_n = 0
y = not(0)
v_curr = 0

ax = 0
ay = 0

vy_curr = 0
vx_curr = 0

x_n = 0
y_n = 0

x_curr = 0
y_curr = 0

i = 1
tab = PrettyTable()
tab.field_names = ["No.","Waktu(t)","X","Y","Vx","Vy"]

x = []
y = []

plt.xlabel('Jarak')
plt.ylabel('Ketinggian')

x.append(x_n)
y.append(y_n)

tab.add_row([i,dT2,x_n,y_n,vx_n,vy_n])
i = 2

while y_n >= 0: #dengan hambatan
    v_curr = math.sqrt(math.pow(vx_n,2) + math.pow(vy_n,2))
    ay = -g-D/m*v_curr*vy_n
    ax = -(D/m)*vx_n*v_curr
    vy_curr = vy_n + ay * dT
    vx_curr = vx_n + ax * dT
    y_curr = y_n + (vy_curr * dT)
    x_curr = x_n + (vx_curr * dT)
    dT2 = round(dT2,2)
    dT2 = dT2 + dT
    x.append(x_curr)
    y.append(y_curr)
    tab.add_row([i,dT2,x_curr,y_curr,vx_curr,vy_curr])
    vy_n = vy_curr
    vx_n = vx_curr
    y_n = y_curr
    x_n = x_curr
    plt.plot(x,y)
    i += 1

print(tab)
plt.show()






