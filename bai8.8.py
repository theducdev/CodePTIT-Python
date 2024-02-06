def make_album(name, album):
    info = {
        "Name": name,
        "Album": album
    }
    return info

while True:
    name = input()
    if name == "END": break
    album = input()
    artist = make_album(name, album)
    print(artist)
