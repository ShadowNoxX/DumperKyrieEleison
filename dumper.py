# CONFIGURATION PLEASE EDIT THESE VALUES
CIPHER = ""
MINLENGTH = 0
MAXLENGTH = 99999999

# ONLY EDIT IF YOU KNOW WHAT YOU ARE DOING
from time import time
i = 1
attempt = 1
results = []
strings = "abcdefghijklmnopqrstuvwxyz0123456789"
start = time()
def decrypt(text: str, key: int):
    n = key
    while True:
        if n % 4 == 0:
            break
        n += 1
    d = 3
    t = ""
    r = ""
    while True:
        if len(
                text
        ) <= n:
            break
        t = text[n]
        text = text[n +
                    1:]  
        r += chr(
            ord(t) -
            d)
    return r
def _kyrie(text: str):
        r = ""
        for char in text:
            if char in strings:
                i = strings.index(char)+1
                if i >= len(strings):
                    i = 0
                char = strings[i]
            r += char
        return r
def _decrypt(text, key):
    decrypted = decrypt(text, key)
    return _kyrie(decrypted)
result = _decrypt(CIPHER, i)
while result != "":
    result = _decrypt(CIPHER, i)
    if len(result) >= MINLENGTH and len(result) <= MAXLENGTH:
        results.append(result)
        attempt += 1
    i += 4
end = time()
elapsed = end - start
with open("dumped.txt", 'w') as f:
    for r in results:
        f.write(r + "\n")
print(f"Dumped in {elapsed} seconds with {attempt} results")