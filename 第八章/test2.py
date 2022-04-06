def make_album(singers, songs, numbers=' '):
    persons = {'singer': singers, 'song': songs}
    return persons

while True:
    print("Do you like?")
    singer = input("singers: ")
    if singer == 'q':
        break

    song = input("songs: ")
    if song == 'q':
        break

    person = singer + song

    print(person)

zhoujielun = make_album('zhoujielun', 'qinghuaci')
liudehua = make_album('liudehua', 'whqinguv')
bing = make_album('bing', 'dej')


print(zhoujielun)
print(liudehua)
print(bing)