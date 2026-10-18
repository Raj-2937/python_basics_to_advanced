# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# Coding:

# if the word contains atleast 3 characters, remove the first letter and append it at the end

# now append three random characters at the starting and the end

# else:

# simply reverse the string

# Decoding:

# if the word contains less than 3 characters, reverse it

# else:

# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.






import random

chars = "abcdefghijklmnopqrstuvwxyz"
message = str(input("write your code massage here: "))
print("Original:", message)

# --- ENCODING ---
encoded_words = []
for w in message.split():
    if len(w) >= 3:
        r1 = random.choice(chars) + random.choice(chars) + random.choice(chars)
        r2 = random.choice(chars) + random.choice(chars) + random.choice(chars)
        encoded_words.append(r1 + w[1:] + w[0] + r2)
    else:
        encoded_words.append(w[::-1])

encoded_msg = " ".join(encoded_words)
print("Encoded:", encoded_msg)

# --- DECODING ---
decoded_words = []
for w in encoded_msg.split():
    if len(w) < 3:
        decoded_words.append(w[::-1])
    else:
        core = w[3:-3] # Removes the 3 random letters from start and end
        decoded_words.append(core[-1] + core[:-1])

print("Decoded:", " ".join(decoded_words))
