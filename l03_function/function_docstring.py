
# coding: utf-8

# # Function + docstring

# In[13]:


def hello(name):
    """This function say hello follow by name """
    print("Hello,", name)
    
print(hello.__doc__)
hello('top')


# # Return
def function_name(parameters):
    """docstring"""
    statement(s)
    return [expression]
# In[25]:


def hello(name):
    """This function say hello follow by name """
    return 'Hello,'+name
print(hello('Jack'))


# # Function Arguments

# - Requird arguments
# - Keyword arguments
# - Default arguments
# - Variable-length arguments

# ## - Requird arguments

# In[38]:


def hello(name):
    """This function say hello follow by name """
    return 'Hello,'+name
print(hello('Jack'))

# print(hello()) #Error


# ## - Keyword arguments

# In[41]:


def hello(name):
    """This function say hello follow by name """
    return 'Hello,'+name

print(hello('Jack'))
print(hello(name='top'))
#print(hello(name2='Jack')) #Error


# ## - Default arguments

# In[42]:


def hello(name='None'):
    """This function say hello follow by name """
    return 'Hello,'+name

print(hello())
print(hello('Jack'))
print(hello(name='top'))


# ## - Variable-length arguments

# In[43]:


def hello(name='None',*word): # ' * ' *word = Tuple
    """This function say hello follow by name """
    text=''
    for w in word :
        text+=str(w)
    return 'Hello,'+name+' '+text

print(hello('top','How','are you')) # Hello,top Howare you
print(hello('Tony',1,2,3)) # Hello,Tony 123

# print(hello(name='top','How','are you')) #Erroe
# n* arguments


# # Anonymous Functions

# # Lambda

# In[44]:


# lamba arguments: expression


# In[52]:


sum = lambda n1,n2 : n1+n2
sub = lambda n1,n2 : n1-n2
div = lambda n1,n2 : n1/n2
mul = lambda n1,n2 : n1*n2

print(sum(20,10)) #30
print(sub(20,10)) #10
print(div(20,10)) #2.0
print(mul(20,10)) #200

def sum(n1,n2):
    return n1+n2


# ## - Lambda Functions

# In[58]:


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  ##22
print(mytripler(11))  ##33


# # Scope

# - local
# - Global

# ## - local
# 

# In[74]:


def foo():
    y = 'local'
    print(y)
foo()
#print(y) #Error


# ## - Global

# In[86]:


x = 'outer'

def foo():
    print('x inside :',x)
    
foo()
print('x outside :',x)


# In[89]:


x = 'Global'

def foo():
    x = x * 2
    print(x)
foo()


# In[90]:


x = 'global'

def foo():
    global x
    y = 'local'
    x = x * 2
    print(x)
    print(y)
foo()
print(x)


# # Types of Functions

# - Build-in
# - user-Define

# ## - Build-in

# abs()	delattr()	hash()	memoryview()	set()
# all()	dict()	help()	min()	setattr()
# any()	dir()	hex()	next()	slice()
# ascii()	divmod()	id()	object()	sorted()
# bin()	enumerate()	input()	oct()	staticmethod()
# bool()	eval()	int()	open()	str()
# breakpoint()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()	 

# ## - User-Define
