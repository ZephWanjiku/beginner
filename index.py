______________________________________
'''Number Guessing Game
The number guessing game is a popular game among programmers. In the number guessing game, the program selects a random number between two numbers, and the user guesses the correct number. I will take you through a tutorial on creating a number guessing game using the Python programming language.
So below is how you can write a program to create a number guessing game using Python:'''
import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")      

________________________________________
'''Group Anagrams using Python
Grouping anagrams is one of the popular questions in coding interviews. Here you will be given a list of words, 
and you have to write an algorithm to group all the words which are anagrams of each other. 
So below is how you can write a Python function to group anagrams:'''
from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()
"""Now let's test the function by creating a list of words containing anagrams and some other words:"""
words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))
dict_values([['tea', 'eat', 'ate'], ['bat'], ['arc', 'car']])
________________________________________
'''Find Missing Number using Python
Finding the missing number in an array means finding the numbers missing from the array according to the range of values inside the array. 
Most of the time, the question you get based on this problem is like:
•	Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.
To find the missing number in an array, we need to iterate over the input array and store the numbers in 
another array that we didn’t find in the input array while iterating over it. Below is how you can find the missing
 number in an array or a list using the Python programming language:'''
def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))
Output: [4, 12, 15]
________________________________________
'''Group Elements of Same Indices using Python
To group elements of the same index, you will initially have two or more lists inside a list like [[a, b], [c, d]]. 
To group the elements of these lists, you need to create two new lists where you will store the elements of 
both the lists at index 0 [a, c] and index 1 [b, d]. That is the meaning of grouping the elements of the same indices.
Now below is how you can group the elements of the same indices using the Python programming language:'''
inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][ index])
    index = index + 1
a, b, c = outputLists[0], outputLists[1], outputLists[2]
print(a, b, c)
[10, 40, 70] [20, 50, 80] [30, 60, 90]
________________________________________
'''Mean Median and Mode using Python
Mean
The mean is the average value of all the values in a dataset. To calculate the mean value of a dataset,
 we first need to find the sum of all the values and then divide the sum of all the values by the total number 
 of values. So here’s how to calculate the mean using Python:'''
# Mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print(mean)
20.2
'''Median
The Median is the middle value among all the values in sorted order. Here we need to calculate the mid-value of all 
the values in a dataset. But before calculating the Median, we need to arrange all the values in sorted order. There are two different ways of calculating the median value:
1.	when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
2.	when the total number of values is odd: Median = {(n+1)/2}thterm
Now below is how you can calculate the median using Python:'''
# Median
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = li
20.0
'''Mode
Mode is the most frequently occurring value among all the values. Below is how we can calculate the mode 
value of a dataset using Python:'''
# Mode
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
20
________________________________________
'''Execution Time of a Python Program
It is important to calculate the execution time when working on a large project. When working on a large project, we have several approaches in mind. The best should be the one that takes the shortest execution time in all scenarios.
So to calculate the execution time of a Python program, we need to follow the steps mentioned below:
1.	First, store the time of initiation of the program into a variable;
2.	Write the Python program;
3.	Store the end time of the program into a variable;
4.	Subtract the time of initiation of the program from the end time of the program;
In the end, you will get the execution time of your program in seconds.
Calculating Execution Time of a Python Program
Now let’s follow the process described in the above section to calculate the time taken by a Python program. 
Here I will write a simple program to create acronyms:'''
from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)

