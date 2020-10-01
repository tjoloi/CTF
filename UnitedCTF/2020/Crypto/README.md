# Cryptography

### Challenges

- [Data Format](#data-format)
- [Le flag de Jules](#le-flag-de-jules)
- [Celui de Vigenère](#celui-de-vigenère)
- [Le XOR](#le-xor)
- [AES Client](#aes-client)
- [AES CTR](#aes-ctr)
- [AES ECB Cut & Paste](#aes-ecb-cut--paste)
- [AES ECB Byte par byte](#aes-ecb-byte-par-byte)

### Data Format

[Link to challenge on github](https://github.com/UnitedCTF/UnitedCTF-2020/tree/master/challenges/crypto/data-format)

The point of this challenge was to make us work with hex and base64 encodings. The challenge was to somehow implement this pseudo code:

`DECODE_HEX("464c4147") + DECODE_BASE64("LTQ5NGM2Zjc2NjU0NDYxNw==") + ENCODE_BASE64("461466f72") + ENCODE_HEX("6174730a")`

Which, in python, is:

`unhexlify("464c4147") + b64decode("LTQ5NGM2Zjc2NjU0NDYxNw==") + b64encode("461466f72".encode()) + hexlify("6174730a".encode())`

The resulting flag was `FLAG-494c6f766544617NDYxNDY2Zjcy3631373437333061`

### Le flag de Jules

[Link to challenge on github](https://github.com/UnitedCTF/UnitedCTF-2020/tree/master/challenges/crypto/julius)

The challenge gave us a flag encrypted using [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) with an unknown n value. To solve the challenge, I used my caesar function from my [common_ciphers.py](https://github.com/tjoloi/CTF/blob/master/CTF-tools/Crypto/common_ciphers.py) file and decrypted using n values from 0 to 25.

At every iteration, we check if the decrypted value had `FLAG-` in it to find the right n value.

The resulting flag was `FLAG-VENIVIDIVICI`\
With n value being `23`

### Celui de Vigenère

[Link to challenge on github](https://github.com/UnitedCTF/UnitedCTF-2020/tree/master/challenges/crypto/vigenere)

The challenge gave us a flag encrypted using [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) with an unknown key of length 4. To solve the challenge, I used my vigenere function from my [common_ciphers.py](https://github.com/tjoloi/CTF/blob/master/CTF-tools/Crypto/common_ciphers.py) file and decrypted the first 4 chars using every combination of 4 letters possible.

At every key combination, we try to see if the result is `FLAG` if it is, we decrypt the entire flag using that key.

The resulting flag was `FLAG-CAESARGOTNOTHINGONTHIS`\
With the key being `EZPZ`

### Le XOR

[Link to challenge on github](https://github.com/UnitedCTF/UnitedCTF-2020/tree/master/challenges/crypto/xor1)

The challenge gave us the current base64 encoded string `ERsWEHoYOQcyIiMWIiQkPhE2ND47MjoyOSMVJSIjMjE4JTQyJQ==` and told us it was the flag encrypted with some XOR key.

To retrieve the key, we first xor the first 4 bytes of the encrypted flag with `FLAG`, which gives us `WWWW`. It is safe to assume that the key is simply `W` and is repeated to fit the length of the data to encrypt.

We then try to decrypt using our assumption, we successfully acquire the flag.

The resulting flag was `FLAG-OnPeutAussiFacilementBruteforcer`

### AES Client

[Link to challenge on github](https://github.com/UnitedCTF/UnitedCTF-2020/tree/master/challenges/crypto/aes-client)

The goal was to implement aes encryption so I did using the pycryptodome library. Pretty straight forward challenge.

The resulting flag was `FLAG-0d4c39fa0c7c1d167d4bd20064a6053f`

### AES CTR

[Link to challenge on github](https://github.com/UnitedCTF/UnitedCTF-2020/tree/master/challenges/crypto/aes-ctr)

The vulnerability here was that the key and nonce were generated at the start of the session and the counter was always reset to 0 so every encryption had the same exact parameters.

The actual exploit is explained in great detail when calling the function `ctr_same_key_nonce(help=True)` from my [aes.py](https://github.com/tjoloi/CTF/blob/master/CTF-tools/Crypto/aes.py) file but the jist of it is that we can ask the server to encrypt something at least the same length of the flag and, using that and the known plaintext of that something, we can retrieve the original flag.

The resulting flag was `FLAG-2b38737dbe6bdbc0db6d35c9689e5155`

### AES ECB Cut & Paste

[Link to challenge on github](https://github.com/UnitedCTF/UnitedCTF-2020/tree/master/challenges/crypto/aes-ecb-cut-paste)

By reading the server and testing it, we realise quickly that the main goal of the challenge is to make it decrypt a "cookie" with it's `flag` value changed to `True` instead of `False`.

To achieve so, we build our payload so that the data we send to the server to encrypt is split in 4 specific blocks

- _B1_: Pad with `0`s to isolate "name="  -> name={0\*11}
- _B2_: pad('True'.encode(), 16)
- _B3_: Pad with `0`s to isolate "&flag=" -> {0\*10}&flag=
- _B4_: the remaining "False"

Then we send to the server `B1+B3+B2` in this order.

This will replace the `False` for a `True` and we can simply discard the last block. When decrypting, the server will read these values
```
name = "{0*21}"
flag = "True"
```

The resulting flag was `FLAG-32c2a2f6befcf9bb7ad9e9e359e550b2`

### AES ECB Byte par byte

WIP