import math


def find_triplets(cypher):
    triplets = {}
    for i in range(3, len(cypher)):
        triplet = cypher[i - 3: i]
        if triplet in triplets.keys():
            triplets[triplet].append(i - 3)
        else:
            triplets[triplet] = [i - 3]

    return triplets


def ggt(a, b):
    if a == b:
        return a
    return ggt(a - b, b) if a > b else ggt(b - a, a)


def ggt_list(numbers):
    if len(numbers) == 1:
        return numbers[0]

    tmp = []
    for i in range(1, len(numbers)):
        tmp.append(ggt(numbers[i], numbers[i - 1]))

    return ggt_list(tmp)


def calc_triplet_diffs(triplets):
    diffs = []
    valid_triplets = []
    for trip, indices in zip(triplets.keys(), triplets.values()):
        if len(indices) <= 1:
            continue
        valid_triplets.append((trip, len(indices)))
        for i in range(1, len(indices)):
            diffs.append(indices[i] - indices[i - 1])

    return valid_triplets, diffs


def most_frequent_symbols(symbols):
    s_freq = {}
    for s in symbols:
        if s in s_freq.keys():
            s_freq[s] += 1
        else:
            s_freq[s] = 1

    return {key: value / len(symbols) for key, value in sorted(s_freq.items(),
            key=lambda item: item[1], reverse=True)}


def analyze_symbol_frequency(cypher, key_len):
    data = []
    for i in range(key_len):
        data.append([])

    for i in range(len(cypher)):
        caesar_index = i % key_len
        data[caesar_index].append(cypher[i])

    return [break_caesar(syms) for syms in data]


def char_list_to_str(chars):
    ret = ""
    for c in chars:
        ret += c

    return ret


def break_caesar(symbols):
    german_freqs = {'e': 17.4, 'n': 9.78, 'i': 7.55, 's': 7.27,
                    'r': 7, 'a': 6.51, 't': 6.15, 'd': 5.08,
                    'h': 4.76, 'u': 4.35, 'l': 3.44, 'c': 3.06,
                    'g': 3.01, 'm': 2.53, 'o': 2.51, 'b': 1.89,
                    'w': 1.89, 'f': 1.66, 'k': 1.21, 'z': 1.13,
                    'p': 0.79, 'v': 0.67, 'j': 0.27, 'y': 0.04,
                    'x': 0.03, 'q': 0.02}

    possible_keys = {}
    for i in range(26):
        caesar_candiate = decrypt(char_list_to_str(symbols), chr(i + ord('a')))
        s_freq = most_frequent_symbols(caesar_candiate)
        error = 0
        for s in s_freq.keys():
            error += s_freq[s] * german_freqs[s] / 100

        possible_keys[chr(i + ord('a'))] = error

    return {key: value for key, value in sorted(possible_keys.items(),
                                                key=lambda item: item[1], reverse=True)}


def decrypt(cypher, key):
    plaintext = ""
    key_chain = key
    num_concat = math.ceil(len(cypher) / len(key))
    for i in range(num_concat - 1):
        key_chain += key

    key_chain = key_chain[:len(cypher)]

    for c, k in zip(cypher, key_chain):
        c_num = ord(c) - ord('a')
        k_num = ord(k) - ord('a')
        tmp = (c_num - k_num)
        if tmp < 0:
            tmp += 26
        plaintext += chr(tmp + ord('a'))

    return plaintext


def main():
    cypher = "xipytdqgyxomprhanfllmwv" \
             "lgeigahhqgyxoqgiheaeotqbku" \
             "lpqpldzxhotfbyhkemdploqgotlzgu" \
             "tnpilplkjzxyakuwfvfzvsqerxtpphnqlklkpqul"
    triplets = find_triplets(cypher)
    val_trips, diffs = calc_triplet_diffs(triplets)
    print("Following triples exist multiple times:")
    print(val_trips)
    print("The distances between these triplets are")
    print(diffs)
    key_len = ggt_list(diffs)
    print("Therefore the most likely key length is %s" % key_len)

    print("Analysis of the symbol frequencies yields following possible keys:")
    caesar_keys = analyze_symbol_frequency(cypher, key_len)

    print("most likely")
    print([list(ck.keys())[0] for ck in caesar_keys])
    print("second most likely")
    print([list(ck.keys())[1] for ck in caesar_keys])
    print("One can easily see that the keyword must be 'licht'.")
    print("The decrypted text is:")
    print(decrypt(cypher, "licht"))


if __name__ == '__main__':
    main()
