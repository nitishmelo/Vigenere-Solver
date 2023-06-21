import VignereBreakWithKeyLength as VP
import KeyLengthCalc as KLC

print("\nEnter ciphertext: ")
text = input()
keyl = KLC.KeyLength(text)
VP.breaker(text, keyl)