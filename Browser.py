import webbrowser
print "select search engineer: google[enter '1'] bing[enter '2'] yahoo[enter '3']"
eng = input()
print "enter search:" 
search = input()
if(eng == 1):
    google1 = "https://www.google.co.il/search?q="
    google2 = "&ie=UTF-8&oe="
    sl = search.split()
    csl = len(sl)
    c = 0
    while(c < csl-1):
        google1 = google1 + str(sl[c]) + "+"
        c = c+1
    google1 = google1 + str(sl[c]) + google2
    webbrowser.open(google1)
if(eng == 2):
    bing1 = "https://www.bing.com/search?q="
    bing2 = "&form=QBLH&sp=-1&pq=hello&sc=8-5&qs=n&sk=&cvid=0FE7C3D3A8494830B5B8BC423C9FCC73"
    sl = search.split()
    csl = len(sl)
    c = 0
    while(c < csl-1):
        bing1 = bing1 + str(sl[c]) + "+"
        c = c+1
    bing1 = bing1 + str(sl[c]) + bing2
    webbrowser.open(bing1)
if(eng == 3):
    yahoo1 = "https://search.yahoo.com/search?p="
    yahoo2 = "&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"
    sl = search.split()
    csl = len(sl)
    c = 0
    while(c < csl-1):
        yahoo1 = yahoo1 + str(sl[c]) + "+"
        c = c+1
    yahoo1 = yahoo1 + str(sl[c]) + yahoo2
    webbrowser.open(yahoo1)