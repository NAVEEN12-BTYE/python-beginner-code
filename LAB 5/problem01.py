 
#01
s = "Hello World"
print(len(s))

#02
s = "python"
print(s.upper())

#03
s = "Education"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

#04
s = "OpenAI"
print(s[::-1])

#05
s = "madam"
clean = ""
for ch in s:
    if ch.isalnum():
        clean += ch.lower()
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#06
s = "hello"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

#07
s = "Python Programming"
print(s.replace(" ", "-"))

#08
s = "machinelearning"
sub = "learn"
print(sub in s)

#09
a = "Data"
b = "Science"
print(a + b)

#10
s = "Computer"
print(s[0], s[-1])

#11
s = "AI and ML and AI"
words = s.split()
count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print(count)

#12
import string
s = "Hello!!! How are you??"
result = ""
for ch in s:
    if ch not in string.punctuation:
        result += ch
print(result)

#13
s = "Deep learning improves computer vision"
words = s.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)

#14
a = "listen".replace(" ", "").lower()
b = "silent".replace(" ", "").lower()

if sorted(a) == sorted(b):
    print(True)
else:
    print(False)

#15
s = "programming"
seen = ""
for ch in s:
    if ch not in seen:
        seen += ch
print(seen)

#16
s = "Python is powerful and easy"
words = s.split()
words.sort()
print(" ".join(words))

#17
s = "abc"
subs = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        subs.append(s[i:j])
print(subs)


#18
s = "AI2025"
letters = 0
digits = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
print("Letters:", letters, "Digits:", digits)


#19
s = "12345"
print(s.isdigit())

#20
s = "Education"
vowels = "aeiouAEIOU"
result = ""
for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch
print(result)

      