from collections import Counter

def arithmetic_encoding(word):
    freq = Counter(word)

    total_symbols = len(word)

    probabilities = {}
    for symbol in freq:
        probabilities[symbol] = freq[symbol] / total_symbols

    symbols = sorted(probabilities.keys())

    cumulative_probabilities = {}
    cumulative = 0
    for symbol in symbols:
        cumulative_probabilities[symbol] = cumulative
        cumulative += probabilities[symbol]

    ranges = {}
    for symbol in symbols:
        ranges[symbol] = (cumulative_probabilities[symbol], cumulative_probabilities[symbol] + probabilities[symbol])

    print("Symbol\tProbability\tCumulative Probability\tRange")
    for symbol in symbols:
        print(f"{symbol}\t{probabilities[symbol]:.5f}\t\t{cumulative_probabilities[symbol]:.5f}\t\t({ranges[symbol][0]:.5f}, {ranges[symbol][1]:.5f})")

    low = 0.0
    high = 1.0
    for symbol in word:
        range_ = high - low
        high = low + range_ * ranges[symbol][1]
        low = low + range_ * ranges[symbol][0]

    print(f"\nEncoded value: {low}")


if __name__ == "__main__":
    word = input()
    arithmetic_encoding(word)
