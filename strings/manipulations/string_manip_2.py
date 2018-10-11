
# coding: utf-8

# In[3]:


def min_enclosing_rectangle(radius, x, y):
    if radius < 0:
        return None
    return (x - radius, y - radius)


# In[4]:


min_enclosing_rectangle(1,1,1)


# In[5]:


min_enclosing_rectangle(4.5, 10, 2)


# In[6]:


min_enclosing_rectangle(-1, 10, 2)


# In[7]:


min_enclosing_rectangle(500, 1000, 2000)


# In[24]:


def series_sum():
    n = int(input("Please enter a non-negative integer: "))
    if n < 0:
        return None
    result = 1000
    for i in range(1, n + 1):
        result += 1 / (i**2)
    
    return result


# In[26]:


series_sum()


# In[27]:


series_sum()


# In[28]:


series_sum()


# In[29]:


series_sum()


# In[30]:


series_sum()


# In[39]:


def pell(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return 2* pell(n - 1) + pell(n - 2)


# In[40]:


pell(0)


# In[41]:


pell(1)


# In[42]:


pell(2)


# In[43]:


pell(3)


# In[44]:


pell(-45)


# In[45]:


pell(6)


# In[51]:


def countMembers(s):
    result = 0
    for char in s:
        if  'e' <= char <= 'j' or '2' <= char <= '6' or char == '!' or char == ',' or char == '\\':
            result += 1
    return result


# In[52]:


countMembers("\\")


# In[53]:


countMembers("2\'")


# In[54]:


countMembers("1\'")


# In[55]:


countMembers("2aAb3?eE'_13")


# In[56]:


countMembers("one, Two")


# In[59]:


def casual_number(s):
    try:
        return int(s.replace(',', ''))
    except:
        return None


# In[61]:


casual_number("251")


# In[62]:


casual_number("1,aba,251")


# In[63]:


casual_number("1,251")


# In[64]:


casual_number("1251")


# In[65]:


casual_number("-97,251")


# In[66]:


casual_number("-97251")


# In[67]:


casual_number("-,,,,")


# In[68]:


casual_number("--97,251")


# In[69]:


casual_number("-")


# In[70]:


casual_number("-1,000,001")


# In[71]:


casual_number("999,999,999,876")


# In[72]:


casual_number("-2")


# In[73]:


def alienNumbers(s):
    return s.count('T') * 1024 + s.count('y') * 598 + s.count('!') * 121 + s.count('a') * 42 + s.count('N') * 6 + s.count('U') * 1


# In[74]:


alienNumbers("a!ya!U!NaU")


# In[75]:


alienNumbers("aaaUUU")


# In[76]:


alienNumbers("")


# In[85]:


def alienNumbersAgain(s):
    ft = {}
    ft['T'] = ft['y']  = ft['!'] = ft['a'] = ft['N'] = ft['U'] = 0
    for char in s:
        if char in ft:
            ft[char] += 1
    return ft['T'] * 1024 + ft['y'] * 598 + ft['!'] * 121 + ft['a'] * 42 + ft['N'] * 6 + ft['U'] * 1


# In[86]:


alienNumbersAgain("a!ya!U!NaU")


# In[87]:


alienNumbersAgain("aaaUUU")


# In[88]:


alienNumbersAgain("")


# In[115]:


def encrypt(s):
    res = ""
    if len(s) <= 1:
        return s
    
    for i in range(0, len(s) // 2):
        res +=  s[len(s) - 1 - i] + s[i] 
    if len(s) % 2 == 1:
        res += s[i + 1]
    return res


# In[116]:


encrypt("Hello, world")


# In[117]:


encrypt("1234")


# In[118]:


encrypt("12345")


# In[119]:


encrypt("1")


# In[120]:


encrypt("123")


# In[121]:


encrypt("12")


# In[122]:


encrypt("Secret Message")


# In[123]:


encrypt(",'4'r")


# In[129]:


def oPify(s):
    res = ""
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i+1].isalpha() :
            if s[i].isupper():
                res += s[i] + 'O'
            else:
                res += s[i] + 'o'
                
            if s[i+1].isupper():
                res += 'P'
            else:
                res += 'p' 
        else:
            res +=  s[i]
    res += s[-1]
    return res


# In[130]:


oPify("aa")


# In[131]:


oPify("aB")


# In[132]:


oPify("ooo")


# In[133]:


oPify("ax1")


# In[134]:


oPify("abcdef22")


# In[135]:


oPify("abcdef22x")


# In[136]:


oPify("aBCdef22x")


# In[137]:


oPify("x")


# In[138]:


oPify("123456")


# In[140]:


def nonrepetitive(s):
    # I have a solution to this which is a little long
    # I want to shorten it
    return True

