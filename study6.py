#1
moji = "カミュ"
print(moji[0])
print(moji[1])
print(moji[2])

#2
diary= "日記"
friend = "友達"
formatting = "私は昨日{}を書いて、{}に送った！".format(diary, friend)
print(formatting)

#3
str = "aldous Huxley was born in 1894"
str = str[0].upper()+str[1:]
print(str)

#4
info = "どこで？ だれが？ いつ？"
result = info.split(' ')
print(result)
print(type(result))

#5
words = ["The","fox","jumped","over","the","fence","."]
result = "  ".join(words[:6])+"".join(words[6:])
print(result)

#6
change = "A screaming comes across the sky."
change = change.replace("s","$")
print(change)

#7
find = "Hemingway".index("m")
print(find)

#8
escape = "\"ある人は十銭をもって 一円の十分の一と解釈する。ある人は十銭をもって 一銭の十倍と解釈する。\"同じ言葉が人によって高くも低くもなる。"
print(escape)

#9
add = "three " + "three " + "three "
re = "three " * 3
print(add)
print(re)

#10
cut_moji = "四月の晴れた寒い日で、時計がどれも十三時を打っていた"
print(cut_moji[:10])