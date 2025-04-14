#w=len(input("what is your name: ").strip())      
#print(w)

#print(len(input("what is your name: ").strip()) ) 
# 执行顺序，1 what is your name  2.strip（） 3len 4 print

# a =input("a: ") 
# b =input("b: ") 
# c = 空杯， a = 牛奶 ，b = coffe 

# #c = a # 先定义 空杯里面装什么 ，现在空杯里面是牛奶
# # a = b #牛奶空杯 去接咖啡
# #b = c  # 咖啡空杯去接 牛奶
# c = b
# b = a
# a = c

# print("a = "+ a ) #+a 是变化后a的新值
# print('b = '+ b )

#pri#city = input(str("What is  name of city you grew up in?\n ")).capitalize()
 #问题后面输入\n 会让插入光标（cursor）出现在下一行
#pet_name= input(str("what is the name of your pet?\n")).capitalize()
#print("Your band name could be " + city + " " + pet_name)
#Do not forget + before city and pet_name 

#DAY2 
#print("Welcom to the tip calculator")
#total_bill= float(input("What was the total bill? $ "))
#people=int(input("How many people to split the bill? "))
#percentage_tip = int(input("What percentage tip would you like to give ? 10,12,or 15? "))

#Each_person_should_pay= (total_bill/people) + (total_bill*percentage_tip/100/people)
#fee=round(Each_person_should_pay,2)
#print(f"Each person should pay  ${fee} ")

#two_digit_number=input("Type a two digit number: " )
#first_number=int(two_digit_number[0])
  #second_number=len(two_digit_number,[1]) wrong code 
  #len()count how many digit  eg:52 is 2
  #(two_digit_number[0]) is the first digit  eg: 52 is 5 
#second_number=int(two_digit_number[1])
#sum=first_number +second_number
#print(sum)

#height=float(input("Entry your height in m : "))
#weight= float(input("Entry your weight in kg: "))
#BMI = round(weight / height **2) #使用round让结果是一个整数
#print(BMI)
#if BMI <=18.5:
    #print("Your weight is underweight")
#elif BMI> 18.5 and BMI >= 25:
  #print(" Your have  a normal weight")
#elif BMI>25 and BMI <30 :
   #print(" You have a  over weight ")
#else:
   #print("You have an clinicalli obese")

#year=int(input("which year do you want to check?"))

#if year % 4 ==0:
    #if year % 100 == 0:
        #if year %400 == 0:
            #print(" It is a leap year")
        #else:
            #print("it is not a leap year")
    #else:
        #print("it is a leap year")
#else:
   #print("it is not a leap year")


#print (8//3) in this case we wii get 2 integer number

#score =0 
#height =1.0
#inWinning = True
#print ("your score is "+str(score))
#print(f"you score is {score}")
#print(f' your score is {score} your height is {height} your are winning is {iswinning}')

#age= int(input("What is your current age? "))
#age_remaing = 90 - age
#days_remaing= age_remaing  *365
#month_remaing=age_remaing *12
#week_remaing= age_remaing  *52
#print(f" You have {days_remaing} days,{month_remaing} months and {week_remaing} weeks")

 #Day 3

#number = int(input("input a number: "))
#reminder = number % 2
#if reminder == 0:
    #print("The number is an even number")
#else:
    #print("The number is an odd number")

#number = int(input("input a number: "))
#if number % 2== 0:
    #print("The number is an even number")
#else:
    #print("The number is an odd number")

#height= int(input("entry your height(cm):"))
#age =int(input ("entry your age: "))
#bill = 0 #设置初始化的价格，后面根据年龄变化
#if height >=120:
    #print("you can ride the rollercoaster")
    
#if age <= 18 and age >12 :
       #bill = 7
       #print ("Please pay 7 dollas")
    #elif age <12:
        #bill =5
        #print("Please pay $5")
     #elif age >= 45 and age <=55:
         #bill=0
         #print("free")
    #else:
        #bill =12
        #print("please pay 12 dollas")
    #wants_phonto = input("do you want a phone taken ?Yes or No: ").strip() .upper()
    #if wants_phonto =="YES":
       #bill +=3 #新的bill = 旧bill + 3  bill = bill+3  可以简写成 bill+=3
       #print(f"you finnal pay {bill}")
    

#else:
    #print("sorry you have to grow taller before you can ride")

#d3.4 pizza order exercise

#print("welcome to pthon pizza deliverise")
#size = input("what size pizza do you want? s ,m,l") .strip().capitalize()
#add_pepperoin =input("Do you want pepperoni? y or n").strip().capitalize()
#extra_cheese = input ("would you like extra cheese: y or n").strip().capitalize()
#price = 0 #设置初始化数值0
#if size == "S":
   #price = 15 #这里值得注意的是price = 15 赋予新的值 15 ，也可以写成 price+=15，
   #不能写成price == 15 比较操作符。
# 用于判断变量 price 的值是否等于 15。
# 是一个表达式，返回 True 或 False
   #if add_pepperoin =="Y" and extra_cheese == "Y":
      #price += 3
      #print (f"please pay {price}")
   #elif add_pepperoin =="Y" and extra_cheese == "N":
      #price += 2
      #print (f"please pay {price}")
   #elif add_pepperoin =="N" and extra_cheese == "Y":
      #price += 1
      #print (f"please pay {price}")
   #else:
      #price +=0
      #print (f"please pay {price}")


