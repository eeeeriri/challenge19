#1
musician = ["Revo", "Arashi", "Hoshino Gen"]
print(musician)

#2
place = [("35", "135"),("43", "141"),("26", "127")]
print(place)

#3
kubo = {"height": 160.0,
        "eyecolor": "brown",
        "like-color": "blue"}
print(kubo)

#4
kubo = {"height": 160.0,
        "eyecolor": "brown",
        "like_color": "blue"}

kubo_info_get = input("height or eyecolor or like_color, please choice write:")
if kubo_info_get in kubo:
    erika = kubo[kubo_info_get]
    print(erika)
else:
    print("Not info.")

#5
musician_song = {
    "HoshinoGen": [
        "Koi",
        "Doraemon",
    ]
}
print(musician_song)

#6
set = ("1","3")