________________________________________
'''Count Number of Words in a Column using Python
Most data science professionals use the pandas library for data handling and preparation. The pandas library doesn’t have any method to count the number of words in a piece of text. One way to solve this problem is by finding the length of the text by splitting the complete text.
So let’s import a textual dataset where we can count the number of words in a column:'''
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')
print(data.head())
'''0  Data analysis is the process of inspecting and...   
1  The performance of a machine learning algorith...   
2  You must have seen the news divided into categ...   
3  When there are only two classes in a classific...   
4  The Multinomial Naive Bayes is one of the vari...   

                                               Title  
0                  Best Books to Learn Data Analysis  
1         Assumptions of Machine Learning Algorithms  
2          News Classification with Machine Learning  
3  Multiclass Classification Algorithms in Machin...  
4        Multinomial Naive Bayes in Machine Learning  
The dataset has two columns Article and Title. Let’s create a new column as the number of words in the article column:
data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())
                                             Article  \
0  Data analysis is the process of inspecting and...   
1  The performance of a machine learning algorith...   
2  You must have seen the news divided into categ...   
3  When there are only two classes in a classific...   
4  The Multinomial Naive Bayes is one of the vari...   

                                               Title  Number of Words  
0                  Best Books to Learn Data Analysis               76  
1         Assumptions of Machine Learning Algorithms               56  
2          News Classification with Machine Learning               70  
3  Multiclass Classification Algorithms in Machin...               66  
4        Multinomial Naive Bayes in Machine Learning               96  '''
________________________________________
'''Rock Paper Scissors Game using Python
To create and play rock paper scissors, I will be using the if and elif statements in Python. I will prepare this game to be played between two players. Player-1 will be the user, and player-2 will be the computer. Player one will manually select the rock paper or scissor, while player two will choose randomly. So I will also use the random module in Python to create this game.
I hope you now have understood everything about the rock, paper, and scissors game and how I will create it. 
Now, below is how we can write a Python script to create and play rock paper scissors using Python:'''
import random

