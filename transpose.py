import os

majorkeys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
minorkeys = ['Am','A#m','Bm','Cm','C#m','Dm','D#m','Em','Fm','F#m','Gm','G#m']

# adef#m - 0-5-7-9
# bf#eg#m - 2-7-9-12
# cfgam - 3-9-11-0
# dgabm - 5-11-0-2
# eab - 7-0-2
# fa#c - 9-1-3
# gcd - 11-3-5

def chord_family(initial):
    maj1 = majorkeys.index(initial)
    maj2 = (maj1+5)%12
    maj3 = (maj1+5+2)%12
    minor = (maj1+5+2+2)%12

    print(majorkeys[maj1],majorkeys[maj2],majorkeys[maj3],minorkeys[minor]) 

def starter():
    initial = input('\nEnter the Root chord : ').upper()
    if initial not in majorkeys:
        print("Sorry! Give a valid key")
    else:
        print("\nChord family of",initial,': ')
        chord_family(initial)
        check_transpose(initial)


def check_transpose(initial):

    initial_index = majorkeys.index(initial)
    while(True):
        choice = input("\nDo you want to transpose it?  (y/n)").lower()
        
        if choice == 'y':
            transpose = input("\nEnter the transpose val : ")
            if transpose != None :
                transpose = int(transpose)
                if transpose < 13 and transpose > -13 :
                    n = (transpose + initial_index)%12
                    new_initial = majorkeys[n]

                    print("\nBase chord family of",initial,': ')
                    chord_family(initial)

                    print("\nTranspose =",transpose)

                    print("Chord family of",majorkeys[n],': ')
                    chord_family(new_initial)

                else:
                    print("Please Enter a valid transpose value")
            else: 
                print("Please Enter a valid transpose value")
        else :
            break

starter()
