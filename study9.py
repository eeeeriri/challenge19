# ファイル操作
#1
with open("self_taught.csv","r")as fileopen:
    print(fileopen.read())

#2
ques = input("身長はいくつですか？")
with open("QuestionTest.txt","w")as filewrite:
    filewrite.write(ques)
with open("QuestionTest.txt","r")as fileopen:
    print(fileopen.read())

#3 リストの書き出し
import csv
with open("movie.csv","w+",newline="\n") as filewrite:#open関数のnewline="\n"で改行させないようにする
    movie = [["Top Gun", "Risky Business", "Minority Report"],["Titanic", "The Revenant", "Inception"],["Training Day", "Man on Fire", "Flight"]]
    fw=csv.writer(filewrite)
    for i in range(len(movie)):
        """
        csv:csvモジュール
        writer:writerメソッド
        fw:csvオブジェクト
        writerow:writerowメソッド
        """
        fw.writerow(movie[i])
    filewrite.seek(0)#データの先頭に移動
    print(filewrite.read())

#4　#3の日本語ver
import csv
with open("movie_ja.csv","w+",newline="\n",encoding="utf-8") as filewrite:
    movie = [["トップガン", "危険なビジネス", "マイノリティ・リポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレーニングデイ", "マイ・ボディガード", "フライト"]]
    for i in range(len(movie)):
        fw=csv.writer(filewrite)
        fw.writerow(movie[i])
    filewrite.seek(0)
    print(filewrite.read())