#elif size == "M" :
   #price = 20
   #if add_pepperoin =="Y" and extra_cheese == "Y":
      #price = 23
      #print (f"please pay {price}")
   #elif add_pepperoin =="Y" and extra_cheese == "N":
      #price = 22
      #print (f"please pay {price}")
   #elif add_pepperoin =="N" and extra_cheese == "Y":
    #price = 21
    #print (f"please pay {price}")
   #else:
      #price =20
      #print (f"please pay {price}")
#else:
  #price =25
  #if add_pepperoin =="Y" and extra_cheese == "Y":
      #price = 28
      #print (f"please pay {price}")
  #elif add_pepperoin =="Y" and extra_cheese == "N":
      #price = 27
      #print (f"please pay {price}")
  #elif add_pepperoin =="N" and extra_cheese == "Y":
    #price = 26
    #print (f"please pay {price}")
  #else:
      #price =25
      #print (f"please pay {price}")
#视频答案：
#size = input("what size pizza do you want? s ,m,l") .strip().capitalize()
#add_pepperoin =input("Do you want pepperoni? y or n").strip().capitalize()
#extra_cheese = input ("would you like extra cheese: y or n").strip().capitalize()
#price = 0

#if size == "S":
   #price += 15
#elif size =="M":
   #price +=20
#else :
   #price += 25

#if add_pepperoin =="Y" :
    #if size =="S":
       #price+=2
    #else:
       #price+=3

#if extra_cheese == "Y":
   #price +=1

#print(f"you final pay {price}")

#print("Welcome to the code below")
#name1= input("What is your name ?\n") .strip() .lower() 
#name2= input("What is your name ?\n") .strip() .lower()
#combined_string = name1+ name2
#t=combined_string. count("t")
#r=combined_string. count("r")
#u=combined_string. count("u")
#e=combined_string. count("e")
#true = t+r+u+e 
#The program adds up the counts of t, r, u, and e to calculate the total "TRUE" score, 
# which is the sum of all occurrences of these four characters.


#l=combined_string. count("l")
#o=combined_string. count("o")
#v=combined_string. count("v")
#e=combined_string. count("e")
#love = l+o+v+e

#love_score =int(str(true)+ str(love))
# str（true）代表十位数值，str（love）代表个位数值。
#先两个数黏在一起，例如：ab ，1a，43这样
#再将这两个数变成数值，value。

#print(love_score)
#if love_score <10 or love_score>90:
    #print(f'Your love score is {love_score},you go together like coke and mo')
#elif love_score >= 40 and love_score<=50:
    #print(f'you love score is {love_score},you are alringt together.')
#else:
    #print(f"you score is {love_score}")

#day 3 打印
#print(" Welcome to Treasure Island.You mission is to find the trwasure")
#first_select= input("Select left or ringt \n").strip() .lower()
#下面两行重复的错误代码，导致进入if first— select == left以后，会重新跳出来循环 下面两行代码删掉就OK了。

#重复second_select= input("Select swim or wait \n").strip() .lower()
#重复third_select= input("Select the door red ,yellow or blue \n").strip() .lower()

#if first_select == "left":
    #second_select = input("Select swim or wait \n").strip() .lower()
    #if second_select == "wait":
        #third_select= input("Select the door red ,yellow or blue \n").strip() .lower()
        #if third_select == "yellow":
            #print("You Win !")
        #else:
            #print("Game Over!")  
    #else:
       #print("Game Over!")
        
#else:
    #print("Game Over!")

#day 4 randomisation
#import random  
#random_integer = random.randint(1,10)# 包含10
#print (random_interger)

#random_float = random. random()# between 0 and 1 ,not including 1 
#0.0000....-- 0.999999
# how to creat a dencimal number  between 0 to 5?
# random_flort = random. random()
#random_float *5

# coin games
# import random  
# random_side = random.randint(1,2)# 包含10
# if random_side == 1:
#     print("heads")
# else:
#     print("tails")

#list
#states_of_america=[ "a","b","c","d"] # oder is 0 start
#states_of_america[2]= "3" # change c to 3
#states_of_america. append("angelala") # add "angelala" at the end

#print(states_of_america)

# who pad the bill
# import random
# name_string = input("give me everyone's name ,sperated by a comma: \n")
# names=name_string.split(",")
# num_item=(len(names)) # count how many names input
 
# random_choice = random.randint(0, num_item -1)
# pay_bill_person = names[random_choice]
# print(f"{pay_bill_person}  will pay the bill ")

import random#chatgpt

# Ask the user for names separated by commas
name_string = input("Give me everyone's name, separated by a comma: \n")

# Split the input string by commas
names = name_string.split(',')

# Strip any extra spaces around names (optional)
names = [name.strip() for name in names]

# Print the list of names
print("Names in the list:", names)

# Randomly select one person to pay the bill
pay_bill_person = random.choice(names)

# Print the selected person
print(f"The person who will pay the bill is: {pay_bill_person}")

#D4 
# row1= ["😄","😄","😄"]
# row2= ["😄","😄","😄"]
# row3= ["😄","😄","4"]

# map=[row1,row2,row3]
# print(f'{row1}\n{row2}\n{row3}')
# position=input(" where di you want to put the treasure? ")

# horizonal =int (position[0])
# vertical = int (position[1])
# print(map[vertical -1])
