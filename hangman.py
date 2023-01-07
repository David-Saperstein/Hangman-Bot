import re
last=''
wrong=0
guessed=''
def guess(input):
    regex='^'+input+'$'
    global last,wrong,guessed
    if not last=='' and not len(regex)==len(last):
        return 'yy'
    if regex==last:
        wrong+=1
    possiblewords=''
    with open('words_alpha.txt','r') as words:
        for word in words:
            result=re.match(regex,word)
            if result:
                if guessed=='':
                    possiblewords=possiblewords+word[0:-1]
                else:
                    for x in range(len(input)):
                        if input[x]=='.':
                            test=re.match('['+guessed+']',word[x])
                            if test:
                                break
                        if x==len(input)-1:
                            possiblewords=possiblewords+word[0:-1]
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    count = [0] * 256

    # Utility variables
    max = -1
    c = ''

    # Traversing through the string and maintaining the count of
    # each character
    if len(possiblewords)==len(input):
        return possiblewords
    if possiblewords=='':
        return 'zz'
    for i in possiblewords:
        if guessed=='':
            count[ord(i)]+=1
        else:
            if not re.match('['+guessed+']',i):
                count[ord(i)]+=1

    for i in possiblewords:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i
    last=regex
    guessed=guessed+c
    print('')
    print(c)
    return c
while True:
    x=input(': ')
    pop=guess(x)
    if len(pop)>1:
        if pop=='zz':
            print("I'm sorry. I was not proggramed with your word")
            word=input('What was your word?: ')
            with open('words_alpha.txt','a') as file:
                file.write('\n')
                file.write(word)
            break
        elif pop=='yy':
            print("wrong number of letters try again")
        else:
            print('The word is '+pop)
            print('I got '+str(wrong)+' letters wrong')
            y=input('Is that correct? (y/n): ')
            if y=='y':
                print('Hooray!')
            else:
                print("I'm sorry. I was not proggramed with your word")
                word=input('What was your word?: ')
                with open('words_alpha.txt','a') as file:
                    file.write(word)
                    file.write('\n')
            break
