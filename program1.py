import bisect
import re

def better_solution(random_word, wordlist, dictionary):
    # 入力された単語をソートして、二分探索する
    # dictionary.txtにおけるインデックスをidxに格納
    sorted_random_word = ''.join(sorted(random_word))
    idx = bisect.bisect(dictionary,sorted_random_word)
    
    # anagramが複数ある場合を考えて、リストにしておく
    anagram = list()
    for i in range(10):
        # #以降の部分がkeyになる
        # keyはwords.txtにおけるインデックスだから、keyを基準に元の文字列を探す
        key = re.sub(r'\D', '', dictionary[idx+i])
        cdd = wordlist[int(key)].rstrip('\n')
        
        # 実際にanagramともとの文字列が一致するか確認する
        sorted_anagram = ''.join(sorted(cdd))
        print(sorted_anagram)
        if sorted_random_word == sorted_anagram:
            anagram.append(cdd)
        else:
            break
    return anagram


d = open('dictionary.txt', 'r')
dictionary = d.readlines()
f = open('words.txt', 'r')
wordlist = f.readlines()
while True:
    s = input()
    # 0を入力したら終了とする
    if s != '0':
        ans = better_solution(s, wordlist, dictionary)
        print(ans)
    else:
        break

d.close()
f.close()