import VigenereCompleteBreak as VCB
def main():
    print("\nEnter ciphertext: ")
    text = input()
    VCB.decode(text)

if __name__ == "__main__":
    main()