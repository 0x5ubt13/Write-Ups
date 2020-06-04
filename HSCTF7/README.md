# XORed write up

Hello, here's how I solved the XORed challenge for 100 points using python3:

## They provide us with the following problem:
```
I was given the following equations. Can you help me decode the flag?
Key 1 = 5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533
Key 1 ^ Key 3 = 9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b
Key 2 ^ Key 3 ^ Key 5 = 557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05
Key 1 ^ Key 4 ^ Key 5 = 7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb
Key 3 ^ Key 4 = 996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a
Flag ^ Key 1 ^ Key 2 ^ Key 3 ^ Key 4 ^ Key 5 = 306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139
```
### Solution:

1. Firstly, we need to convert the **hex strings** into **decimal integers**. For that we have the python3 command `int([hex string],16)`
In order to automate the process, we can declare all the strings as variables and use a for loop to have a dedicated list:

```python3
keys2 = []
for key in keys:
  keys2.append(int(key,16))
```

2. Then we must perform XOR operations in order to retrieve the original strings since XOR can be reversed by using XOR again. More info here: `https://stackoverflow.com/questions/14279866/what-is-inverse-function-to-xor`

3. Once we have all the keys we get the flag in decimal format. We need to parse it into hex again using `hex()` and then decode it using `bytes.fromhex('').decode('utf-8')`

4. We print the flag and submit it! 100 points.
