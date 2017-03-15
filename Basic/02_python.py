Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
name = "raghav babbar"
>>> name[0]
'r'
>>> name[-1]
'r'
>>> name[-2]
'a'
>>> name[1:2]
'a'
>>> name[1:3]
'ag'
>>> name[0:8]
'raghav b'
>>> name[2:]
'ghav babbar'
>>> len(name)
13
>>> 
playeer=[22,33,32,43,17,21]
>>> palyeer[2]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    palyeer[2]
NameError: name 'palyeer' is not defined
>>> playeer[2]
32
>>> playeer[2]=100
>>> playeer[2]
100
>>> playeer+[1,2,3,4]
[22, 33, 100, 43, 17, 21, 1, 2, 3, 4]
>>> playeer
[22, 33, 100, 43, 17, 21]
>>> p=[1,2,3,4]
>>> newlist=p+playeer
>>> newlist
[1, 2, 3, 4, 22, 33, 100, 43, 17, 21]
>>> newlist[:5]
[1, 2, 3, 4, 22]
>>> newlist[:2]=[0,0]
>>> newlist
[0, 0, 3, 4, 22, 33, 100, 43, 17, 21]
>>> newlist[:2]=[1]
>>> mewlist
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    mewlist
NameError: name 'mewlist' is not defined
>>> newlist
[1, 3, 4, 22, 33, 100, 43, 17, 21]
>>> newlist[:5]=[10]
>>> newlist
[10, 100, 43, 17, 21]
>>> newlist[:2]=[]
>>> newlist
[43, 17, 21]
>>> 
