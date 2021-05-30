#Phone number extracter using regular expressions
import re, pprint


details = '''
161


80
I want to write a regular expression for a standard US type phone number that supports the following formats:

###-###-####
(###) ###-####
### ### ####
###.###.####
where # means any number. So far I came up with the following expressions

^[1-9]\d{2}-\d{3}-\d{4}
^\(\d{3}\)\s\d{3}-\d{4}
^[1-9]\d{2}\s\d{3}\s\d{4}
^[1-9]\d{2}\.\d{3}\.\d{4}
respectively. I am not quite sure if the last one is correct for the dotted check. I also want to know if there is any way I could write a single expression instead of the 4 different ones that cater to the different formats I mentioned. If so, I am not sure how do I do that. And also how do I modify the expression/expressions so that I can also include a condition to support the area code as optional component. Something like

+1 ### ### ####
where +1 is the area code and it is optional.

regex
Share
Edit
Follow
edited Mar 19 '20 at 9:13

Wiktor Stribiżew
485k2626 gold badges302302 silver badges397397 bronze badges
asked May 22 '13 at 18:21

noobcoder
8,96788 gold badges3131 silver badges5454 bronze badges
5
possible duplicate of stackoverflow.com/questions/123559/… the suggested answer is to strip every non-digit character. In this way, you simplify the validation – Arnaud Denoyelle May 22 '13 at 18:24 
1
I know this was a while back, but I don't think US area codes can begin with 1. (123) 456-7890 would be invalid because of the leading 1. – bobanahalf Jul 31 '15 at 19:49
For a more complete correct answer see: stackoverflow.com/a/18626090/561710 – Joe Johnston Sep 11 '17 at 17:23
Parsing phone numbers is hard. Google released an open source lib for this. Help yourself, use libphonenumber (or a fork in your language) – aloisdg Mar 30 '18 at 15:05
Add a comment
20 Answers

262

^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$
Matches the following

123-456-7890
(123) 456-7890
123 456 7890
123.456.7890
+91 (123) 456-7890
If you do not want a match on non-US numbers use

^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$
Update :
As noticed by user Simon Weaver below, if you are also interested in matching on unformatted numbers just make the separator character class optional as [\s.-]?

^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$
Share
Edit
Follow
edited Jan 12 '15 at 15:13
answered May 22 '13 at 18:52

Ravi K Thapliyal
47k88 gold badges7070 silver badges8484 bronze badges
1
Do you think that the question mark is not necessary in (?\d{3}) part of your very first line ? I think we do need one or more occurrence and not zero or one occurrence of a digit within the '(' and ')' – noobcoder May 22 '13 at 19:54 
3
The ? there applies on parentheses (), not on the digits. The complete related regex is \(?\d{3}\)?. \d{3} specifies that there must be three digits between the () that are (made) optional (by ?). – Ravi K Thapliyal May 22 '13 at 20:07 
6
note: this doesn't match 1234567890 which may or may not be a problem. for me it was - so I just added ? after each [\s.-] to make it optional – Simon_Weaver Aug 12 '14 at 20:59
1
@Simon_Weaver Thank you for your inputs. I've added your observation to the answer. – Ravi K Thapliyal Jan 12 '15 at 15:17
3
If you want one that avoids the issue @BobRay mentioned, use ^(\+\d{1,2}\s)?((\(\d{3}\))|(\d{3}))[\s.-]\d{3}[\s.-]\d{4}$. (I basically just duplicated the segment of the RegEx that covers the area code and allowed one variant with parens and one without) – Shrey Gupta Sep 17 '18 at 11:35
Show 10 more comments

161

There are many variations possible for this problem. Here is a regular expression similar to an answer I previously placed on SO.

^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$
It would match the following examples and much more:

18005551234
1 800 555 1234
+1 800 555-1234
+86 800 555 1234
1-800-555-1234
1 (800) 555-1234
(800)555-1234
(800) 555-1234
(800)5551234
800-555-1234
800.555.1234
800 555 1234x5678
8005551234 x5678
1    800    555-1234
1----800----555-1234
Regardless of the way the phone number is entered, the capture groups can be used to breakdown the phone number so you can process it in your code.

Group1: Country Code (ex: 1 or 86)
Group2: Area Code (ex: 800)
Group3: Exchange (ex: 555)
Group4: Subscriber Number (ex: 1234)
Group5: Extension (ex: 5678)
Here is a breakdown of the expression if you're interested:

^\s*                #Line start, match any whitespaces at the beginning if any.
(?:\+?(\d{1,3}))?   #GROUP 1: The country code. Optional.
[-. (]*             #Allow certain non numeric characters that may appear between the Country Code and the Area Code.
(\d{3})             #GROUP 2: The Area Code. Required.
[-. )]*             #Allow certain non numeric characters that may appear between the Area Code and the Exchange number.
(\d{3})             #GROUP 3: The Exchange number. Required.
[-. ]*              #Allow certain non numeric characters that may appear between the Exchange number and the Subscriber number.
(\d{4})             #Group 4: The Subscriber Number. Required.
(?: *x(\d+))?       #Group 5: The Extension number. Optional.
\s*$                #Match any ending whitespaces if any and the end of string.
To make the Area Code optional, just add a question mark after the (\d{3}) for the area code.

Share
Edit
Follow
edited May 22 '13 at 23:10
answered May 22 '13 at 23:03

Francis Gagnon
2,76511 gold badge1212 silver badges2222 bronze badges
10
best answer IMHO. For my purpose, the \s at the beginning and end are not needed, because I'm using for validation, and the field is trimmed already. – Daniel May 26 '15 at 20:31
3
By far the best answer and most complete. I also really appreciate the regex breakdown. – Bryant Jackson May 25 '17 at 13:05
@Kondal I'm curious about the input you're using to make it fail. It seems to work fine for me with a 0 for the country code. – Francis Gagnon Nov 22 '17 at 12:41
<input type="text" name="phone_no" class="form-control" ng-pattern="^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$" only-numbers ng-maxlength="10" /> – Kondal Nov 22 '17 at 13:04 
@Kondal Sorry. I meant the text you are trying to match that is failing with this regex. – Francis Gagnon Nov 23 '17 at 12:32
Show 6 more comments

20

^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$

Matches these phone numbers:
1-718-444-1122
718-444-1122
(718)-444-1122
17184441122
7184441122
718.444.1122
1718.444.1122
1-123-456-7890
1 123-456-7890
1 (123) 456-7890
1 123 456 7890
1.123.456.7890
+91 (123) 456-7890
18005551234
1 800 555 1234
+1 800 555-1234
+86 800 555 1234
1-800-555-1234
1 (800) 555-1234
(800)555-1234
(800) 555-1234
(800)5551234
800-555-1234
800.555.1234
18001234567
1 800 123 4567
1-800-123-4567
+18001234567
+1 800 123 4567
+1 (800) 123 4567
1(800)1234567
+1800 1234567
1.8001234567
1.800.123.4567
+1 (800) 123-4567
18001234567
1 800 123 4567
+1 800 123-4567
+86 800 123 4567
1-800-123-4567
1 (800) 123-4567
(800)123-4567
(800) 123-4567
(800)1234567
800-123-4567
800.123.4567
1231231231
123-1231231
123123-1231
123-123 1231
123 123-1231
123-123-1231
(123)123-1231
(123)123 1231
(123) 123-1231
(123) 123 1231
+99 1234567890
+991234567890
(555) 444-6789
555-444-6789
555.444.6789
555 444 6789
18005551234
1 800 555 1234
+1 800 555-1234
+86 800 555 1234
1-800-555-1234
1.800.555.1234
+1.800.555.1234
1 (800) 555-1234
(800)555-1234
(800) 555-1234
(800)5551234
800-555-1234
800.555.1234
(003) 555-1212
(103) 555-1212
(911) 555-1212
18005551234
1 800 555 1234
+86 800-555-1234
1 (800) 555-1234
See regex101.com

Share
Edit
Follow
answered Jun 4 '19 at 20:28

stomy
8711111 silver badges1414 bronze badges
Add a comment

8

Here's a fairly compact one I created.

Search: \+?1?\s*\(?-*\.*(\d{3})\)?\.*-*\s*(\d{3})\.*-*\s*(\d{4})$

Replace: +1 \($1\) $2-$3
Tested against the following use cases.

18001234567
1 800 123 4567
1-800-123-4567
+18001234567
+1 800 123 4567
+1 (800) 123 4567
1(800)1234567
+1800 1234567
1.8001234567
1.800.123.4567
1--800--123--4567
+1 (800) 123-4567
Share
Edit
Follow
edited Nov 25 '14 at 16:26
answered Nov 25 '14 at 16:06

Puneet Lamba
70188 silver badges1313 bronze badges
This matches stuff like (800 444-4444 – Jake Dec 11 '15 at 4:20
Add a comment

6

Adding up an example using above mentioned solutions on jsfiddle. I have modified the code a bit as per my clients requirement. Hope this also helps someone.

/^\s*(?:\+?(\d{1,3}))?[- (]*(\d{3})[- )]*(\d{3})[- ]*(\d{4})(?: *[x/#]{1}(\d+))?\s*$/
See Example Here

Share
Edit
Follow
answered Oct 28 '16 at 11:35

Avinash Lad
6111 silver badge11 bronze badge
Add a comment

5

try this for Pakistani users .Here's a fairly compact one I created.

((\+92)|0)[.\- ]?[0-9][.\- ]?[0-9][.\- ]?[0-9]
Tested against the following use cases.

+92 -345 -123 -4567
+92 333 123 4567
+92 300 123 4567
+92 321 123 -4567
+92 345 - 540 - 5883
Share
Edit
Follow
answered Mar 14 '16 at 19:06

sajid
4711 silver badge55 bronze badges
Hello Sajjid.If i want to add 03041234567. What would be Regular expression. – Anees Dec 30 '20 at 14:19
Add a comment

5

Phone number regex that I use: /^[+]?(\d{1,2})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/

Covers:

18001234567
1 800 123 4567
+1 800 123-4567
+86 800 123 4567
1-800-123-4567
1 (800) 123-4567
(800)123-4567
(800) 123-4567
(800)1234567
800-123-4567
800.123.4567
Share
Edit
Follow
edited Mar 29 '19 at 3:27
answered Aug 31 '18 at 20:00

Yevhen Kotliar
9111 silver badge44 bronze badges
Add a comment

4

Starting with @Ravi's answer, I also applied some validation rules for the NPA (Area) Code.

In particular:

It should start with a 2 (or higher)
It cannot have "11" as the second and third digits (N11).
There are a couple other restrictions, including reserved blocks (N9X, 37X, 96X) and 555, but I left those out, particularly because the reserved blocks may see future use, and 555 is useful for testing.

This is what I came up with:

^((\+\d{1,2}|1)[\s.-]?)?\(?[2-9](?!11)\d{2}\)?[\s.-]?\d{3}[\s.-]?\d{4}$
Alternately, if you also want to match blank values (if the field isn't required), you can use:

(^((\+\d{1,2}|1)[\s.-]?)?\(?[2-9](?!11)\d{2}\)?[\s.-]?\d{3}[\s.-]?\d{4}$|^$)
My test cases for valid numbers (many from @Francis' answer) are:

18005551234
1 800 555 1234
+1 800 555-1234
+86 800 555 1234
1-800-555-1234
1.800.555.1234
+1.800.555.1234
1 (800) 555-1234
(800)555-1234
(800) 555-1234
(800)5551234
800-555-1234
800.555.1234
My invalid test cases include:

(003) 555-1212     // Area code starts with 0
(103) 555-1212     // Area code starts with 1
(911) 555-1212     // Area code ends with 11
180055512345       // Too many digits
1 800 5555 1234    // Prefix code too long
+1 800 555x1234    // Invalid delimiter
+867 800 555 1234  // Country code too long
1-800-555-1234p    // Invalid character
1 (800)  555-1234  // Too many spaces
800x555x1234       // Invalid delimiter
86 800 555 1212    // Non-NA country code doesn't have +
My regular expression does not include grouping to extract the digit groups, but it can be modified to include those.

Share
Edit
Follow
answered Jul 28 '16 at 22:24

MCattle
2,49722 gold badges3030 silver badges4949 bronze badges
Great answer + add on. Thanks – Llama Apr 14 at 21:44
Add a comment

3

Regex pattern to validate a regular 10 digit phone number plus optional international code (1 to 3 digits) and optional extension number (any number of digits):

/(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?/g
Demo: https://www.regextester.com/103299

Valid entries:

/* Full number */
+999 (999) 999-9999 Ext. 99999

/* Regular local phone number (XXX) XXX-XXXX */
1231231231
123-1231231
123123-1231
123-123 1231
123 123-1231
123-123-1231
(123)123-1231
(123)123 1231
(123) 123-1231
(123) 123 1231

/* International codes +XXX (XXX) XXX-XXXX */
+99 1234567890
+991234567890

/* Extensions (XXX) XXX-XXXX Ext. XXX... */
1234567890 Ext 1123123
1234567890Ext 1123123
1234567890 Ext1123123
1234567890Ext1123123

1234567890 Ext: 1123123
1234567890Ext: 1123123
1234567890 Ext:1123123
1234567890Ext:1123123

1234567890 Ext. 1123123
1234567890Ext. 1123123
1234567890 Ext.1123123
1234567890Ext.1123123
'''

pattern = re.compile(r'''(
( (\d{3})|\(\d{3}\))?        #Area code optional
(-|/.|\s)?                         #gap filling optional       
(\d{3})+                     #first 3 digits
(-|\.|\s)+                         #seperator 
(\d{4})+                     #last 4 digits                 
)''', re.VERBOSE)

search = pattern.findall(details)
pprint.pprint(search)






