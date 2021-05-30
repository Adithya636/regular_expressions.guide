# Regular Expressions
# Regular Expressions are a way to find matching patters for example if we need to find a  list of email or a phone numbers...
# Regular expressions can be used
#in this code I will be giving some basic regular expressions documentation
# getting started with regular expressions
import re # By this way we can import regular expressions
# note(regular expressions also called regex, which is a built in python module)*
#Creating A Regex Object
#re.compile('')# inside this function we have to pass the pattern we need to match 
RegexPattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')# so we created a pattern
#re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')here \d refers to digits 0-9, I Have Used "r" before pattern because it is a raw string 
# which will escape the backslashes and print it out if 'r' was not inculed then it will be a escaping charecter.
#Now that we created a object we can create a function search() to find any line with our pattern in it.
mo = RegexPattern.search('My name is leo and my phone number is 333-222-6749 call me at 10 AM, Bye') #Here we created a search 
#method and given a string of words to find our pattern.
#To find our pattern we use group() method on mo.

print('Phone Number Found ' + mo.group()) # Here we go!
#This should print 'Phone Number Found  333-222-6749'

#GROUPS
# we can create a group in regex using parantheses

RegexPattern2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

moo = RegexPattern2.search(' 333-222-6749 ')
# you can see i created a group by using ()

#To get group one first set of value in first '()', use - group(1)
print(moo.group(1))
#To get group second  set of value in second '()', use - group(2)...ETC
print(moo.group(2))
#To get everything leave it as blank or input 0
print(moo.group(0))
#To get every groups inside the pattern use groups() method which return a tuple type of values
print(moo.groups())

#Pipe Charecter

# '|' This can also be called the Pipe Charecter

#using this we can match multiple regex objects

RegexPattern3 = re.compile(r'Batman|Superman')
# IF both were in the line it will give first occurence of batman or superman pattern. To get all pattern we can use findall() method
mo2 = RegexPattern3.search('Batman killed Superman')
#Finds first occurence
print(mo2.group())
mo2 = RegexPattern3.search('Superman killed by Batman')
#Finds first occurence
print(mo2.group())
#------------------------------------------------------------------------------------------------------------------------------------------

#Matching 
#Matching a pattern once or none(optional)
# Using ? symbol we can match a pattern in our string optional mean zero times or once
object = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = object.search('This is new number "222-333-2323"')
print(mo3.group())
mo4 = object.search('This is new number "333-2323"')
print(mo4.group())
#These both will work
try:
    object2 = re.compile('Bat(wo)?man')
    new = object2.search('Batwowowoman')
    print(new.group())
except AttributeError:
    print('Yes, This wouldn\'t work')
#While this would not work

#Matching a pattern zero times or more
# Using * operator we can match a pattern zero times or more
object3 = re.compile('Bat(wo)*man')
new2 = object3.search('Batwowowowowowowowoman')
#This time it will work :)
print(new2.group())

#Matching a pattern once or more(particullarly it should be there)
# Using + operator we can match a pattern once or more
object4 = re.compile(r'bat(wo)+man')
new3 = object4.search('batwowowoman')
print(new3.group())
#This should work

#While This Ain't
try:
    object5 = re.compile(r'bat(wo)+man')
    new4 = object4.search('batman')
    print(new4.group())
except AttributeError:
    print('It won\'t actually print answer but it prints this line')
#-------------------------------------------------------------------------------------------------------------------
#Matching a specific times a pattern using {} 
# it takes first value the starting point and second ending point same as range func()
object5 = re.compile(r'(\d){3}-(\d){3}-(\d){4}')
new4 = object5.search('333-457-5467')
print(new4.group())


object6 = re.compile(r'(he){3,5}')
new5 = object6.search('hehehe')
new6 = object6.search('hehehehe')
new7 = object6.search('hehehehehe')
print(new5.group())
print(new6.group())
print(new7.group())

#These steps will work


#While
try:
    new8 = object6.search('he')
    new9 = object6.search('hehehehehehehehe')
    #this wouldn't be runed it will be an error
    print(new8.group())
    print(new9.group())
except AttributeError:
    print('Yep it won\'t')

#Greedy and non-greedy
#greedy
#normally regular expressions find the longest pattern (b) if we use {a, b} *more about it is in the top, if both a and b sized patterns given
#while non-greedy also lazy and will find lowest, by  using ? charecter at last after {}.
#lets check
non_greedy = re.compile(r'(he){3,6}?')
search = non_greedy.search('hehehehehehe')
print(search.group())
#Findall method which used to find all the occurence of the patterns matching object
#if the pattern has no groups findall returns a list while if it has groups it returns tuples

#With out groups
new_method = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(new_method.findall('Hey guys my name is rocky and i have two phone no they are 333-222-6875 and 464-578-5373'))

#With groups
new_method2 = re.compile(r'(\d\d\d-)(\d\d\d-)(\d\d\d\d)')
print(new_method2.findall('Hey guys my name is rocky and i have two phone no they are 333-222-6875 and 464-578-5373'))
#--------------------------------------------------------------------------------------------------------------------------------------------
#Charecter classes
#these are used to short some specic things like \d for digits 0-9
#I will show you charecter classes table
'''
Symbol;  ------------- specification;

\d                     numeric digits from 0 to 9.                                             

\D                     not a numeric digits 

\w                     any character that is letters numeric digits and underscores                    

\W                     any character that is not letters numeric digits and underscores                                             

\s                     spaces , new lines and tabs                   

\S                     non space or new lined or tabed charecters                 


'''

#Making your own character classes

