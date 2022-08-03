import os
clear = lambda: os.system('cls')
clear()


s = 'foO BaR BAZ quX'
print(s.capitalize())

s = 'foo123#BAR#.'
print(s.capitalize())

s = 'FOO Bar 123 baz qUX'
print(s.swapcase())

s = 'the sun also rises'
print(s.title())

s = "what's happened to ted's IBM stock?"
print(s.title())

s = 'FOO Bar 123 baz qUX'
print(s.lower())

s = 'FOO Bar 123 baz qUX'
print(s.upper())

s = 'i Learn Python language'
print(s.capitalize())

s = 'i LEARN Python LAnguaGE'
print(s.lower())

s = '$12344%^$#@!'
print(s.lower())

s1 = 'a'
s2 = s1.upper()
print(s1, s2)

s = 'i LEARN Python LAnguaGE'
print(s.upper())

s = 'i LEARN Python LAnguaGE'
print(s.swapcase())