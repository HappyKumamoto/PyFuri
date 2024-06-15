import random

#「歩兵」駒の表と裏の要素を五枚分用意
komas= ("歩","と","歩","と","歩","と","歩","と","歩","と")

#10の要素から5を無作為に選び出す
kekka = random.sample(komas , 5)

#結果のリストをシンプルにする
result= ''
for i in range(len(kekka)):
    result += kekka[i]

# HTML の <py-script>タグ に表示させる
pyscript.write("furi" , result )
