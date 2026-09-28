Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='I am in class'
a[0]
'I'
a[5]+a[6]+a[7]+a[8]
'in c'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[1]
' '
a[1]+a[4]+a[7]
'   '
a='vijayawada is a royal city'
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]
'is'
# Negative index
a='vizag is a city of destiny'
a[-15]+a[-16]+a[-17]
'c a'
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
a='Simple is better than complex'
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'Simple'
# Slicing
a='codegnan'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a='work hard until you succeed'
a[11:16]
'ntil '
a[10:11]
'u'
a[10:16]
'until '
a[5:9]
'hard'
a[:4]
'work'
a[16:19]
'you'
a[20:]
'succeed'
b='Time is very precious'
a[13:]
'il you succeed'
b[13:]
'precious'
a[10:14]
'unti'
a[10:15]
'until'
a[:4]
'work'
#negetive slicing
a='I love python'
a[-11:-19]
''
a[-11:-9]
'lo'
a[-11:-7]
'love'
a[6:]
' python'
>>> a[-6:]
'python'
>>> b='Today is weekend'
>>> b[-16:-11]
'Today'
>>> b[-10:-8]
'is'
>>> b[-7:]
'weekend'
>>> #Striding
>>> a='Data Science'
>>> a[::]
'Data Science'
>>> a[::1]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a='Machine Learning'
>>> a[::4]
'MiLn'
>>> a[::6]
'Men'
>>> a[::2]
'McieLann'
>>> a[:9]
'Machine L'
>>> a[::7]
'M n'
>>> a='cloud computing'
>>> a[2:14:4]
'ocu'
>>> a[5:13:3]
' mt'
>>> a[4:12:2]
'dcmu'
>>> #negative striding
>>> a='python course'
>>> a[-1:-11:-2]
'ero o'
>>> a[-2:-12:-3]
'sont'
>>> a[-2:-12:3]
''
>>> a[::-1]
'esruoc nohtyp'
