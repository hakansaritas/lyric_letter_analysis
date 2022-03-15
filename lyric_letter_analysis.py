# ######################################################################
# ##########   NUMBER OF THE LETTERS IN THE LYRIC ! ####################

# This work is about calculation of frequency of the unique letters in a lyric 
# using basic python commands. It would be a first step for future project which
# analyses the rock'n'roll lyric letters (mainly 80's) by creating database.

# I have written this function to improve myself,give useful
# ideas to python users and get fun.

# for much more information how to use this function, visit my Mediuum page

# I would want to dedicate this my first public function to "Ronnie James DIO" and "Rainbow"...
# which are the one the best rock vocals and music band in the universe.

# I am opening to suggestions and corrections
# Thanks
# ======================================================================
# Hakan SARITAŞ
# linledin : www.linkedin.com/in/hakansaritas
# Mediuum: https://hakansaritas.medium.com/
# GitHub: https://github.com/hakansaritas
# kaggle: https://www.kaggle.com/hakansaritas
# ======================================================================
# ######################################################################

#pip install lyricsgenius

import matplotlib.pyplot as plt
from lyricsgenius import Genius

api_key = "copy and paste your api client access token "

def lyric_letter():
    
    #input song name and artist 
    song_title = input("Song Name: ")
    song_artist = input("Artist Name: ")
    
    # Genius function with api key
    genius = Genius(api_key, remove_section_headers=True, verbose=False)
    
    # treching the genius  database with song name and artist inputs
    song = genius.search_song(song_title, song_artist)
    
    # corrected artist and title name even if you write wrong 
    song_artist = song.artist
    song_title = song.title
    
    # geting the lyric with song name
    song_before = song.lyrics
    
    # to get rid of song name in the first line
    song_after = song_before.split("\n", 1)[1]
    
    ################################################################################
    # using uppercase 
    song_upper = song_after.upper()
    
    # counter is composed of unique letters 
    counter = ""
    
    for letter in song_upper:
        if letter not in counter:
            counter += letter
    
    # unwanted symbol the lyric list. you can add symbol.
    unwanted = [" ", ",", ".", "'", "!", "#", "$", "\n", "?", "-", "_", "%", "&", "+", "=", "(", ")", "[", "]", '"',
                    ":", "1","2","3","4","5","6","7","8","9","0"]
    
    
    letter_list = []
    number_list = []
    
    # get rid of unwanted symbols.
    for i in counter:
    
        if i in unwanted:
            continue
            
    # record unique letters and their counts separately into the lists.
        letter_list.append(i)
        number_list.append(song_upper.count(i))
    # ########################################################
    
    # zipping the lists and sort by letter 
    zipped_letter = list(zip(letter_list, number_list))
    zipped_letter.sort()
    
    # get the sorted key-values pairs using dictionary functions.
    new_dict = dict(zipped_letter)
    A = list(new_dict.keys())
    B = list(new_dict.values())
    # ##########################################################
    
    # zipping the lists and sort by number
    zipped_number = list(zip(number_list, letter_list))
    zipped_number.sort()
    
    # different way to get the sorted list value pairs using list functions.
    
    C =[]
    D =[]
    
    for i in range(len(zipped_number)):
        C.append(zipped_number[i][0])
        D.append(zipped_number[i][1])
    
    ###############################################################
    # CREATE GRAPHS    
    # you can check plot styles;
    # plt.style.available[:]
    
    plt.style.use('seaborn')
    
    fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(20, 20))
    
    ax[0].barh(D, C);
    ax[1].scatter(A, B, color="g");
    ax[1].plot(A, B);
    ax[2].stem(A, B, use_line_collection=True)
    
    
    # set labels: https://matplotlib.org/stable/tutorials/text/text_intro.html
    
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    
    ax[0].set_title("Number of the Letters: "+song_title.upper() +" "+"("+song_artist+")", fontdict = font1)
    
    ax[0].set_xlabel("Frequency", fontdict = font2)
    ax[0].set_ylabel("Letters", fontdict = font2)
    
    
    ax[1].set_xlabel("Letters", fontdict = font2)
    ax[1].set_ylabel("Frequency", fontdict = font2)
    
    
    ax[2].set_xlabel("Letters", fontdict = font2)
    ax[2].set_ylabel("Frequency", fontdict = font2)
    
    
    # add annotation, the frequency number of the each letter
    for ii, txt in enumerate(B):
        ax[2].annotate(txt, (A[ii], B[ii]))
    
    fig.tight_layout()

    
    print("\n"+"(Letter,Frequency): "+ str(zipped_letter)+ "\n")
    print("The total number of all letters: "+ str(sum(B))+ "\n")
    print("The total number of different letters: "+ str(len(A))+ "\n")
#    print(10*"*"+ str(song_before.split("\n", 1)[0]) + 10*"*")
#    print(song_after)

    return song_title, song_artist, song_before, song_after

###############################################################
## to run lyric_letter function uncomment below command
    
# song_title, song_artist, song_before, song_after = lyric_letter()

