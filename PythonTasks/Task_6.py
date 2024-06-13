#Task 6 : Write a python program to access environment variables.
import os
print ("#"*40)
print (os.environ)
print ("#"*40)
print (os.environ.get('PATH'))
print ("#"*40)
print (os.environ.get('HOME'))
print ("#"*40)