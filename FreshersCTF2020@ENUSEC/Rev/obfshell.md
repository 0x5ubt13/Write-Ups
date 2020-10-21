## Rev challenges

# Obfshell

## Problem

We get a .ps1 script which doesn't apparently do anything.

## Solution

Looking into the obfuscated code, once we arrange it, we detect a suspicious encoded string of text.

![1](../images/obfshell_1.png)

It looked like hex to me, so I went ahead and tried to decode it.

![2](../images/obfshell_2.png)

Go back to [Rev](./)
