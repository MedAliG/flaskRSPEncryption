result = {}
keys = []


def gen_key(cle, nbRonds):
    cles = []
    for rond in range(nbRonds + 1):
        mot = int(cle[rond * 4: rond * 4 + 16], 2)
        cles.append(mot)
    return cles

def rsp_mot16(x, nbRonds, cles):
    
    sub = {0: 0xe, 1: 4, 2: 0xd, 3: 1, 4: 2, 5: 0xf, 6: 0xb, 7: 8, 8: 3, 9: 0xa, 0xa: 6, 0xb: 0xc, 0xc: 5, 0xd: 9, 0xe: 0, 0xf: 7}
    
    per = {1: 1, 2: 5, 3: 9, 4: 13, 5: 2, 6: 6, 7: 10, 8: 14, 9: 3, 10: 7, 11: 11, 12: 15, 13: 4, 14: 8, 15: 12, 16: 16}
    w = int(x, 2)
    for rond in range(nbRonds + 1):
        x = "{0:016b}".format(w)
        keys.append(x)
        print("> {0:016b}".format(w))
        w = w ^ cles[rond]
        u = sub[w & 0x000f] + (sub[(w & 0x00f0) >> 4] << 4) + (sub[(w & 0x0f00) >> 8] << 8) + (sub[(w & 0xf000) >> 12] << 12)
        v = 0
        for j in range(16):
            b = (u & (1 << (16 - per[j + 1]))) >> 16 - per[j + 1]
            v += b << (16 - j - 1)
        if rond < nbRonds - 1:
            w = v
        elif rond < nbRonds:
            w = u
    return "{0:016b}".format(w)

def rsp(x, nbRonds, cle):
    cles = gen_key(cle, nbRonds)
    y = ""
    ind = 0
    while ind < len(x):
        y += rsp_mot16(x[ind: ind + 16], nbRonds, cles)
        ind += 16
    result['keys'] = keys
    result['y'] = y
    return keys,y



