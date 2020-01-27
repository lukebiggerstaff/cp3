from collections import defaultdict

def nd():
    return defaultdict(nd)

def make_trie(words):
    t = nd()
    curr = t
    for word in words:
        for char in word:
            curr[char]
            curr = curr[char]
        curr['_end']
        curr = t
    return t

def search_trie(trie, word):
    curr = trie
    for c in word:
        if c not in curr:
            return False
        curr = curr[c]
    return '_end' in curr

def insert(trie, word):
    curr = trie
    for c in word:
        curr[c]
        curr = curr[c]
    curr['_end']
    return t

if __name__ == '__main__':
    t = make_trie(['ball', 'bat', 'dad'])
    assert search_trie(t, 'bal') == False
    assert search_trie(t, 'ball') == True

    assert search_trie(t, 'cat') == False
    insert(t, 'cat')
    assert search_trie(t, 'cat') == True