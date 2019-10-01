#pallindrome string

def reverse(s):
    return s[::-1]
def isPalindrome(s):
    rev=reverse(s)
    if(s==rev):
        return True
s=input("ENter the string to check:"),
ans=isPalindrome(s)
if ans==1:
    print("Yes")
else:
    print("No")
    
    
    
#reverse words in a string
def reverse(input):
    inputwords=input.split()
    inputwords=inputwords[-1::-1]
    output=' '.join(inputwords)
    return output
input="hello you are buffalo"
print(reverse(input))



#replace ith character
str="hellosejal"
print("original string:"+str)
new_str=str.replace('e','',2)
print(new_str)


#check substring is present
def check(stri,sub):
    if(stri.find(sub)==-1):
        print("NO")
    else:
        print("YES")
stri="sejal is the best in the world"
sub=input("enter the substring")
check(stri,sub)


#print words of even length
def printeven(str):
    str=str.split(' ')
    for word in str:
        if len(word)%2==0:
            print(word)
str="I am Sejal having goodd coommmnnnuutti skills"
printeven(str)




#accept vowel string
def check(str):
    vowels=set("aeiou")
    s=set({})
    for char in str:
        if char in vowels:
            s.add(char)
        else:
            pass
    if len(s)==len(vowels):
        print("ACCEPTED")
    else:
        print("NOT ACCEPTED")
        
str="SEEquoiL"
str=str.lower()
check(str)



#number of matching characters
def count(str1,str2):
    set1=set(str1)
    print(set1)
    set2=set(str2)
    print(set2)
    match=set1 & set2
    print(match)
    
    print("num of chars matched:",len(match))
str1 = 'aabcddekll12@'
str2 = 'bb2211@55k'  
count(str1,str2)


#count vowels using set
def vowel_count(str):
    vowel=set("aeiouAEIOU")
    count=0
    s=[]
    print(vowel)
    for char in str:
        if char in vowel:
            s.append(char)
            count=count+1
    s=set(s)
            
    print(s)
    print(len(s))
        
    print("no of vowels",count)
str="Geeks for geekssaaiew"
vowel_count(str)


#remove duplicates
from collections import OrderedDict
def removeduplicate(str):
    return "".join(set(str))
def removewithorder(str):
    return "".join(OrderedDict.fromkeys(str))
str="geeksforgeeks"
print(removeduplicate(str))
print(removewithorder(str))



#remove special characters
import re
def run(string):
    regex=re.compile('[@_!$%^&*<>?/\|}{~:]')
    if(regex.search(string)==None):
        print("accept")
    else:
        print("not accepted")
string="geeks@for%^&geeks"
run(string)
    


#generate random strings
import string
import random
import time
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'
t="sejal"







#split and join a string
def split(str):
    list=str.split(" ")
    return list
def join(list):
    str=' '.join(list)
    return str
str="sejal is the best"
list=split(str)
print(list)
print(list[0][1])
join_str=join(list)
print(join_str)



#find close matches of a word
from difflib import get_close_matches
def close_matches(word,patterns):
    print(get_close_matches(word,patterns,2,0.5))
word="sejalchandra"
patterns=['sej','jalchan','chandra','sejalcha']
close_matches(word,patterns)



#find uncommon words between 2 strings
def uncommon(A,B):
    
    A=A.split()
    for word in A:
        count[word]=count.get(word,0)+1
    B=B.split()
    for word in B:
        count[word]=count.get(word,0)+1
    for word in count:
        if count[word]==1:
            print( word,end=" ")
    
A="learning is God"
A=A.lower()

B="God is the best"
B=B.lower()
count={}
uncommon(A,B)
for word in count:
    print(word,end="    ")
    print(count[word])

def UncommonWords(A, B): 
  
    # count will contain all the word counts 
    count = {} 
      
    # insert words of string A to hash 
    for word in A.split(): 
        count[word] = count.get(word, 0) + 1
      
    # insert words of string B to hash 
    for word in B.split(): 
        count[word] = count.get(word, 0) + 1
  
    # return required list of words 
    return [word for word in count if count[word] == 1] 
  
# Driver Code 
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
  
# Print required answer 
print(UncommonWords(A, B))

#find duplicate chars
def duplicate(str):
str="geeksofgeeksssejal"
print(duplicate(str))





#exxtract digits fro string
import re

string="sejal12chandra3345"
res=re.sub("\D","",string)
stri=str(res)
print(stri)


import re
def extractmax(input):
    numbers=re.findall("\d+",input)
    print(numbers)
    numbers=[int(i) for i in numbers]
    print(numbers)    
    #numbers=map(int,numbers)
    #print(sum(numbers))
    print(max(numbers))
    print(min(numbers))
    print(sum(numbers))
input="100kkjfk 8jhkj6hf jf9000nfb"
extractmax(input)





#Find all the patterns  of “1(0+)1” in a given string
import re
def extract(input):
    count=0
    substring=re.search('01+',input)
    print(substring)
    while substring!=None:
        count=count+1
        input=input[(substring.end()-1):]
        substring=re.search("01+",input)
    print(count)
input="10111011010010"
extract(input)


#find question mark and replace 0 and 1
import re
def find_ques(input):
    result=re.search('?',input)
    print(result)
    
input="11?000?111"
find_ques(input)






























