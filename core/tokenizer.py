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

def decode(ids):
    tokens = b"".join(vocab[idx] for idx in ids)
    return tokens.decode('utf-8', errors='replace')

def encode(text):
    tokens = text.encode('utf-8')
    while True:
        stats = _get_stats(tokens)
        pair = min(stats, key=lambda p: merges.get(p, float('inf')))
        if pair not in merges:
            break # nothing else can be merged
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)
    return tokens






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

vocab = {idx: bytes([idx]) for idx in range(256)}
for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1] # byte objects


print(tokens)
print(merges)
print(ids)
print(decode(ids))
print(decode(encode("h")))

