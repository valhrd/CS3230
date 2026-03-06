from heapq import *
from typing import Union

# Overall TC: O()
def huffman_encoding(char_freqs: dict[str, int]) -> dict[str, str]:

    # TC: O(n) (heapify can be done in O(n) time)
    n = len(char_freqs)
    minheap = [(freq, char) for char, freq in char_freqs.items()]
    heapify(minheap)
    h = {}

    # We will use a "flattened" representation of a tree instead of defining a Node struct/class
    # Since each non-leaf node as exactly 2 children, we can represent a tree as a series of nested tuples
    # Example: ('a', (('b', 'c'), ('d', 'e'))) would represent:
    #      () 
    #    /    \
    #   a     ()
    #       /    \
    #     ()      ()
    #    /  \    /  \
    #   b    c  d    e
    #
    # We pop the 2 least frequency characters/grouped characters and push their combined tuple back onto the minheap
    # We terminate when there is only 1 element left (base case)
    # O(nlogn) (each heappop is O(logn), we decrease the size of the heap by 1 each time, hence the stated time complexity)
    while len(minheap) > 1:
        f1, c1 = heappop(minheap)
        f2, c2 = heappop(minheap)
        t = (c1, c2)
        heappush(minheap, (f1 + f2, t))
    
    _, tree = minheap[0]
    encoding = dict()
    # This is for recursive backtracking to get the encoding of each character
    def dfs(
        curr_node: Union[tuple, str],
        curr_encoding: list[str],
        encoding: dict[str, str]
    ):
        if isinstance(curr_node, str):
            encoding[curr_node] = ''.join(curr_encoding)
            return

        curr_encoding.append('0')
        dfs(curr_node[0], curr_encoding, encoding)
        curr_encoding.pop()

        curr_encoding.append('1')
        dfs(curr_node[1], curr_encoding, encoding)
        curr_encoding.pop()
    
    dfs(tree, [], encoding)
    return encoding

if __name__ == '__main__':#
    from collections import Counter
    from pprint import pprint

    CORPUS = 'resources/sample.txt'
    CHARACTERS = set(chr(ord('a') + i) for i in range(26))
    # Get frequencies of characters
    with open(CORPUS, 'r') as f:
        text = f.read().lower()
        frequencies = Counter(text)
    
    char_freqs = {char: freq for char, freq in frequencies.items() if char in CHARACTERS}

    # Class example for verification, comment out if you want to use the frequency of letters from the resources subfolder
    char_freqs = {
        'a': 0.45,
        'b': 0.18,
        'c': 0.15,
        'd': 0.12,
        'e': 0.10,
    }
    pprint(huffman_encoding(char_freqs))