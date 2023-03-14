from collections import Counter

alphabet = "abcdefghijklmnopqrstuvwxyz"

def calcIOC(text):

    loweredtext = list([ch for ch in text if ch.isalpha()])
    loweredtext = "".join(loweredtext)
    loweredtext = loweredtext.lower()

    alphalen = len(alphabet)

    textlen = len(loweredtext)

    if (textlen == 1):
        return 0

    lettercounter = Counter(loweredtext) 

    ioc = 0

    sum2 = 0

    for i in range(alphalen):

        charcount = lettercounter[alphabet[i]]
        sqval = (charcount * (charcount - 1))
        sum2 += sqval
    
    ioc = sum2 / ((textlen * (textlen - 1)))
    
    return ioc

def KeyLength(text):

    loweredtext = list([ch for ch in text if ch.isalpha()])
    loweredtext = "".join(loweredtext)
    loweredtext = loweredtext.lower()

    textlen = len(loweredtext)

    maxioc = 0.0

    iterations = int(textlen / 10) + 3

    maxdiff = (0.0, 1)

    for i in range(1, iterations):

        totalioc = 0.0
        avgioc = 0.0

        for j in range(i):

            subtext = ""

            while (j < textlen):

                subtext += loweredtext[j]

                j += i

            totalioc += calcIOC(subtext)
        
        avgioc = (totalioc / i)

        if (i == 1):
           if (avgioc >= 0.060):
                break

        diff = (avgioc - maxioc)

        if ((diff > maxdiff[0]) and (i > 1)):
            
            maxdiff = (diff, i)

        if (avgioc > maxioc):

            maxioc = avgioc
        
    keyl = maxdiff[1]

    return keyl

def breaker(text, keylen):

    commonlettervals = [5, 20, 1, 15, 9, 14, 19, 18, 8, 12, 4, 3, 21, 13, 6, 16, 7, 23, 25, 2, 22, 11, 24, 10, 17, 26]

    letterfreqs = [0.1249, 0.0928, 0.0804, 0.0764, 0.0757, 0.0723, 0.0651, 0.0628, 0.0505, 0.0407, 0.0382, 0.0334, 0.0273, 0.0251, 0.0240, 0.0214, 0.0187, 0.0168, 0.0166, 0.0148, 0.0105, 0.0054, 0.0023, 0.0016, 0.0012, 0.0009]

    savedtext = list([ch for ch in text if ch.isalpha()])

    savedtext = "".join(savedtext)

    savedtext = savedtext.lower()

    textlen = len(savedtext)

    keyl = int(keylen)

    strind = 0

    subtext = ""

    key = ""

    cmltrind = 0

    difflist = []

    charlist = []

    for i in range(keyl):

        difflist.clear()
        charlist.clear()

        strind = i

        while (strind < textlen):

            subtext += savedtext[strind]

            strind += keyl
    
        mostfreq = Counter(subtext)

        mostfreq = max(mostfreq, key = mostfreq.get)

        freqval = ord(mostfreq) - 96

        while (cmltrind < 26):

            shift = ((freqval - 1) - (commonlettervals[cmltrind] - 1)) % 26

            shift += 96

            shiftchar = chr(shift + 1)

            plaintext = decrypt(subtext, shiftchar)

            plaintext = list([ch for ch in plaintext if ch.isalpha()])

            plaintext = "".join(plaintext)

            plaintext = plaintext.lower()

            freqplain = Counter(plaintext)

            plaintextlen = len(plaintext)

            difftotal = 0.0

            for x in range(26):

                intval = commonlettervals[x] + 96
                charval = chr(intval)
                charcount = freqplain[charval]
                freq = (charcount / plaintextlen)
                difftotal += abs((freq - letterfreqs[x]))

            difflist.append(difftotal)
            charlist.append(chr(commonlettervals[cmltrind] + 96))

            cmltrind += 1

        tuple = list(zip(difflist, charlist))

        tuple = sorted(tuple, key=lambda tup: tup[0])

        minchar = tuple[0][1]

        minval = ord(minchar) - 96

        shift = ((freqval - 1) - (minval - 1)) % 26

        shift += 96

        shiftchar = chr(shift + 1)

        key += shiftchar

        subtext = ""

        cmltrind = 0

    key = key.upper()

    print(key)

    print(decrypt(text, key))

def decrypt(text, key):
    
    keylen = len(key)

    plaintext = ""

    alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

    keyindex = 0

    alterval = 0

    val = 0

    lochar = 0

    key = key.upper()

    for ch in text:

        if ch in alphabet:

            val = ord(ch)

            if (val < 97):
                val -= 64
                lochar = 0

            else:
                val -= 96
                lochar = 1

            alterval = ord(key[keyindex]) - 64

            val = ((val - 1) - (alterval - 1)) % 26

            if (lochar):

                val += 96

            else:

                val += 64

            val = chr(val + 1)

            plaintext += val

            keyindex += 1

        else:

            plaintext += ch 

        if (keyindex == keylen):

            keyindex = 0

    return plaintext       

text = input()

keyl = KeyLength(text)

breaker(text, keyl)