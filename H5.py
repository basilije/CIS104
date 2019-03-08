from MusicDB import music

def main():
    music('help')

    while True:
        choice = input('What do you want to do? ')
        music(choice)


main()


