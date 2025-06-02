# BPE (Byte Pair Encoding) Implementation

### what is BPE?

 BPE is a data compression technique that iteratively replaces the most frequent pair of bytes in a sequence with a single byte that does not occur in the sequence. It is commonly used in natural language processing for tokenization.

```python
pip install tiktoken
```
### Example usage of tiktoken for BPE tokenization
```python
import importlib
import tiktoken

print(importlib.metadata.version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")

text = ("Hello, do you like tea? <|endoftext|> In the Sunlit teraces." "of someUnknownPlace."
"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce non tempus lectus. Vestibulum vestibulum et velit a ultrices. Suspendisse libero ante, ornare in sem et, dictum rhoncus nibh. Phasellus dictum ac risus non lobortis. Praesent vel nibh id purus volutpat rhoncus. Pellentesque nec purus eros. Praesent lectus enim, pretium quis.")

integers = tokenizer.encode(text=text, allowed_special={"<|endoftext|>"})
print(integers)

```


### Output: 
`[15496, 11, 703, 389, 30, 0, 198, 262, 329, 0, 198, 262, 329]`