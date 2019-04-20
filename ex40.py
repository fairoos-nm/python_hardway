#Module class and objects.

#Modules are like dictionaries

mystuff = {"apple": "I love apples"}

print(mystuff["apple"])

#here we can call a value in dictionaries using thair keys:
#Assume that you have file mystuff.py and it containing a function called apple:

# def apple():
#     print("I love apples")
# my_name = "name"

#You can call it like this function from some where like

#import mystuff.py
#mystuff.apple()
#print(mystuff.my_name)


#CLASS ARE LIKE MODULES

class mystuff(object):
    def __init__(self):
        self.tangerine = "Ajd now a thouseand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

inst = mystuff()
inst.apple()
inst.tangerine

#Getting things from things:
#----------------------------#

#..............dict_style:...........#
#mystuff["apple"]

#.............module style:.........#
#mystuff.apple()
#print(mystuff.tangerine)

#.............class style:............#
#thing = mystuff()
#thing.apple()
#print(thing.tangerine)



class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

wedding_song = Song(["love of my sweet",
                     "Your lovely voice",
                     "my dream is you"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

wedding_song.sing_me_a_song()
