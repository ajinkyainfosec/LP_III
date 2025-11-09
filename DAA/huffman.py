import heapq
from collections import Counter, namedtuple

# Define a node structure
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(text):
    # Step 1: Frequency of each character
    freq = Counter(text)

    # Step 2: Create priority queue (min-heap)
    heap = [Node(ch, fr, None, None) for ch, fr in freq.items()]
    heapq.heapify(heap)

    # Step 3: Combine nodes until one remains
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    # Step 4: Generate Huffman codes
    huffman_codes = {}
    def generate_codes(node, code=""):
        if node.char:
            huffman_codes[node.char] = code
            return
        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    root = heap[0]
    generate_codes(root)

    # Step 5: Encode the text
    encoded_text = ''.join(huffman_codes[ch] for ch in text)

    return huffman_codes, encoded_text


# Main Program
text = input("Enter the text to encode: ")
codes, encoded = huffman_encoding(text)

print("\nCharacter Huffman Codes:")
for ch in codes:
    print(f"{ch}: {codes[ch]}")

print(f"\nEncoded String: {encoded}")
