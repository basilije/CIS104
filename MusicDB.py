import json
import sys

mydatafile = 'MyFavoriteSongs.db'

try:
    with open(mydatafile) as f:
        masterlist = json.load(f)
except:
    print("Failed to load the music database. Failed to open file " + mydatafile)
    masterlist = []

def music(choice):
    
    if choice == 'add':
        new = {}
        new['title'] = input('Enter song title: ')
        new['artist'] = input('Enter artist: ')
        new['album'] = input('Enter album name: ')
        new['track'] = input('Enter track #: ')
        new['input']= input('Enter year: ')
        new['genre'] = input('Enter genre: ')
        if len(masterlist) <= 7: 
            masterlist.append(new)
        else:
            print("That's to many songs ya chode!!")
        
    if choice == 'list':
        for things in masterlist:
            for keys,values in things.items():
                print(f'{keys} is {values}')

    if choice == 'save':
        with open(mydatafile, 'w') as f:
            json.dump(masterlist, f)

    if choice == 'help':
        print("this is the help")

    if choice == 'exit':
        sys.exit()
