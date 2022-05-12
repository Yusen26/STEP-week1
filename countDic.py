# 宿題2に使う辞書(count_dic2.txt)を作るプログラム
# まず全単語に対して、各文字の出現回数を数えて、新しい文字列を作る
# 例えばitの場合、i1t1のようになる
# つぎにprogram1のときと同様に、インデックスを文字列の後に書いておく
# itはwords.txtでのインデックスが75184であるから、i1t1#75184
# 最後にpointも文字列に付け加える
# iもtも1pointだから、i1t1#75184$2

f = open('words.txt', 'r')
wordlist = f.readlines()
new_f = open('count_dic2.txt', 'a')
new_list = list()
values = list()
index = [i for i in range(len(wordlist))]
pri = ['jkqxz','bfgpvwy','cdlmu','aehinorst']

# 各単語のpointを計算して、words.txtと同じ順番にvaluesに格納
for word in wordlist:
    word = word.rstrip('\n')
    point = 0
    for i in word:
        for j in range(4):
            if i in pri[j]:
                point += 4-j
    values.append(point)

# 各alphabetの出現回数を数えて、文字列を作る
# words.txtと同じ順番にnew_listに格納
for word in wordlist:
    alphabets = list(set(word.rstrip('\n')))
    sorted_alphabets = sorted(alphabets)
    word_info = ""
    for alphabet in sorted_alphabets:
        count = word.count(alphabet)
        word_info = word_info + alphabet + str(count)
    #print(word_info)
    new_list.append(word_info)
    
# keyはindex,valueはカウントの文字列
# it --> i1t1#75184
# 新しい文字列はnew_list_with_indexに格納
d = dict(zip(index,new_list))
new_list_with_index = list()
for ind,word in d.items():
    new_list_with_index.append(word + '#' + str(ind))
  
# keyはnew_list_with_index,valueはpoint
# i1t1#75184 --> i1t1#75184$2
# 新しい文字列はnew_dに格納
new_d = dict(zip(new_list_with_index,values))

# new_dをpoint順にソート
new_dic = sorted(new_d.items(), key=lambda x:x[1], reverse=True)
for word in new_dic:
    new_f.write(word[0] + '$' + str(word[1]) + '\n')

f.close()
new_f.close()
    
    