#you can make your classes using [] brackets 
# example [0-9] is actually ('0|1|2|3|4|5|6|7|8|9') same for a-z and A-Z


created_charecter_classes = re.compile(r'[a-zA-z0-1-_]')
print(created_charecter_classes.findall('newlined comme fi a ssgsggshs'))


# using ^ charecter after first [ bracket then the pattern will be : any pattern inside [] will not be pattern for your understanding run the below code
created_charecter_classes1 = re.compile(r'[^a-zA-z0-6]')
print(created_charecter_classes1.findall('newlined  9 comme fi 87    a ssgsg-gshs2  = - -  -gh " / . , '))

#caret and dollar sign
#caret ^ is used in regex pattern where the pattern must begin with 
#dollar $ is used in regex pattern where  the pattern must end with
#both can be used as it should start and end with them

spam = re.compile(r'^\d+')
print(spam.findall('555 is my code for the party'))


spam2 = re.compile(r'\d+$')
print(spam2.findall('my code for the party is 555'))

spam3 = re.compile(r'^\d+$')
print(spam3.findall('555'))

#Until this your terminal should look like this
#if you were using some online compiler or vs code or pycharm or sublime text
'''
Phone Number Found 333-222-6749
333
222-6749
333-222-6749
('333', '222-6749')
Batman
Superman
222-333-2323
333-2323
Yes, This wouldn't work
Batwowowowowowowowoman
batwowowoman
It won't actually print answer but it prints this line
333-457-5467
hehehe
hehehehe
hehehehehe
Yep it won't
hehehe
['333-222-6875', '464-578-5373']
[('333-', '222-', '6875'), ('464-', '578-', '5373')]
['n', 'e', 'w', 'l', 'i', 'n', 'e', 'd', 'c', 'o', 'm', 'm', 'e', 'f', 'i', 'a', 's', 's', 'g', 's', 'g', 'g', 's', 'h', 's']
[' ', ' ', '9', ' ', ' ', ' ', '8', '7', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '=', ' ', '-', ' ', '-', ' ', ' ', '-', ' ', '"', ' ', '/', ' ', '.', ' ', ',', ' ']
['555']
['555']
['555']
'''

#Wild card character
#the .(or dot) character is used in regex called as wild card character it is used to match except new lines
#but this will match only one charecter . == \w and non new lined characters
#to match it with many charecter use .* method
#also it can be matched to newlines by giving re.complie a second argument re.DOTALL; new_line = re.compile(r'.*', re.DOTALL)
#its actually a greedy value to change it to non greedy use ? charecter (r'.*?')
#for this charecter i wont do it but you try it on yourself if you got stuck in this problem google this charecter

#case insensetive matching
#here we have to pass re.I as second argument to do incasesensetive matching
IGNORECASE = re.compile(r'new world', re.I)
IGNORECASE1 = IGNORECASE.search('nEw WorLd is going to br created at year of 4597476')
print(IGNORECASE1.group())

#substituting string inplace of other strings
#it can be done by name.sub() instead of .search()
substitute = re.compile(r'agent \w+')
print(substitute.sub('censored','agent bobby decided to get into agent rocky club for more payment but agent spam is going to kill agent eggs'))

#Managing complex regexes using re.VERBOSE function
#if you need to write an address or email etc you need to write complicated texts inside re.compile 
#but passing re.VERBOSE as second argument
#you can add anythign like comments in your program as a normal python [program do]

complex = re.compile(r'''(
# I will show a phone number pattern
( (\d{3})|\(\d{3}\))?        #Area code optional
(-)?                         #gap filling optional       
(\d{3})+                     #first 3 digits
(-)+                         #seperator 
(\d{4})+                     #last 4 digits                 
)''', re.VERBOSE)

answer = complex.findall('my new number is 777-4646 and its full number is 332-777-4646 and old number was 342-323-5675 don\'t call it')
print(list(answer))

#hey thats all youre good until this 
#actually i made a simple documentation on regex this is useful when you know about regex already and  need to revise it 
#i have made some simple mistakes on spelling maybe but all the code inputed are corect

#After all this program your output should look like this:
'''
Phone Number Found 333-222-6749
333
222-6749
333-222-6749       
('333', '222-6749')
Batman
Superman
222-333-2323
333-2323
Yes, This wouldn't work
Batwowowowowowowowoman
batwowowoman
It won't actually print answer but it prints this line
333-457-5467
hehehe
hehehehe
hehehehehe
Yep it won't
hehehe
['333-222-6875', '464-578-5373']
[('333-', '222-', '6875'), ('464-', '578-', '5373')]
['n', 'e', 'w', 'l', 'i', 'n', 'e', 'd', 'c', 'o', 'm', 'm', 'e', 'f', 'i', 'a', 's', 's', 'g', 's', 'g', 'g', 's', 'h', 's']
[' ', ' ', '9', ' ', ' ', ' ', '8', '7', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '=', ' ', '-', ' ', '-', ' ', ' ', '-', ' ', '"', ' ', '/', ' ', '.', ' ', ',', ' ']
['555']
['555']
['555']
nEw WorLd
censored decided to get into censored club for more payment but censored is going to kill censored
[('777-4646', '', '', '', '777', '-', '4646'), ('332-777-4646', '332', '332', '-', '777', '-', '4646'), ('342-323-5675', '342', '342', '-', '323', '-', '5675')]
'''

#Good luck if you got this
#by the way you can check more reguler expressions at;
#official site
#https://docs.python.org/3/library/re.html
#here too:
#https://www.regular-expressions.info/
print(input('have a nice day;'))