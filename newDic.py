# 宿題1に使う辞書を作るプログラム
# 辞書の中の全単語に対して単語内でソートして、単語の後にインデックスを書いておく
# 次に、辞書をソートして、dictionary.txtに保存する。

f = open('words.txt', 'r')
wordlist = f.readlines()
new_f = open('dictionary.txt', 'a')
new_wordlist = list()
keys = [i for i in range(len(wordlist))]

# 全単語に対して単語内でソート
for word in wordlist:
    new_str_list = sorted(word.rstrip('\n'))
    new_word = ''.join(new_str_list)
    new_wordlist.append(new_word)
 
# dictをつくる
# (aはwords.txtで1番目だから、keyは0)   
d = dict(zip(keys,new_wordlist))
# 辞書をソート
new_dic = sorted(d.items(), key=lambda x:x[1])
#print(dic)

# keyを各文字列の後に書いておく(a#0というように)
for word in new_dic:
    new_f.write(word[1] + '#' + str(word[0]) + '\n')

f.close()
new_f.close()

    