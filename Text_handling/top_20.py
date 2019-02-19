f = open("naver_source_190204.txt")
lines = f.readlines()
f.close()

[s.split("<")[1].split(">")[1] for s in lines if "ah_k" in s]
