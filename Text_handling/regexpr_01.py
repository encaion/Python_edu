import re
match = re.search("[0-9]{3}", "abc123")
match.group()
match.start()
match.end()

tt = ["a12312b", "a123b", "asdd"]
[re.sub("[0-9]", "", s) for s in tt]
