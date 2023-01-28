import sys
import random

i = 10

def swap_random(seq):
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]

with open("./3000word.txt", "r") as r:
    wordlist = r.read().split("\n")

with open("./3000word-th.txt", "r") as r:
    wordlist_th = r.read().split("\n")


# wordlist = wordlist[:700]
# print(wordlist)

if(len(sys.argv)>1):
    i = int(sys.argv[1])
    
questions = random.choices(wordlist, k=i)

score = 0
print("="*40)
print(f"เริ่มทดสอบ {len(questions)} ข้อ")
print("="*40)

for i in range(len(questions)):
    print(f"{i+1}. {questions[i]} แปลว่า?")
    correct_answer = wordlist_th[wordlist.index(questions[i])]
    choices = random.choices(wordlist_th, k=3)
    choices.append(correct_answer)
    swap_random(choices)
    for i_choice in range(len(choices)):
        print(f" {str(i_choice+1)}) {choices[i_choice]}")
    answer = choices[int(input("กรอกคำตอบ(1-4): "))-1]
    print("*"*40)
    if(correct_answer == answer):
        print("ถูกต้องงงงง")
        score += 1
    else:
        print("ผิดจ้าาาาา")
        
    print("*"*40)

print(f"\nตอบถูก: {score} ข้อ")
    
    
