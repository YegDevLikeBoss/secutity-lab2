import argparse

def caesar(string, shift):
    return "".join(chr(((ord(char) - 65 + shift) % 26) + 65) if not char.isspace() else " " for char in string)

def frequencyAnalysis(string): # Normalised frequency analysis
    freq = [0] * 26

    for c in string:
        if c.isalpha():
            freq[ord(c) - ord('A')] += 1

    total = sum(freq)

    for i in range(0, len(freq)):
        freq[i] /= (float(total) / 100)

    return freq

def initialiseParser():
    parser = argparse.ArgumentParser(description = "Encrypt or decrpyt a string using the Caesar Cipher")

    parser.add_argument("--bruteforce", "--brute", "-b", help = "bruteforce mode", action = "store_true")
    parser.add_argument("--encrypt", "--enc", "-e", help = "encryption mode (default)", action = "store_true")
    parser.add_argument("--decrypt", "--dec", "-d", help = "decryption mode", action = "store_true")
    parser.add_argument("--shift", "-s", help = "value for the Caesar shift", type = int, choices = range(1, 26))
    parser.add_argument("--spacing", "-x", help = "specify the spacing in output", type = int)
    parser.add_argument("--guess", "-g", help = "use statistical analysis to guess the most likely shift value", action = "store_true")
    parser.add_argument("--input", "-i", help = "input file", type = str)

    return parser

def shiftScoreCalculator(frequencyAnalysis, shift): # Calculates a weighted score for a given shift value
    englishFrequencies = [  8.167, 1.492, 2.782,
                            4.253, 12.702, 2.228,
                            2.015, 6.094, 6.966,
                            0.153, 0.772, 4.025,
                            2.406, 6.749, 7.507,
                            1.929, 0.095, 5.987,
                            6.327, 9.056, 2.758,
                            0.978, 2.360, 0.150,
                            1.974, 0.074 ]

    score = 0

    for index in range(0, 26):
        shiftIndex = (index + shift) % 26
        score += abs(frequencyAnalysis[index] - englishFrequencies[shiftIndex])

    return score / 26

def shiftCalculator(frequencyAnalysis): # Calculates the most likely shift value for a substring by comparing weighted scores of different shift values
    bestGuess = ''
    bestGuessVal = float('inf')

    for shift in range(1, 27):
        score = shiftScoreCalculator(frequencyAnalysis, shift)

        if score < bestGuessVal:
            bestGuessVal = score
            bestGuess = 26 - shift

    return bestGuess

def main():
    parser = initialiseParser()
    args = parser.parse_args()

    if args.bruteforce:
        bruteforce = True
    else:
        bruteforce = False
        shift = args.shift

    if args.decrypt:
        shift = -shift

    input_file = open(args.input)
    string = input_file.read()

    if args.spacing:
        string = ' '.join([string[i:i + args.spacing] for i in range(0, len(string), args.spacing)])

    if args.guess:
        shift = shiftCalculator(frequencyAnalysis(string))
        print("Best shift value guess: %d (%c)\nAttempting decryption...\n%s" % (shift, chr(shift + ord('A') - 1), caesar(string, -shift)))
        return

    if bruteforce:
        for shift in range(1, 26):
            print("%d:\t%s" %(shift, caesar(string, -shift)))
    else:
        print(caesar(string, shift))

if __name__ == "__main__":
    main()