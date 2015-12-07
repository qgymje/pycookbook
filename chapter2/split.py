import re

line = 'asdf fjkl; afed, fjek,asdf,    foo'
print(re.split(r'[;,\s]\s*', line))
