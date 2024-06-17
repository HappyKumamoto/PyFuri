import random
import count

#「歩兵」駒の表と裏の要素を五枚分用意
komas= ("歩 ","と ","歩 ","と ","歩 ","と ","歩 ","と ","歩 ","と ")

#10の要素から5を無作為に選び出す
kekka = random.sample(komas , 5)

#選び出された5要素を連結
result= ''
for i in range(len(kekka)):
    result += kekka[i]

# HTML の <py-script>'furi' に表示
pyscript.write("furi" , result )

#どちらが先手か判定を判断
countF = countT = 0
for i in range(len(kekka)):
    if kekka[i] == '歩':
        countF += 1
    else:
        countT += 1

# HTML<py-script>タグの'hantei'に表示
if countF > countT:
    sente = '上座'
    pyscript.write("hantei" , sente)
else:
    sente = '下座'
    pyscript.write("hantei" , sente)

