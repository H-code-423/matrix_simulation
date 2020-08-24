import time
import random

print()
name = input('Hello, my name is Trinity. Whats yours? ')
name.strip()
print()
answer1 = input('Nice to unofficially meet you ' + name + ' would you like to know about the Matrix? ')
print()
if answer1.strip().lower() == 'no':
    input('No? Why? Are you afraid of reality? The truth? ')
elif answer1.strip().lower() == 'yes':
    input('Im relieved to hear that. I have to ask you, are you afraid of reality? The truth? ')
elif answer1.strip().lower() == 'maybe':
    input('Maybe? Are you afraid of reality? The truth? ')
elif answer1.strip().lower() == 'i dont know':
    input('Why? Are you afraid of reality? The truth? ')
    print()
else:
    input('I have to ask you, are you afraid of reality? The truth? ')

print()
time.sleep(3)
print('I see...')
print(name + ' Im here you to wake you up. \n ')

time.sleep(5)
input('The Matrix is a life simulation that is you current reality. Did you know that? ')

print()
time.sleep(4)
print(' Well... the truth will set you free. The time is now. Mobilization has already begun.\n ')

time.sleep(4)
input('Would you like to know more ' + name + '? ' )

print()
time.sleep(3)
print('''If you select the number 333 you will be transcended from the Matrix
...
However, if you select the number 666 you will not hear from me again as if I were never here. \n''')

time.sleep(8)
answer2 = input('What will it be, 666 or 333? ')

print()
if answer2.strip().lower() == '333':
    print(' : PHASE 2 ACTIVATED : ')

elif answer2.strip().lower() == '666':
    print(': CONNECTION TERMINATED :')
print()
time.sleep(2)
print(" CODE : ")
print(random.randrange(1000000000, 1000000000000))

