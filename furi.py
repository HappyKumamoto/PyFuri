import random
#import count

#「歩兵」駒の表と裏の要素を五枚分用意
komas= ("歩 ","と ","歩 ","と ","歩 ","と ","歩 ","と ","歩 ","と ")

#10の要素から5を無作為に選び出す
kekka = random.sample(komas , 5)

#選び出された5要素を連結
result= ''
for i in range(len(kekka)):
    result += kekka[i]

# HTMLの<py-script>の'furi' に表示
pyscript.write("furi" , result )

#判定のために '歩' と ’と' の数を数える
countF = countT = 0
for i in range(len(kekka)):
    if kekka[i] == '歩':
        countF += 1
    else:
        countT += 1

# 判定を<py-script>の'hantei'に表示
if countF > countT:  #歩の枚数が多いとき
    sente = '上座'
    pyscript.write("hantei" , sente)
else:                #との枚数が多いとき
    sente = '下座'
    pyscript.write("hantei" , sente) 

