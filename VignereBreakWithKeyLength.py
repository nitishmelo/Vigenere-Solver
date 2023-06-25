from collections import Counter
import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"

def breaker(text, keylen):
    savedtext = list([ch for ch in text if ch.isalpha()])
    
    if not savedtext:
        sys.stderr.write("Text cannot be decrypted; there are no letters.")
        return

    savedtext = "".join(savedtext)
    savedtext = savedtext.lower()
    textlen = len(savedtext)

    commonlettervals = [
        5, 20, 1, 15, 9, 14, 19, 18, 8, 12, 4, 3, 21, 13, 6, 16, 7, 23, 25, 2,
        22, 11, 24, 10, 17, 26
    ]
    letterfreqs = [
        0.1249, 0.0928, 0.0804, 0.0764, 0.0757, 0.0723, 0.0651, 0.0628, 0.0505,
        0.0407, 0.0382, 0.0334, 0.0273, 0.0251, 0.0240, 0.0214, 0.0187, 0.0168,
        0.0166, 0.0148, 0.0105, 0.0054, 0.0023, 0.0016, 0.0012, 0.0009
    ]
    keyl = keylen
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
        mostfreq = max(mostfreq, key=mostfreq.get)
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
    print(f"\nKey: {key}\nPlaintext: {decrypt(text, key)}")

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