from bs4 import BeautifulSoup
import sys
import os




def deleteImages(path):

    file = open(path, "rb")

    soup = BeautifulSoup(file, "html.parser")

    file.close()

    images = soup.find_all("img")

    for image in images:

        imgPath = image["src"]

        if "https" in imgPath:
            continue

        print(imgPath[3:])

        os.remove(imgPath[3:])


def deletePages(path):
    print(path)
    os.remove(path)



def main():

    for path in sys.argv[1:]:

        # deleteImages(path)
        deletePages(path)

    




main()




# index_html = open("index.html", "r")
# soup = BeautifulSoup(index_html, "html.parser")
# index_html.close()

# projects = soup.find_all("h4", class_="my-3")

# print(projects[3])