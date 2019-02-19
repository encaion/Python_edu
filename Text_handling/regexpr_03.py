import re
import pandas as pd

# 실습데이터 만들기
text1 = "1234 asdfASDF  ㄱㄴㄷㄹㅏㅑㅓㅕ가나다라   .!@#"
text2 = "<a> <ab> <abc> <abcd>"
text3 = pd.Series(["aaa", "bbb", "ccc", "abc"])

# text1
# 숫자 치환
re.sub(pattern = "[0-9]", repl = "@", string = text1)

# 영문 치환
# __ 소문자 치환
re.sub(pattern = "[a-z]", repl = "@", string = text1)

# __ 대문자 치환
re.sub(pattern = "[A-Z]", repl = "@", string = text1)

# 한글 치환
# __ 자음 치환
re.sub(pattern = "[ㄱ-ㅎ]", repl = "@", string = text1)

# __ 모음 치환
re.sub(pattern = "[ㅏ-ㅣ]", repl = "@", string = text1)

# __ 완성형 치환
re.sub(pattern = "[가-힣]", repl = "@", string = text1)

# 띄어쓰기 치환
re.sub(pattern = " ", repl = "@", string = text1)
re.sub(pattern = "  ", repl = "@", string = text1)
re.sub(pattern = "   ", repl = "@", string = text1)

# 응용
# __ 숫자가 아닌 모든 문자 치환
re.sub(pattern = "[^0-9]", repl = "@", string = text1)

# __ 영문자가 아닌 모든 문자 치환
re.sub(pattern = "[A-z]", repl = "@", string = text1)

# __ 한글이 아닌 모든 문자 치환
re.sub(pattern = "[ㄱ-힣]", repl = "@", string = text1)

# __ 숫자와 영문 대문자가 아닌 모든 문자 치환
re.sub(pattern = "[0-9A-Z]", repl = "@", string = text1)

# __ 숫자 2, 3만 치환
re.sub(pattern = "[2-3]", repl = "@", string = text1)
re.sub(pattern = "[23]", repl = "@", string = text1)
re.sub(pattern = "2|3", repl = "@", string = text1)

# __ 숫자 2, 3, 4, 7, 8, 9 치환
re.sub(pattern = "[2-47-9]", repl = "@", string = text1)

# __ '.'의 치환
re.sub(pattern = ".", repl = "@", string = text1)
re.sub(pattern = "[.]", repl = "@", string = text1)
re.sub(pattern = "\.", repl = "@", string = text1)

# __ 두 칸 띄어쓰기와 세 칸 띄어쓰기의 치환
re.sub(pattern = "  |  ", repl = "@", string = text1)
re.sub(pattern = " {2}| {3}", repl = "@", string = text1)
re.sub(pattern = " {2,3}", repl = "@", string = text1)

re.sub(pattern = " {2,}", repl = " ", string = text1)

# __ "asdf"와 "가나다라" 치환
re.sub(pattern = "asdf|가나다라", repl = "@", string = text1)
re.sub(pattern = "asdf|[가-라]", repl = "@", string = text1)


# 특수문자내 문자 처리(text2)
# __ 모든 경우의 수 치환
re.sub(pattern = "<.*?>", repl = "@", string = text2)

# __ 내부 문자 1개 치환
re.sub(pattern = "<.>", repl = "@", string = text2)

# __ 내부 문자 2~4개 치환
re.sub(pattern = "<.{2,4}>", repl = "@", string = text2)

# 텍스트 조건(text3)
# __ "a"를 포함하는 원소 추출
text3.str.match(pat = "a")

# __ "b"를 포함하는 원소 추출
text3.str.match(pat = "b")

# __ "b"로 시작하는 원소 추출
text3.str.match(pat = "^a")

# __ "a"로 끝나는 원소 추출
text3.str.match("a$")
text3.str.match("^.*a$")

# __ "a"또는 "b"를 포함하는 원소 추출
text3.str.match(pat = "a|b")

