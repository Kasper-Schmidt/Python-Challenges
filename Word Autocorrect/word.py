import csv
from datetime import datetime

WORDS_FILE = "words.txt"
LOOKUPS_FILE = "lookups.csv"


def read_words():
    words = []
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                words.append(word)
    return words


def word_exists(word, words):
    return word in words


'''
def close_words(input_word, words):
    for w in words:
        if w and w[0] == input_word[0]:
            print(w)
'''



def close_words(input_word, words, max_suggestions=5):
    """
    Finder op til max_suggestions ord der "ligner" input_word.

    Lighedslogik:
    - Kandidatordet skal starte med samme første bogstav
    - Kandidatordets længde må højst afvige med 1 (±1)
    - Score = antal bogstaver der matcher på samme position (index)
    """

    # Normalisér input (så opslaget bliver case-insensitive)
    input_word = input_word.strip().lower()

    # Hvis brugeren ikke skrev noget, ingen forslag
    if not input_word:
        return []

    def score(candidate: str) -> int:
        """
        Returnerer et simpelt match-score:
        +1 for hvert bogstav der er ens på samme position i input_word og candidate
        """
        return sum(1 for a, b in zip(input_word, candidate) if a == b)

    candidates = []

    # Gennemgå alle ord i ordlisten og udvælg relevante kandidater
    for w in words:
        if not w:
            continue

        # Filter 1: samme startbogstav (hurtig grov sortering)
        if w[0] != input_word[0]:
            continue

        # Filter 2: næsten samme længde (for at undgå helt irrelevante forslag)
        if abs(len(w) - len(input_word)) > 1:
            continue

        # Beregn hvor godt ordet matcher input
        s = score(w)

        # Gem kun kandidater der matcher mindst én position
        if s > 0:
            length_diff = abs(len(w) - len(input_word))
            candidates.append((s, length_diff, w))

    # Sortering:
    # - score: højeste først (derfor -s)
    # - length_diff: laveste først
    # - w: alfabetisk som tie-breaker
    candidates.sort(key=lambda x: (-x[0], x[1], x[2]))

    # Returnér kun ordene (uden score/metadata), og maks max_suggestions
    return [w for _, __, w in candidates[:max_suggestions]]


def main():
    words = read_words()
    word = input("Word: ").strip().lower()

    if word_exists(word, words):
        print("FOUND!")
    else:
        print("Word not found")

        suggestions = close_words(word, words)

        if suggestions:
            print("Suggestions:")
            for s in suggestions:
                print(s)
        else:
            print("No suggestions")


if __name__ == "__main__":
    main()
