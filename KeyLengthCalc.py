from collections import Counter
from VignereBreakWithKeyLength import alphabet

def calcIOC(text):
    loweredtext = list([ch for ch in text if ch.isalpha()])
    loweredtext = "".join(loweredtext)
    loweredtext = loweredtext.lower()
    alphalen = len(alphabet)
    textlen = len(loweredtext)
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
    if textlen < 2:
        return 1;
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