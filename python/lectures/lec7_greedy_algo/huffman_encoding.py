from heapq import *
from typing import Union

class Node:
    def __init__(self, val: tuple):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __lt__(self, other) -> int:
        return self.val > other.val
    
    def __repr__(self):
        return str(self.val)

# Overall TC: O()
def huffman_encoding(char_freqs: dict[str, int]) -> dict[str, str]:

    # TC: O(n) (heapify can be done in O(n) time)
    minheap = [(freq, Node((char,))) for char, freq in char_freqs.items()]
    heapify(minheap)

    # We pop the 2 least frequency characters/grouped characters and push their combined tuple back onto the minheap
    # We terminate when there is only 1 element left (base case)
    # O(nlogn) (each heappop is O(logn), we decrease the size of the heap by 1 each time, hence the stated time complexity)
    while len(minheap) > 1:
        f1, n1 = heappop(minheap)
        f2, n2 = heappop(minheap)
        t = Node(n1.val + n2.val)
        t.left, t.right = n1, n2
        heappush(minheap, (f1 + f2, t))

    _, tree = minheap[0]
    encoding = dict()
    # This is for recursive backtracking to get the encoding of each character
    def dfs(
        curr_node: Node,
        curr_encoding: list[str],
        encoding: dict[str, str]
    ):
        if curr_node.is_leaf():
            encoding[curr_node.val[0]] = ''.join(curr_encoding)
            return

        curr_encoding.append('0')
        dfs(curr_node.left, curr_encoding, encoding)
        curr_encoding.pop()

        curr_encoding.append('1')
        dfs(curr_node.right, curr_encoding, encoding)
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