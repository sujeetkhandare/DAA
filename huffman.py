import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    heap = [Node(char, freq) for char, freq in Counter(data).items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    build_huffman_codes(root.left, current_code + '0', codes)
    build_huffman_codes(root.right, current_code + '1', codes)

def huffman_encoding(data):
    if not data:
        return None, None

    root = build_huffman_tree(data)

    codes = {}
    build_huffman_codes(root, '', codes)

    encoded_data = ''.join([codes[char] for char in data])
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return None

    current = root
    decoded_data = ''
    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_data += current.char
            current = root

    return decoded_data

if __name__ == "__main__":
    input_data = "this is an example for huffman encoding"
    
    # Huffman encoding
    encoded_data, huffman_tree = huffman_encoding(input_data)

    print("Input data:", input_data)
    print("Encoded data:", encoded_data)

    # Huffman decoding
    decoded_data = huffman_decoding(encoded_data, huffman_tree)

    print("Decoded data:", decoded_data)
