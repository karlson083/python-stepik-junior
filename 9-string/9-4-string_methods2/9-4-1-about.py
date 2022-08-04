import os
clear = lambda: os.system('cls')
clear()

s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ

s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('baz'))

s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))


s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))

s = '     foo bar foo baz foo qux      '
print(s.strip())


s = '     foo bar foo baz foo qux      '
print(s.lstrip())


s = '      foo bar foo baz foo qux      '
print(s.rstrip())

s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))


s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))

s = 'aabbAAccDDaa'
s = s.lower()
print(s.count('a'))

s = 'www.stepik.org'
print(s.startswith('www'))

s = 'www.stepik.org'
print(s.endswith('.ru'))

s = 'I learn Python language. Python - awesome!'
print(s.find('Python'))

s = '     I learn Python language               '
print(s.strip())

s = 'abcdababa'
print(s.replace('ab', '123'))