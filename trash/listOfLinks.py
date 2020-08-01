def func_names():
    f = open("allxmlNames.txt","r")
    txt = f.readline()
    lOfLinks = []
    while(txt != ''):
        lOfLinks.append(txt)
        txt = f.readline()
    f.close()
    return lOfLinks
