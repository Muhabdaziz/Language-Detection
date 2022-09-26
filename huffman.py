import random

def build_huffman_tree(letter_count):
    """ recieves dictionary with char:count entries
        generates a LIST structure representing
        the binary Huffman encoding tree"""
    queue = [(x, px) for x,px in letter_count.items()]
    while len(queue) > 1:
    # combine two smallest elements
        a, pa = extract_min(queue)   # smallest in queue
        b, pb = extract_min(queue)   # next smallest
        chars = [a,b]
        weight = pa+pb # combined weight
        queue.append((chars,weight)) # insert new node
        #print(queue)   # to see what whole queue is
        #print()
    x, px = extract_min(queue) # only root node left 
    return x

def extract_min(queue):
    P = [px for x,px in queue]
    return queue.pop(P.index(min(P)))

def generate_code(huff_tree, prefix=""):
    """ receives a Huffman tree with embedded encoding,
        and a prefix of encodings.
        returns a dictionary where characters are
        keys and associated binary strings are values."""
    if isinstance(huff_tree, str): # a leaf
        return {huff_tree: prefix}
    else:
        lchild, rchild = huff_tree[0], huff_tree[1]
        codebook = {}

        codebook.update( generate_code(lchild, prefix+'0'))
        codebook.update( generate_code(rchild, prefix+'1'))
        return codebook
    
def compress(text, encoding_dict):
  """ compress text using encoding dictionary """
  assert isinstance(text, str)
  return "".join(encoding_dict[ch] for ch in text if ord(ch)<128)


def build_decoding_dict(encoding_dict):
   """build the "reverse" of encoding dictionary"""
   return {y:x for (x,y) in encoding_dict.items()}
  # return {y:x for x,y in encoding_dict.items()} # OK too


def decompress(bits, decoding_dict):
   prefix = ""
   result = []
   for bit in bits:
      prefix += bit
      if prefix in decoding_dict:
          result.append(decoding_dict[prefix])
          prefix = ""
   assert prefix == "" # must finish last codeword
   return "".join(result)  # converts list of chars to a string


