f = open('QR-location-AR.csv', 'r')
offsets = [4194665,4194675]   #BYTE POSITIONS. You can use single value
for offset in offsets:
    f.seek(offset)
    print (f.readline().strip())