import json

from matplotlib.font_manager import json_dump

def printList(list):
    counter = 0
    for i in list:
        print(str(counter) + ": " + i)
        counter += 1
    print()

f = open('msglow_kompas.txt', 'r')

tanggal = []
url = []
judul = []
berita = []

counter = 0
for line in f:
    content = line.replace('\n', '')
    if counter % 5 == 0:
        tanggal.append(content)
    elif counter % 5 == 1:
        url.append(content)
    elif counter % 5 == 2:
        judul.append(content)
    elif counter % 5 == 3:
        berita.append(content)
    
    counter = counter + 1

# remove duplicates

print("Number of URLs found: " + str(len(url)))
print("Length before removing duplicates: ", len(url))
i = 0
j = 0
while i < len(tanggal):
    while j < len(tanggal):
        if i == j:
            j = j + 1
        else:
            if tanggal[i] == tanggal[j]:
                tanggal.pop(j)
                url.pop(j)
                judul.pop(j)
                berita.pop(j)
            else:
                j = j + 1
    i = i + 1
    j = i

print("Length after removing duplicates: ", len(url))

# remove irrelevant results

print("Length before removing irrelevant results: ", len(url))

i = 0
while i < len(tanggal):
    if (berita[i].__contains__("glow")):
        pass
    else:
        tanggal.pop(i)
        url.pop(i)
        judul.pop(i)
        berita.pop(i)
    i = i + 1

print("Length before removing irrelevant results: ", len(url))

# split tanggal
listTanggal = []
for tgl in tanggal:
    t = tgl.split('/')
    listTanggal.append({'tahun': t[2], 'bulan': t[1], 'tanggal': t[0]})

jsonTanggal = json_dump(listTanggal, 'tanggal.json')
jsonURL = json_dump(url, 'url.json')
jsonJudul = json_dump(judul, 'judul.json')
jsonBerita = json_dump(berita, 'berita.json')

printList(judul)