# ######################################################################
# ##########   NUMBER OF THE LETTERS IN THE LYRIC ! ####################
# I have written this function just for fun and make en exercise to improve myself.

# The issue is weird and i know that it is unnecessary but the music is universe.
# I couldn't wait to present such an important script to humanity.  :))

# many thanks Vahit Keskin, Mehmet Aktürk, Ozan Güner, Mehmet Tuzcu,...
# Arif Eker and my DSMLBC-8 group friends who are from Veri Bilim Okulu and Miuul.

# I would want to dedicate this my first public function to "Ronnie James DIO" and "Rainbow"...
# who was the one the best rock vocals and music band in the universe.

# I am opening to suggestion and correction

# Hakan Saritas (saritas_hakan@yahoo.com)
# ######################################################################
pip install lyricsgenius
api_key = ""

import seaborn as sns
import matplotlib.pyplot as plt
from lyricsgenius import Genius

def lyric_letter():
    """
    this function is calculate number of the unique letter in a lyric
    fill input song name, and lyric as copy-paste from web
    :param lyric: song lyric
    :return: letter and its count value , 3 graphs which show number and count values
    """
    song_title = input("write song name")
    song_artist = input("write artist name")

    genius = Genius(api_key, remove_section_headers=True, verbose=False)

    song = genius.search_song(song_title, song_artist)

    song_before = song.lyrics
    song_artist = song.artist

    # to get rid of song name in the first line
    song_after = song_before.split("\n", 1)[1]
    ################################################################################
    counter = ""
    song_lower = song_after.lower()

    for letter in song_lower:
        if letter not in counter:
            counter += letter

    # unwanted symbol the lyric list. you can add symbol.
    unwanted = [" ", ",", ".", "'", "!", "#", "$", "\n", "?", "-", "_", "%", "&", "+", "=", "(", ")", "[", "]", '"',
                ":"]

    # get rid of unwanted symbols.
    # record letters and their counts separately into lists.

    letter_list = []
    number_list = []

    for i in counter:

        if i in unwanted:
            continue

        letter_list.append(i)
        number_list.append(song_lower.count(i))

    zipped = list(zip(letter_list, number_list))
    zipped.sort()

    zipped_number = list(zip(number_list, letter_list))
    zipped_number.sort(reverse=True)

    new_dict = dict(zipped)
    A = list(new_dict.keys())
    B = list(new_dict.values())

    new_dict2 = dict(zipped_number)
    C = list(new_dict2.keys())
    D = list(new_dict2.values())
    ###############################################################
    # choose one of the plot style from the list checking with;
    # plt.style.available[:]

    plt.style.use('seaborn')

    # 3 graphs in one row
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))

    # first two graphs is created by seaborn, all two p overlap, p1 is seperate
    p = sns.barplot(C, D, ax=ax[0]);
    p1 = sns.scatterplot(A, B, color="g", ax=ax[1]);
    p1 = sns.lineplot(A, B, size=0.3, legend=False, ax=ax[1]);

    # last graph is created by matplotlib
    ax[2].stem(A, B, use_line_collection=True)

    # add annotation of the count values on the graph
    for ii, txt in enumerate(B):
        ax[2].annotate(txt, (A[ii], B[ii]))

    # labels
    p.set_xlabel("Count", fontsize=10)
    p.set_ylabel("Letters", fontsize=10)
    p1.set_title("Number of Unique Letter: " + song_artist + " "+song_title, fontsize=15)
    p1.set_xlabel("Letters", fontsize=10)
    p1.set_ylabel("Count", fontsize=10)

    fig.tight_layout()
    fig.show()

###############################################################

# automatically run lyric_letter function
lyric_letter()


#pip install lyrics-extractor

#Your_API_KEY = AIzaSyAS1PZXpsPeuhYZA5gsNMyLct0g_nWnWZQ
#GCS_ENGINE_ID = 1cd7497b11168bb63
###############################################################






