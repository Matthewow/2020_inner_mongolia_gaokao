
import os
import glob
index = set()

def tagging():
    count = 0
    f = open("./index_wo_dul.txt", "r")

    lines = f.readlines()
    for line in lines:
        number = line.split(":")[0]
        tags_line = line.split(":")[1].replace('"',"")
        tags_line2 = tags_line.replace("['","")
        tags_line = tags_line2.replace("']","")
        tags_line2 = tags_line.replace(" ","")
        tags_line = tags_line2.replace("/","")
        tags_line2 = tags_line.rstrip()
        tags = tags_line2.split("''")
        filename = "./Tags/" + tags_line2 + ".txt"
        print(filename)
        for tag in tags:
            if len(tag) >= 20:
                continue
            filename = "./Tags/" + tag + ".txt"
            file1 = open(filename, "a")
            file1.write("{}\n".format(number))
        print(count)
        count += 1

def tag_delete():
    tags = glob.glob('./Tags/*.txt')
    for tag in tags:
        file1 = open(tag)
        if (len(file1.readlines()) <= 5):
            os.remove(tag)
            print(f"{tag} removed")


def readfiles(filename):
    file1 = open(filename, 'r')
    lines = file1.readlines()
    for line in lines:
        indexs.add(str(line))
    file1.close()


def classify():
    filenames = ["index0-32k.txt", "index32k-36k.txt", "index36k-40k.txt", "index40k-44k.txt", "index44k-56k.txt", "index56k-596000.txt"]
    for filename in filenames:
        readfiles(filename)

    f = open("index_w.txt", "a")
    for i in indexs:
        f.write(str(i))
    f.close()

