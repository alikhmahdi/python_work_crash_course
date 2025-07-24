def make_album(artist, title, tracks='unkown'):
    '''Make a music album dictionary.'''
    album = {'artist': artist, 'title': title}
    album['tracks'] = tracks
    return album
user_albums = {
}
while True:
    name=input("Hello, What is your name? ")
    print("\nPlease enter the album information:")
    artist = input("Artist name (or 'q' to quit): ")
    if artist == 'q':
        break
    title = input("Album title: ")
    tracks = input("Number of tracks (leave blank if unknown): ")
    if tracks.isdigit():
        user_albums[name] = make_album(artist, title, int(tracks))
    else:
        user_albums[name] = make_album(artist, title)

print("\nYour album collection:")
for user, album in user_albums.items():
    print(f"{user}: {album}")
