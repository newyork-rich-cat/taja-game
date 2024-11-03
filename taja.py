import random
import time
from nltk.corpus import words
import nltk
from googletrans import Translator
w = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
alphabet = [chr(i) for i in range(97, 123)]

nltk.download('words')
translator = Translator()
def make_q():
    word_list = words.words()
    word = random.choice(word_list)
    trans = translator.translate(word, src = 'en', dest = 'ko')
    return word + " "+ trans.text

n = 1
print("[타자 게임]준비되면 엔터!")
input()
start = time.time()
q = make_q()
while n <= 5:
    
    print("*문제",n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n = n + 1
        q = make_q()
    else:
        print("오타! 다시 도전! ㅋㅋㅋ 이걸 어떻게 틀리냐 인간 ㅋ.")
        
end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간:",et,"초")
 