# ループ
#1
words = ["ヴァンパイア・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for word in words:
    print(word)

#2
for stres in range(25,50):
    print(stres)

#3
words = ["ヴァンパイア・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for i,word in enumerate(words):
    print(i,word)

#4
# 無限ループ
while True:
# 文字を入力させる
    n = input("qもしくは数字を入力してください:")
#     ｑなら終了
    if(n == "q"):
        break
#     数字なら正解か判定
    elif (n.isdigit() == True):
        list1 = ["1","3","6","10","15"]
        print(type(n))
        while True:
            #リストと一致したら正解
            if n in list1:
                print("正解")

            #リストと不一致なら不正解
            else:
                print("不正解")
            break
    else:
        print("数字を入力するか、qで終了します")
        break

#5
# リスト1とリスト2のすべての掛け算
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
mult = []
for i in list1:
    for j in list2:
        mult.append( i * j )
print(mult)

