import heapq

class BinaryTree:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

class HuffmanCoding:
    def __init__(self, text):
        self.text = text
        self.root = None

    def __frequency_of_chars(self, text):
        freq_dict = {}
        for char in text:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        return freq_dict

    def __build_tree(self, text):
        counter = self.__frequency_of_chars(text)
        pq = [BinaryTree(char, counter[char]) for char in counter]
        heapq.heapify(pq)
        while len(pq) > 1:
            left = heapq.heappop(pq)
            right = heapq.heappop(pq)
            parent = BinaryTree(None, left.frequency + right.frequency, left, right)
            heapq.heappush(pq, parent)
        return heapq.heappop(pq)

    def __build_map(self, root):
        def dfs(root, code, encoding_map):
            if root.char:
                encoding_map[root.char] = "".join(code)
            else:
                code.append('0')
                dfs(root.left, code, encoding_map)
                code.pop()
                code.append('1')
                dfs(root.right, code, encoding_map)
                code.pop()
        encoding_map = {}
        dfs(root, [], encoding_map)
        return encoding_map

    def __encode(self):
        self.root = self.__build_tree(self.text)
        encoding_map = self.__build_map(self.root)
        return ''.join([encoding_map[char] for char in self.text])

    def __decode(self, encoded, root):
        if root.char:
            return root.char * len(encoded)
        decoded = []
        node = root
        for bit in encoded:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            if node.char:
                decoded.append(node.char)
                node = root
        return ''.join(decoded)

    def __build_padded_text(self, encodedText):
        paddingValue = 8 - len(encodedText) % 8
        for i in range(paddingValue):
            encodedText += '0'
        paddedInfo = '{0:08b}'.format(paddingValue)
        paddedText = paddedInfo + encodedText
        return paddedText

    def __build_byte_array(self, paddedText):
        array = []
        for i in range(0, len(paddedText), 8):
            byte = paddedText[i:i + 8]
            array.append(int(byte, 2))
        return array

    def compress(self):
        encodedText = self.__encode()
        paddedText = self.__build_padded_text(encodedText)
        bytesArray = self.__build_byte_array(paddedText)
        finalBytes = bytes(bytesArray)
        return finalBytes

    def __remove_padding_from_text(self, text):
        padded_info = text[:8]
        padding_value = int(padded_info, 2)
        text = text[8:]
        text = text[:-1 * padding_value]
        return text

    def decompress(self, compressed_data):
        bit_string = ''
        for byte in compressed_data:
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
        text = self.__remove_padding_from_text(bit_string)
        actual_text = self.__decode(text, self.root)
        return actual_text
