def makemap(fstr, tostr):
    transmap = {}
    for i, (fchar, tochar) in enumerate(zip(fstr, tostr)):
        if tochar in " ":
    	    tochar=""
        if fchar in " ":
            while fstr[i] in " ":
                i -= 1
            transmap[fstr[i]] += tochar
        else:
    	    transmap[fchar] = tochar
    return transmap

if __name__ in "__main__":
    print(makemap("йцукя чс", "qweryaxc"))
