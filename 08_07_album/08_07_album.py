def make_album(artist, title, tracks=None):
    '''Make a music album dictionary.'''
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album
print(make_album('Adele', '30'))
print(make_album('Taylor Swift', 'Evermore', 15))
print(make_album('Ed Sheeran', 'Divide', 12))