#               #
#   TOKENIZER   #
#               #

text = 'Die Auflösung der römischen Tetrarchie war der Prozess in der römischen Geschichte, der in den Jahren 306–324 zum Ende des von Kaiser Diokletian begründeten Vierkaisersystems führte. Als 306 der bisherige Oberkaiser (Augustus) Constantius Chlorus starb, riefen seine Truppen seinen Sohn Konstantin zum Kaiser aus.'
tokens = list(text.encode('utf-8'))

def _get_stats(ids):
    counts = {}
    for pairs in zip(ids, ids[1:]):
        counts[pairs] = counts.get(pairs, 0) + 1 # counts how often each pair exisits in text
    return counts

def merge(ids, pair, idx):
    newIDs = []
    i = 0
    while i < len(ids):
        if i < len(ids) -1 and ids[i] == pair[0] and ids[i+1] == pair[1]: # not last position and next position is equal pair
            newIDs.append(idx)
            i += 2
        else:
            newIDs.append(ids[i])
            i += 1

    return newIDs


vocab_size = 276
num_merges = vocab_size - 256
ids = list(tokens)

merges = {}
for i in range(num_merges):
    stats = _get_stats(ids)
    pair = max(stats, key=stats.get)
    idx = 256 + i
    print(f"merging {pair} into ({idx})")
    ids = merge(ids, pair, idx)
    merges[pair] = idx


print(tokens)
print(merges)
print(ids)


