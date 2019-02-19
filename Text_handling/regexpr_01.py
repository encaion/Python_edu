import re
match = re.search("[0-9]{3}", "abc123")
match.group()
match.start()
match.end()

tt = ["a12312b", "a123b", "asdd"]
[re.sub("[0-9]", "", s) for s in tt]

s_sub = []
for s in tt:
    ss = re.search("a.*?b", s)
    if ss != None:
        s_sub.append(ss.group())
s_sub
