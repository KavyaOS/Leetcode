def song_chain(songs):
    result = []
    longest_list = 0
    words = songs[0].split(" ")
    last_word = words[-1]
    last_song = songs[0]
    songs_list = [last_song]

    for k in range(len(songs)):
        longest_so_far = 0
        for i in range(1, len(songs)):
            words = songs[i].split(" ")
            if words[0] == last_word:
                longest_so_far = longest_so_far + 1
                if last_song not in songs_list:
                    songs_list.append(last_song)
                if songs[i] not in songs_list: songs_list.append(songs[i])
            last_word = words[-1]
            last_song = songs[i]

        if longest_so_far>=longest_list:
            if longest_so_far == longest_list:
                if songs_list[0].compareTo(result[0])>0:
                    result = songs_list
                    #print(songs_list[0].compareTo(result[0])>0)
            else:
                longest_list = longest_so_far
                result = songs_list

    return result

list_of_songs = ["Every Breath you take down", "down by the", "river side"]
print(song_chain(list_of_songs))