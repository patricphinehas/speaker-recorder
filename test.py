
import os
from selenium import webdriver
import time


def main():
    counter = 0
    links = []
    string_start = "https://www.youtube.com"
    default_url = "https://www.youtube.com/playlist?list=PL90229471516D05ED"
    url = input("Enter the URL of the playlist. Must be HTTPS"
                "\nexample:\nhttps://www.youtube.com/playlist?list=PL90229471516D05ED\n")
    # the example is to Miracle of Sounds Music Playlist
    if url.__contains__(string_start):
        print("URL is " + url)
    else:
        url = default_url
        print("Bad URL\nURL is " + url)
    direct_path = input("Enter the Direct Path of the playlist or enter nothing and it will use the root Music folder. "
                        "\nEnsure that you add the slash at the end"
                        "\nexample:\nD:/Users/\n")
    driver = webdriver.Firefox()
    driver.get(url)
    the_page = driver.page_source
    while True:
        counter = counter + 1
        driver.execute_script('window.scrollTo(0,'+counter.__str__()+'00000);')
        # scroll to the bottom of the page
        time.sleep(2)
        new_page = driver.page_source
        if the_page != new_page:
            # check if you are at the end of the page, if you are read all the way to the bottom of the new page
            the_page = new_page
        else:
            break
    driver.close()
    all_page = the_page.split()
    for word in all_page:
        if "watch?v" in word:
            if "href=\"" in word:
                links.append(word)
                # get all the actual videos and none of the extra html
    links.pop(0)
    links.pop(0)
    # get rid of extra links that are not part of the playlist
    import numpy as np
    x = np.array(links)
    links = np.delete(x, slice(None, None, 2))
    # get rid of every other link because there are two of every video right next to each other
    for i in range(len(links)):
        links[i] = links[i][6:]
        links[i] = links[i][:-1]
        links[i] = string_start + links[i]
    # we now have the list of all the links
    # begin saving the file
    identity = url[38:]
    direct_path = os.path.dirname(direct_path)
    path = os.path.dirname("~/Music/")
    path = os.path.expanduser(path)
    if os.path.exists(direct_path):
        path = direct_path
        # check if the direct path you are using exists and use it, otherwise your root Music folder
    print("Path is " + path)
    file = open(path+"/YT_PLaylist"+identity+".xspf", "w")
    file.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
    file.write("""<playlist version="1" xmlns="http://xspf.org/ns/0/">\n""")
    file.write("""<trackList>\n""")
    for words in links:
        file.write("""<track>\n""")
        file.write("""<title>"""+words+"""</title>\n""")
        file.write("""<location>"""+words+"""</location>\n""")
        file.write("""</track>\n""")
    file.write("""</trackList>\n""")
    file.write("""</playlist>""")
    file.close()
    time.sleep(10)


if __name__ == "__main__":
    main()