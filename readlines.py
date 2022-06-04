def cutOneVideo(filename, sec, video):
    frames = sec*20

    with open(f"data/{filename}", "r+") as f, open("data/" + str(video) + "_" + filename, "w") as f2:
        data = f.readlines()  # Read from file 1
        f.seek(0)
        for line in data[frames:]:
            f.write(line)
        for line in data[:frames]:
            f2.write(line)

len = [27, 27, 28, 27, 26, 27, 28, 27, 27, 26, 28, 25, 27, 27, 26]

for num in range (1,22):
    for l in range(0,15):
        cutOneVideo(f"{num}.txt", len[l], l+1)

