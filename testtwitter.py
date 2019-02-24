from konlpy.tag import Twitter
twitter = Twitter()
a='책가방을메고 학교에가서 공부를 하자'
b = '우리나라 금수강산 이라서 그런가 금수저가 많네요'
mo = twitter.morphs(a)
mo2 = twitter.morphs(b)
po = twitter.pos(a)


ta =[]
ta.append(mo)
ta.append(mo2)

print(ta)
print(len(ta))

for word, tag in ta:
    print(word)
    print(tag)

