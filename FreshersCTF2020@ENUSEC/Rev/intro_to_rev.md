## Rev

# Intro to Rev(erse engineering)

## Problem

A file! Let's download it!

![2](../images/intro_to_rev_2.png)

If we go and type into a terminal `file IntroToRev`, we see the creator gave us an executable. Let's crack it open!

## Solution

There are 2 possible easy solutions for this challenge I can think of.

### Solution 1: `strings`

`strings` will extract all the text strings out of the executable. We just need to call it issuing `strings IntroToRev` in a terminal and we get our flag

![1](../images/intro_to_rev_3.png)

### Solution 2: `Disassemble`

Open the file in a disassembler like IDA and check the hex!!

![3](../images/intro_to_rev.png

`FCTF{you_can_still_see_me}`

Go back to [Rev](./)


 