player1 = input("Select Rock, Paper, or Scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Player 2 selected: ", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Wins")

________________________________________
'''Print Emojis using Python
Smiling, thumbs up, and the heart emoji are some of the emojis we often use while texting our friends or colleagues. It’s possible to print any emoji using the Python programming language. To print emojis using Python, you need to install the emoji module in your Python virtual environment. You can easily install it by using the pip command on your terminal or command prompt as mentioned below:
•	pip install emoji
The emoji.emojize method helps you write the description of any emoji inside “::” while writing a piece of text. Below are examples of descriptions of some of the popular emojis:
1.	:thumbs_up:
2.	:red_heart:
3.	:smiling_face:
You can use the description of any emoji inside “::” to print the emoji using Python. 
You can find the description of all the emojis here. Now let’s have a look at an example of how to'''
#  print emojis using Python:
import emoji

print(emoji.emojize("I love reading books:books:"))
print(emoji.emojize("Some people have a very sensitive heart:red_heart:, please be kind with them.:hibiscus:"))
'''I love reading books📚
Some people have a very sensitive heart❤️, please be kind with them.🌺
Correct Spellings using Python
The SpellChecker module in Python is one of the handiest tools that can be used to correct misspelt words in a piece of text. If you have never used this Python module before, you can easily install it in your Python virtual environment by running the command mentioned below in your command prompt or terminal:
•	pip install pyspellchecker
Now below is how you can use this module to correct any misspelt word using Python:
from spellchecker import SpellChecker'''
corrector = SpellChecker()

word = input("Enter a Word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)

________________________________________
'''Scraping GitHub Profile using Python
When we open any GitHub account, we see a profile picture, the name of the user, and a short description of the user in the profile section. Here you will learn how to scrape your GitHub profile image. For this task, you need some knowledge of HTML and the requests and BeautifulSoup libraries in Python.
If you have never used the BeautifulSoup library before, use the command mentioned below in your command prompt or terminal to install this library in your Python virtual environment:
•	pip install beautifulsoup4
You don’t need to install the requests library as it is already present in the Python standard library. 
Now below is how to write a Python program to scrape a profile image from any GitHub profile:'''
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/amankharwal"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper

________________________________________
'''Visualize a Linear Relationship using Python
When the value of variable increases or decreases with the increase or decrease in the value of another variable, then it is nothing but a linear relationship. When we visualize a linear relationship, it shows whether the relationship between the two features is linear or not.
You can use any data visualization library in Python to visualize a linear relationship. I prefer to use plotly as it provides interactive results. But as so many Python programmers use matplotlib for data visualization, I will show you how to visualize a linear relationship with Python using plotly and matplotlib.
Visualizing Linear Relationships using Python
So let’s import a dataset and all the necessary Python libraries for this task:'''
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding = 'latin1')
data = data.dropna()
  
figure.show()
 
'''To visualize linear relationships using matplotlib, you have to use seaborn.regplot method. So here's 
how to plot linear relationships by using the matplotlib library in Python:'''
plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()
 
________________________________________
'''Generate Text using Python
Let's import the GPT-2 model from the transformers library and start with the task of generating text using Python:'''
from transformers import pipeline
model = pipeline("text-generation", model = "gpt2")
'''Downloading: 100%
665/665 [00:00<00:00, 8.60kB/s]
Downloading: 100%
523M/523M [00:11<00:00, 43.5MB/s]
Downloading: 100%
0.99M/0.99M [00:00<00:00, 1.74MB/s]
Downloading: 100%
446k/446k [00:00<00:00, 1.74MB/s]
Downloading: 100%
1.29M/1.29M [00:00<00:00, 3.44MB/s]'''
'''Here's how you can generate text using Python by using the GPT-2 model:'''
sentence = model("Hi, My name is John Cena, I am here", 
                 do_sample=True, top_k=50, 
                 temperature=0.9, max_length=100, 
                 num_return_sentences=2)

for i in sentence:
  print(i["generated_text"])
'''Hi, My name is John Cena, I am here to see you. I have been here this entire time. I've worked. 
I've seen all these things. It's just, man, my life has changed because of you guys. You guys get to
 see everything, including my career, things like that. You guys have, you know, the most amazing stuff about me.'''

'''JANUARY 10, 2015:

After the match, the fans were happy.
________________________________________
Scrape Table from a Website using Python
There are many Python libraries and modules that you can use for web scraping. To scrape a table from a website, 
I will use the urllib module in Python, which is already available in the Python standard library. 
So you don't need to install any external library to scrape data from a website. Below is how you 
can use the urlib module to scrape a table from a website using Python programming language:'''
import urllib.request
import pandas as pd
url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

with urllib.request.urlopen(url) as i:
    html = i.read()
    
data = pd.read_html(ht
    '''Websites Popularity(unique visitors per month)[1]  Front-end(Client-side)  \
0  Google[2]                               1600000000  JavaScript, TypeScript   
1   Facebook                               1120000000              JavaScript   
2    YouTube                               1100000000   JavaScript,TypeScript   
3      Yahoo                                750000000              JavaScript   
4       Etsy                          516,000,000[15]              JavaScript   

                               Back-end(Server-side)  \
0             C, C++, PHP, Go,[3] Java, Python, Node   
1  Hack, PHP (HHVM), Python, C++, Java, Erlang, D...   
2             C, C++, Python, PHP, Java, [11] Go[12]   
3                                                PHP   
4                                        PHP[16][17]   

                                     Database  \
0                     Bigtable,[4] MariaDB[5]   
1     MariaDB, MySQL,[9] HBase, Cassandra[10]   
2            Vitess, BigTable, MariaDB[5][13]   
3  PostgreSQL, HBase, Cassandra, MongoDB,[14]   
4                            MySQL, Redis[18]   

                                               Notes  
0           The most used search engine in the world  
1            The most visited social networking site  
2  The most popular video sharing site [YouTube i...  
3                                                NaN  
4                                E-commerce website.  
In the code above, I am collecting data from a table available on a webpage that contains a table describing the programming languages used in most popular companies. You can see the data we have received after web scraping is about the programming languages and databases being used by companies. So this is how you can scrape tables from any website using the Python programming language.
If you want to save this data in a CSV file, below is how you can save it:
data.to_csv("programming.csv")
After running the above code, you will see the CSV file saved on the same directory where your Python file is.'''
________________________________________
'''Extract Text from PDF with Python
You must know how to collect text from pdf as a Python developer. This skill is useful when working with resumes. Extracting text from a pdf file is not a difficult task at all. For this task, you need to install a Python library known as PyPDF2.
You can easily install this Python library by using the pip command in your terminal or command prompt 
as mentioned below:'''
#pip install pypdf2
#After installing this Python library, we are all prepared for extracting text from any pdf file. Below is how you can extract text from any PDF file using the Python programming language:
import PyPDF2
pdf = open("Aman.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())
#In the fourth line of the above code, the getPage() method will help you specify the page number you want to extract text from.
________________________________________
#Reverse a String using Python
'''There are many ways to reverse a string using Python. You can use any method that you find easy unless you are told to use a specific method.
You must have heard of the concept of slicing in Python. Here I will show you how to use string slicing to
 reverse a string using Python:'''
def reverse_string(string):
    return string[::-1]

a = "lawrahK namA"
print(reverse_string(a))
#Output:
#Aman Kharwal
#The first character in the string has index 0, and the last character has index n-1, where n is the length of the string. The string slicing operator “::” reads all the characters of the string, and -1, in the end, reverses the order of the characters. This is how we can reverse a string.
________________________________________
#SequenceMatcher in Python
#The SequenceMatcher class is available in the difflib module in Python, which is available in the Python standard library. You do not have to install it before using it. There are many classes in the difflib module to compare texts. One of those classes is SequenceMatcher which calculates how well the sequence of two texts matches each other. In simple words, it finds similarities in the sequence of two different texts.
#Let’s see how to use this class to find similarities in the sequence of two texts. I will first input two very similar texts into this class:
from difflib import SequenceMatcher
text1 = "My Name is Aman Kharwal"
text2 = "Hi, My Name is Aman Kharwal"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")
#Both are 92.0 % similar
#So, according to the score above, it shows that both the text inputs have very similar sequences. Now let’s try it with text inputs that are dissimilar from each other:
text1 = "My Name is Aman Kharwal"
text2 = "I am the founder of thecleverprogrammer.com"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")
#Both are 24.242424242424242 % similar
#So, according to the score above, it shows that both the text inputs have less similar sequences. This is how you can use this class in Python available in the difflib module.
________________________________________
#QR Code using Python
#QR codes have a variety of uses; from creating a payment gateway to showing you the food menu of a restaurant, a QR code is being used in several ways. Over the past five years, several businesses have started that are only based on creating QR codes for a business. So if you know how to create a QR code, it will be helpful for you in many ways.
#So to create QR codes using the Python programming language, you first need to make sure that you have the PyQRCode and pypng modules installed in your Python virtual environment. You can easily install both of these modules by executing the commands mentioned below in your command prompt or terminal:
#•	pip install PyQRCode
#•	pip install pypng
#After installing these modules, you can start writing a program to create a QR code using Python, as shown in the code section below:
import pyqrcode
import png
link = "https://www.instagram.com/the.clever.programmer/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)
#The QR code generated by this Python program will be saved on the same directory where your Python file is.
________________________________________
#Decode a QR Code using Python
#I recently shared an article on creating a QR code using Python. If you want to learn about creating a QR code, you can learn more about it from here. To decode a QR code, you need an image of a QR code. You can use any QR code image for this tutorial, or you can create your QR code.
#For decoding QR codes using Python, you need to install two Python libraries in your Python environment; pyzbar and pillow. You can install both these libraries by executing the commands mentioned below in your command prompt or terminal:
#1.	pip install pyzbar
#2.	pip install pillow
#Now below is how you can write a program to decode a QR code using Python:
from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open('instagram.png'))
print(decocdeQR[0].data.decode('ascii'))
https://www.instagram.com/the.clever.programmer/
________________________________________
#Create Dummy Data using Python
#To create dummy data using Python, we can use the faker library. The faker library generates fake data randomly. If you have never used this library before, you can easily install it by using the pip command mentioned below in your command prompt or terminal:
#•	pip install faker
#Now let’s look at some examples of this library before creating a dummy dataset. The code below will return a fake name, address, and text randomly:
from faker import Faker
fake = Faker()
print(fake.name())
print(fake.address())
print(fake.text())
Sean Obrien
2606 Mackenzie Tunnel Apt. 215
East Ericfurt, CO 88091
#Building job station sometimes what language money. Able air really it study suffer health. Body why approach difference case notice choose.
#Every time you will run this code, you will get different results. Now let’s see how to create fake data for creating a dummy dataset using Python.
#The Faker().profile() method returns fake data about job profiles containing 13 columns. So below is how you can create a dummy dataset using Python:
from faker import Faker
import pandas as pd
fake = Faker()
data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)
print(data.head())
#                                      job  ...   birthdate
# 0  Engineer, control and instrumentation  ...  1949-06-13
# 1                     Editor, film/video  ...  1959-07-23
# 2                           Chiropractor  ...  1927-12-12
# 3                           Nurse, adult  ...  1996-11-02
# 4                      Personnel officer  ...  1953-08-19

# [5 rows x 13 columns]
# You can learn more about creating fake data using the faker library from here.
________________________________________
# Remove Cuss Words using Python
# In a research, it was found that on an average, 80-90 words that a person speaks every day, 50-70% of all the words are cuss words. So it means people find it normal while exchanging conversations with cuss words. But sometimes, we need to remove such words from a piece of text to make it available to the audience of every age group.
# So to remove cuss words, by using the Python programming language, we need to install the better_profanity library in our Python environment. It helps identify and remove the cuss words by inserting the * symbol in each letter of a cuss word.
# To install this Python library in your Python environment, you need to execute the command mentioned below in your command prompt or terminal:
# •	pip install better_profanity
# After installing this Python library, below is how you can write a program to remove cuss words using Python:
from better_profanity import profanity
text = "Please leave me alone and just piss off"
censored = profanity.censor(text)
print(censored)
# Please leave me alone and just ****
# So, as you can see in the output, the cuss word has been removed from the text, and we see four stars instead of the cuss word.
________________________________________
# Find Duplicate Values using Python
# To write a program to find duplicate values using Python, I will define a Python function that will take a list of values in any data type. So below is a Python function for finding duplicate values in a list:
def find_duplicates(x):
    length = len(x)
    duplicates = []
    for i in range(length):
        n = i + 1
        for a in range(n, length):
            if x[i] == x[a] and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates
# names = ["Aman", "Akanksha", "Divyansha", "Devyansh", 
#          "Aman", "Diksha", "Akanksha"]
# ['Aman', 'Akanksha']
# Below is how the above function works:
# 1.	The above function takes a list as an input;
# 2.	Then it calculates the length of the list;
# 3.	Then it looks for the same value in the list that is found on the first index;
# 4.	If it finds multiple values, it appends that value in another list of duplicate values;
# 5.	This process continues till the loop reaches the final index of the list. In the end, it returns the list of duplicate values. 
# You can use this function on a Python list of any data type.
________________________________________
# Detect Questions using Python
# To write a Python program to detect whether a sentence is a question or not, we first need to create a list of words that we see at the start of an interrogative sentence. For example, what is your name? where do you live?, in these two questions, “what” and “where” are the types of words we need to store in a python list. Next, to check if a sentence is a question or not, we need to check if any word from the list is present at the beginning of the sentence. If it is present, then the sentence is a question, and if it is not present, then the sentence is not a question.
# Now below is how we can detect questions using Python by following the logic explained in the above section:
from nltk.tokenize import word_tokenize
question_words = ["what", "why", "when", "where", 
             "name", "is", "how", "do", "does", 
             "which", "are", "could", "would", 
             "should", "has", "have", "whom", "whose", "don't"]

question = input("Input a sentence: ")
question = question.lower()
question = word_tokenize(question)

if any(x in question[0] for x in question_words):
    print("This is a question!")
else:
    print("This is not a question!")
# Input a sentence: Do you have any feelings for me?
# This is a question!
# So this is how you can easily detect whether a sentence is a question or not.
________________________________________
# Voice Recorder using Python
# You must have used a voice recorder on your smartphone or your computer once in your life. We generally use it to record a voice message, and some video creators use it to record the voice for their videos. To create a voice recorder using the Python programming language, you need to use the sounddevice library in Python. If you have never used this library before, you can easily install it by using the pip command mentioned below:
# •	pip install sounddevice
# The sounddevice library will help you to record your voice, but to save your voice in a specific file format, 
# you need to use the SciPy library in Python, which can be installed by using the pip command:
# •	pip install SciPy
# Now below is how you can create a voice recorder using Python:
import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")

voice_recorder(10, "record.wav")
# In the above code, I have defined a Python function to record and save your recorded files. It takes two parameters:
# 1.	The first parameter is seconds, where you will enter the number of seconds you want to record your voice.
# 2.	The second parameter is the file, where you will input the name by which you want your recorded file to be saved. 
# For example, “voice.wav”.
# After running the above code, it will show you a message that the recording has started, and after the number of seconds 
# that you have given as input, it will show you that the recording is complete. Once completed, 
# it will automatically be saved to the same directory where your Python file is located.
________________________________________
# Reading and Writing CSV Files using Python
# You can read and write a CSV file without using any Python module or a library. But as we use the pandas 
# library to work with data, this article will teach you how to read and write a CSV file using the pandas library in Python.
# So let’s start by writing a CSV file. Here I will first create a sample data using a Python dictionary about 
# the name and age of students, and then I will store that Python dictionary into a CSV file:
# writing a csv file
import csv
import pandas as pd
data = {"Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"], 
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_data.ccsv", index=False)
#        Name  Age
# 0      Aman   23
# 1    Diksha   21
# 2  Akanksha   25
# 3     Sajid   23
# 4    Akshit   22
# So this is how you can write a CSV file using Python. Now below is how you can read this CSV file using Python:
# reading a csv file
import pandas as pd
data = pd.read_csv("age_data.csv")
print(data.head())
#        Name  Age
# 0      Aman   23
# 1    Diksha   21
# 2  Akanksha   25
# 3     Sajid   23
# 4    Akshit   22
# So this is how easy it is to read and write a CSV file using the pandas library in Python.
________________________________________
# Box Plot using Python
# I will start by importing the necessary Python libraries and a dataset that we can use to visualize box plots using Python:
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data.head())
   Unnamed: 0     TV  Radio  Newspaper  Sales
