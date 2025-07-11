a = 5
b=5
c=2
# A) ***Conditional stmts
#     i) simple-if statement

# if a<b:
#     print('a is less than b')


# if a>b:
#     print('a is less than b')
#     print('a<b')

# if (a>0): print("Given Number is +ve Number"); 




# ii) Multiple-if Statements
# if a<b:
#     print('a is less than b')
# if a>b:
#     print('a is greater than b')
# if a==b:
#     print('a is equal to b')
# x  = int(input('int'))
# if x%2==0:
#     print('Even Number')
# if x%2!=0 :
#     print('odd number')
# if x==0:
#     print('neither even or odd')



# iii) if-else statement
# if a<b:
#     print('a is less than b')
# else:
#     print('a is greater than b')



# iv) Nested if's
# x = int(input('int x '))
# y = int(input('int y ')) 
# z = int(input('int z ')) 
# if x>y:
#     if x>z:
#         print('x is greatest')
#     else:
#         print('z is greater')
# else:
#     if y>z:
#         print('y is greater')
#     else:
#         print('z is greater')  


# x = int(input('int x '))
# y = int(input('int y '))    
# z = int(input('int z '))
# if x<y:
#     if x<z:
#         print('x is smallest')
#     else:
#         print('z is smallest')
# else:
#     if y<z:
#         print('y is smallest')
#     else:
#         print('z is smallest')




# V) ***if-elif-else:-
# if a<b:
#     print('a is less than b')
# elif a>b:
#     print('a is greater than b')
# else:
#     print('a is equal to b')

# x = int(input('int x '))
# y = int(input('int y '))    
# z = int(input('int z '))
# if x>y:
#     print('x is greater')
# elif x>z:
#     print('x is greater')
# elif z>y:
#     print('z is greater')
# else:
#     print('y is greater')


# x = int(input('sub a '))
# y = int(input('sub b '))    
# z = int(input('sub c '))
# result = x+y+z
# avg = result/3
# if avg>=90:
#     print('Grade A')
# elif avg>=80:
#     print('Grade B')
# elif avg>=70:
#     print('Grade C')
# elif avg>=60:
#     print('Grade D')
# elif avg>=50:
#     print('Grade E')
# else:
#     print('Fail')

# x = int(input('enter your age '))
# if x>=65 and x<=100:
#     print('You are senior citizen')
#     print('You are old age')
# elif x>=18 and x<=64:
#     print('You are adult')
# elif x>=12 and x<=17:
#     print('You are teenager')
# elif x>=5 and x<=11:
#     print('You are kid')
# else:
#     print('please enter valid age')







# B) ***Iterative Statements
# i) for loop:-
# a = 'nami'
# for n in a:
#     print(n)

# for x in range(5):
#     print(x)

# for x in range(1,5):
#     print(x)

# for x in range(1,10,2):
#     print(x)

# for x in range(10,1,-2):
#     print(x)

# for x in [10,20,30,40]:
#     print(x)

# for x in 'nani':
#     print(x)

# for x in range(1,10):
    # print(x*x)

# for x in 'nani':
#     print(x*3)







# ii) ***while loop
# a = 10
# b = 20
# while a<b:
#     print(a , ' is less than b')
#     a+=1
# print(a)

# a = int(input('enter a number '))
# b = 1
# while b<=a: print(b*b); b+=1
# print()
# b=1
# while b<=a: print(b*b*b); b+=1

# while True: 
#     print('hello')

# a = 10
# while a==10:
#     print('hello')

# i = 1
# while True:
#     print(i)
#     i+=1





# Nested Loops
# for i in range(5):
#     for j in range(5):
#         print(i,',',j,end='\t')
#     print()

# for i in range(5):
#     for j in range(5):
#         print(i,',',j,sep='',end='\t')
#     print('\n')




#c) ***(Transfer Stmts) in Control Statements
# a) break
# for x in range(10):
#     print(x)
#     if x==9:
#         break

# i = 0
# while i<=100:
#     if i==50:
#         break
#     print(i)
#     i=i+1

# i=2
# while True:
#     if i==50:
#         break
#     print(i)
#     i+=1



# b) continue stmt
# i=0
# while i<=100:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

# for i in range(1,101,1):
#     if i%3==0:
#         continue
#     print(i)





# c) pass statement:-
# if a < b:
#     pass

# def a():
#     pass

# class a:
#     pass

# for x in range(1,101,1):
#     if x%3==0:
#         print(x)
#     else:
#         pass






    