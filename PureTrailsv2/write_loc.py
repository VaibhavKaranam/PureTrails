file = "trash_cans.txt"
rfile = open(file, "r")
afile = open(file, "a")

def write_loc(lat, lon):
    if type(lat) is not float:
        quit()
    if type(lon) is not float:
        quit()
    last = 1
    for line in rfile:
        last += 1
    afile.write("%d. %.10f, %.10f\n" % (last, lat, lon))

def main():
    lat = float(input("Enter the latitude: "))
    lon = float(input("Enter the longitude: "))
    write_loc(lat, lon)

main()
