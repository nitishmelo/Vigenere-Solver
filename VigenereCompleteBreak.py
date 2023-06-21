import VignereBreakWithKeyLength as VP
import KeyLengthCalc as KLC

def decode(text):
    keyl = KLC.KeyLength(text)
    VP.breaker(text, keyl)