0           1  230.1   37.8       69.2   22.1
1           2   44.5   39.3       45.1   10.4
2           3   17.2   45.9       69.3    9.3
3           4  151.5   41.3       58.5   18.5
4           5  180.8   10.8       58.4   12.9
# Now below is how you can visualize a box plot using the Python programming language:
import plotly.express as px
fig = px.box(data, y="TV")
fig.show()
 
# So this is how you can easily visualize box plots using Python.
________________________________________
# Send Instagram Messages using Python
# To send Instagram message using Python, you need to have an Instagram account and the instabot library installed 
# in your Python virtual environment. Instabot is a Python library that you can use to automate features of your 
# Instagram account using Python, like sending messages without even opening your application. 
# You can install this Python library by using the pip command mentioned below:
# •	pip install instabot
# I hope you now have installed the instabot library in Python, now below is how you can send 
# Instagram messages using Python:
from instabot import Bot
bot = Bot()

bot.login(username="Your Username", password="Your Password")
bot.send_message("Hi Brother", ["Receiver's Username"])
# In the above code, I am using the login function of the instabot library to login into my Instagram account using Python.
#  Here you have to use the username parameter to input your username and the password parameter to input your password.
#   Then, in the next line, I am using the send_message function to send the message where the first parameter is 
#   the message itself and the second parameter is the username of the Instagram account you want to send a message to.
________________________________________
# Age Calculator using Python
# Age Calculator is an amazing application to create as a beginner in any programming language. 
# To create an age calculator, you need two dates:
# 1.	today's date
# 2.	date of birth
# You can either ask the user for both dates or just ask for the date of birth and use today's date from the 
# computer itself. Asking for the birthday only seems like a more user-friendly option. So here’s how to create 
# an age calculator using Python:
def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(1998, 9, 3)
# In the above code:
# 1.	I have first defined a Python function where I am asking for three user inputs:
# •	y: year of birth 
# •	m: month of birth 
# •	d: date of birth
# 2.	Then I am importing the datetime module in Python inside the function
# 3.	Then in the next line, I am taking today’s date by using the datetime.now() method of the datetime module
# 4.	Then I have introduced a new variable in the next line as dob, 
# where I am using the date of birth as the input given by the user
# 5.	Then I am subtracting the dob with today’s date and then dividing it by 365.25 which is returning the age of the user.
________________________________________
# LCM using Python
# Finding LCM of two numbers means finding the smallest number that is a multiple of both the numbers. 
# Python has many inbuilt functions that you can use for mathematical calculations, but unfortunately, 
# it doesn’t have any function to calculate the LCM of two or more numbers. 
# So for calculating the LCM of two numbers using Python, you have to define your Python function. 
# So below is how you can find the LCM of two numbers using Python:
def least_common_multiple(a, b):
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while(True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm

print(least_common_multiple(10, 12))
60
# In the code above, I defined a Python function, where I used two parameters as a and b. Then I find the large 
# number between the two numbers and divide the larger number with both the numbers in a while loop where 
# the value of the larger number will be increased by 1 until we get 0 as a remainder. So this is how you 
# can find the least common multiple of two numbers using the Python programming language.
________________________________________
# Price Elasticity of Demand using Python
# I will start the task of calculating price elasticity of demand using Python by 
# creating a small dataset that should contain data about the change in the price and the demand for a product:
import pandas as pd
data = pd.DataFrame({"Demand": [20, 30, 31, 33, 30, 33, 35], 
                     "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600]})
print(data)
#   Demand  Price
# 0      20   2000
# 2      31   1850
# 3      33   1700
# 4      30   1800
# 5      33   1700
# 6      35   1600
# The first rows of this dataset contain the initial demand and price for a product, and the subsequent rows contain the change in demand and the change in the price of the product. Now our next step is to add two more columns as the Percentage change in Demand and Percentage change in Price by calculating them:
# data["% Change in Demand"] = data["Demand"].pct_change()
# data["% Change in Price"] = data["Price"].pct_change()
# print(data)
#    Demand  Price  % Change in Demand  % Change in Price
# 0      20   2000                 NaN                NaN
# 1      30   1800            0.500000          -0.100000
# 2      31   1850            0.033333           0.027778
# 3      33   1700            0.064516          -0.081081
# 4      30   1800           -0.090909           0.058824
# 5      33   1700            0.100000          -0.055556
# 6      35   1600            0.060606          -0.058824
# Now the last step is to calculate the price elasticity of demand (% Change in Demand / % Change in Price) by adding a new column to this data. Below is how you can calculate it using Python:
# data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]
# print(data)
#    Demand  Price  % Change in Demand  % Change in Price  Price Elasticity
# 0      20   2000                 NaN                NaN               NaN
# 1      30   1800            0.500000          -0.100000         -5.000000
# 2      31   1850            0.033333           0.027778          1.200000
# 3      33   1700            0.064516          -0.081081         -0.795699
# 4      30   1800           -0.090909           0.058824         -1.545455
# 5      33   1700            0.100000          -0.055556         -1.800000
# 6      35   1600            0.060606          -0.058824         -1.030303
#python #programming #developer #morioh #programmer #softwaredeveloper #computerscience #webdev #webdeveloper #webdevelopment #pythonprogramming #pythonquiz #ai #ml #machinelearning #datascience

