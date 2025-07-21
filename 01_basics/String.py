# String Operations***


# a) using indexes
# a = 'nani'
# print(a[-1])
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])




# # b) Using slice-operator
# #str-access-slicing
# a = 'nani is developer'
# print(a[1:10:2])
# print(a[::-1])
# print(a[5:])
# print(a[:5  ])
# print(a[:])
# print(a[::])
# print(a[::-2])
# print(a[-1:-9:-2])
# print(a[-9:-1:-1])
# print(a[1:0:2])






# Strings with Mathematical Operators
# a = 'nani you '
# b= 'are engineer'

# print(len(a))

# print(a+b)

# print(a*1)
# print(a*20)






# # Checking/Finding/Searching String(****) = It is done with "in" or "not in" operator
# a="god is all mighty"
# print('is' in a)
# print("" in a)
# print(' ' in a)
# print('  ' in a)
# print('s ' in a)
# print('IS' in a)



# # count()  
# a="god is all mighty"
# print(a.count('god'))
# print(a.count('is',3,10))
# print(a.count('i',3,-1))
# print(a.count('i',3))



# # replace() #Replacing old-str with new-str
# a="god is all mighty"
# print(a.replace(' ','  '))
# print(a.replace('god','GOD'))



# # Immutable str-obj(***)
# a="god is all mighty"
# print(id(a))
# a=a.replace('god','GOD')
# print(id(a))




# a = '       nani        '
# # a) rstrip() :- removes extra spaces from right-side
# print(a.rstrip())


# # b) lstrip() :- removes extra spaces from left-side
# print(a.lstrip())


# # c) strip() :- removes extra spaces from both-sides
# print(a.strip())



# a=['nani','nami','anya','baia']
# # Joining of Strings
# print(''.join(a))
# print(' '.join(a))
# print(', '.join(a))
# print(' * '.join(a))



# a='nani nami baia anya'
# b='nani, nami, baia, anya'
# # Splitting of Strings
# print(a.split())
# print(a.split(' '))
# print(a.split('i'))
# print(b.split(','))





# a='nani'
# b='NANI'
# c='NaNi'
# d='nani konala'
# # Changing case of a string
# # a) upper() 		#converts to upper-case
# print(a.upper())

# # b) lower() 		#converts to lower-case
# print(b.lower())

# # c) swapcase() 	#converts to upper to lower & lower to upper
# print(c.swapcase())

# # d) title() 		#converts each word 1st letter to Upper-case
# print(d.title())

# # e) capitalize()	#only 1st-char will be converted to upper-case
# print(d.capitalize())





# # Checking Starting and Ending part of a string = These methods returns True or False
# a = 'nani konala'
# print(a.startswith('nani'))
# print(a.startswith('Nani'))

# print(a.endswith('konala'))
# print(a.endswith('la'))
# print(a.endswith('  '))

