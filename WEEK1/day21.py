"""
# Arithmetics Operetor

print(2+3)

print(2+int('3'))

print(2*'3')
#3が2回出力される→33

print(2/3)
#割り算いつでも結果はfloat

print(10%3)

print(10//4)
#小数点以下は表示されない

#Comparison operators
print(3 == 4)
print(3 != 3)

x=(1,2,3,4,5)
print(4 in x)
#4はinside　x

x=[1,2,3,4,5]
print(4 not in x)
#4はinside　x ではない


#Logical operators
print(4 > 5 or 5 > 10)
print((4 > 5 or 5 > 10)and(3 == 3 or 3 <=4))
print(not(4 > 5 or 5 > 10)and(3 == 3 or 3 <=4))

#String operation
name = input('What is your name:')
age = int(input('How old are you?'))
print('Hi {} you are already {} ?'.format(name,age))
#orderの順番に設定する必要がある
print(f'Hi {name} you are already {age}.')
#new format 




word = "Lorem Ipsum Dolor"

print(word[:5])
print(word[:-5])

print(word.split('o'))


word = ['I am','Jan','Cebu']
print('/'.join(word))

word ='Lorem Ipsum Dolor'
new_word = word.replace('o','a')
print(new_word)


speed = 210
if speed > 160 and speed <= 200 :
    print('Over Speeding')
elif speed > 200:
    print('It is not a car its plane')
elif speed == 0:
    print('Stopped')
else:
    print('Speed is not limit yet.')

"""
"""
You will ask the user for his/her age:
first if the age is less than 18
    you are underage
if age is greaterthan or equal 18
    you are in legal age
if age is greaterthan or equal 60 but not greaterthan 120
    you are in Senior age
else
    age is invalid
"""

"""
age = int(input('your age:'))

if age < 18 and age >= 0:
    print('you are underage')
elif age >= 18:
    print('you are in legal age')
elif age >= 60 and age <120:
    print('you are in Senior age')
else:
    print('age is invalid')

"""
"""
#print(range(1,10))
mylist = [1,2,3,4,5,6,7]
count = 20
for i in range(1,count+1):
    if i%2 != 0:
        print(f'odd number{i}')
    else:
        print(f'even number {i}')

students = ["Taka","Hiro","Ayaka"]
print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)

for i,student in enumerate(students):
    print(f'[{i}]{student}')
"""
"""
x = 0
while x <= 10:
    print(x)
    x+=1
"""
"""
count = 10
while True:
    answer = input('input x to break and c to continue:')
    if answer == 'c':
        count =input('enter a number:')
        for i in range(1,int(count)+1):
            print(i)
        continue
    else:
        print('Stopped')
        break
"""

# numbers = [i*2 for i in [1,2,3,7]]
numbers = [i*2 for i in range(1,10) if i%2==0]
print(numbers)
