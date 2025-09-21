# Task  1.1

longString = 'In addition to the tasks below, you must go as far as possible in this game.'
# print(a)

# Task 1.2
# print(longString[0])
# print(longString[12])

# Task 1.3
# print(longString[-1])

# Task 1.4
print(longString[4:9])

# Task 2.1
longString = longString.lower()
print(longString)

# Task 2.2
# sentence = 'tutu on the tuki-kata'
# newSentence = ''
#
# for i in range(len(sentence)):
#     if 'u' == sentence[i]:
#         if 't' == sentence[i - 1]:
#             newSentence += 'a'
#     else :
#         newSentence += sentence[i]
# print(newSentence)

# Task 2.3
# string = 'Hello World !'
# position = string.find('a')
# print(position)

# Task 2.4
# p = "abcdefghij"
# print (p [3:])

# Task 2.6
# for i in range(10):
#     print(str(i+1)+' : '+p)

# Task 2.7
# print("hello "+str(42))

# Task 2.8
# s1,s2,s3 = "42" ,"is","the answer"
# sentence = s3 +' '+s2+' '+s1
# print(sentence +' contains '+str(len(sentence))+' '+'characters.')

# Challenge

# CHECK_LIST = ['cat','garden','mice']
# newSentence = "the CataCat attaCk a Cat"
#
# def countWord (sentence):
#     MAX_SENTENCE = len(sentence)
#     sum = 0
#     sentence = sentence.lower()
#     newSentenceReverse = sentence[::-1]
#
#     for i in range(len(sentence)):
#         for x in CHECK_LIST :
#             if sentence[i:i+len(x)] == x :
#                 sum +=1
#
#             elif newSentenceReverse[i:i+len(x)] == x :
#                 sum += 1
#     return sum
#
# print(countWord(newSentence))

# Task 3.1

# user = input('What is your name : ').capitalize()
# print('Hello '+user)

# Task 3.2
# number = input('Enter your number : ')
# print('The type is '+str(type(number)))

# Task 3.3

# sum = 0
# for i in range(2) :
#     number = input('Enter the number '+str(i+1)+' : ')
#     sum += int(number)
# print(sum)

# Task 3.4
# def extractWord() :
#     sentences =  input('Enter your sentences : ')
#     sentences = sentences.split(' ')
#     word = ''
#     for i in sentences :
#         word += i[0]
#     return word
#
# print(extractWord())
