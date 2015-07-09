###Week 1
*DAY 1 (6/23)*:  
I learned the basics of Linux and started to learn Python.  Iterative and recursive lines.  

*DAY 2 (6/24)*:  
Started the day by searching for an online class about Python.  Found codeacademy.com, started the 13 hr Python class.  Ran through iterations and recursions again on whiteboard.  Factorial both iterative and recursive.  Intro to random walks, then installed numpy to generate random lists and arrays.

*DAY 3 (6/25)*: 
Learned how to trace through code to find errors. Project Euler questions 1 - 3.  (euler.ipynb)

###Week 2
*DAY 4 (6/29)*: 
Project Eueler 4 - 5.  ipython notebook has new folders.
Sample code for Project Euler 4:
```
i, b = 999, 999
pals = []
while b > 800:
    i = 999
    while i >= b:   
        pal = str(i * b)    
        if pal == pal[::-1]:
            pals.append(i * b)
        i = i - 1
    b = b - 1
print max(pals)
```

*DAY 5 (6/30)*:
Took a tour of 4 labs at the Photonic labs.  MATLAB class.  Started a game.  Create/save accounts with usernames, passwords, and scores.

*DAY 6 (7/1)*:
Finished multiplication game.  Program crashes when string is typed, so I will add an exception handler.

*DAY 7 (7/2)*:
Added an exception handler to my game.  Now when any other type is inputed, they can repeat the question with no penalty.
```
try:
    question = int(raw_input("How many questions would you like?: "))
    break
except ValueError:
    print "Please type a number!"
```

###Week 3
*DAY 8 (7/6)*:
Started the day off with linear algebra.  Learned about vectors and matrices and dot products.  Two ipython notebook programs for dot products and unit vectors.  Continued my game and made a few modifications.  Added a timer per question and some print statements to say if the question was wrong or not.  Currently trying to add an exception to handle a string input after the "how many questions" question is asked.

*DAY 9 (7/7)*:  
Added an exception handler for the "how many questions?" part of my game.  A ton of linear algebra was taught and somewhat absorbed, ~ 3.5 hours worth.  MATLAB class in the morning, coded for 1089 game.  Learning commands and uses of MySQL (Structured Query Language).  SQL lets you access and manipulate databases and information within databases.  Will start adding the info from the mapping project to a database tomorrow. Successfully changed the game to where it also has a random operator as well as random numbers.  

*DAY 10 (7/8)*:
Signal processing (in my notebook).  Trying to understand Aaron's code for creating a database and adding our ship information into tables inside of the database.  Writing own code for this step.  Continuing to think of ideas to improve my math game.

*DAY 11 (7/9)*:
Worked out an error in my math game.  If you got an answer wrong, then typed a non-int it would crash.  Added another exception handler in that part of my code.  I wanted the passwords in the userInfo.txt file to be ecrypted so I used base64.b64encode() to hide the passwords from other users.  Successful.
