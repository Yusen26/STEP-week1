
def better_solution(random_word, count_dic):
    # 入力された文字列の各alphabetの出現回数をカウントして
    # 同じように新しい文字列を作る
    # cake --> a1c1e1k1
    # これをword_infoに格納
    alphabets = list(set(random_word))
    sorted_alphabets = sorted(alphabets)
    word_info = ""
    for alphabet in sorted_alphabets:
        count = random_word.count(alphabet)
        word_info = word_info + alphabet + str(count)
    
    start = '#'
    end = '$'
    for word in count_dic:
        i = 0
        flag = True
        # 辞書の中の全単語の#までの文字をチェックして
        # 全てword_infoに含まれていて、かつ、各文字のcountがword_infoのcount以下になれば
        # その単語のwords.txtにおけるindexを調べる
        # point高い順の並んでいるため、順番に探して最初に当てはまったものがpoint最大になる
        while word[i] != '#':
            if word[i] not in word_info:
                flag = False
                break
            else:
                index = word_info.index(word[i])
                if int(word[i+1]) > int(word_info[index+1]):
                    flag = False
                    break
            i+=2
        if flag:
            # indexは#以降$より前の部分
            a = word.index(start)
            b = word.index(end)
            idx = word[a+1:b]
            return int(idx)

d = open('count_dic2.txt', 'r')
count_dic = d.readlines()
f = open('words.txt', 'r')
wordlist = f.readlines()

input_f = open('large.txt', 'r')
input = input_f.readlines()
output = open('answer_large.txt', 'a')

for word in input:     
    idx = better_solution(word.rstrip('\n'), count_dic)
    print(wordlist[idx])
    output.write(wordlist[idx])

