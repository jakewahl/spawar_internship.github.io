#Jake Wahl's 2015 Summer SPAWAR Internship
***
###Week 1
*DAY 1 (6/23)*:  
- I learned the basics of Linux and started to learn Python.  Iterative and recursive lines.  
- Completed a number of easy Python challenges from Scott.  Here they are: [LearningPython](https://github.com/jakewahl/spawar_internship.github.io/blob/master/Easy_Python_Challenge.ipynb)
- Awesome Python Computer Language tutorial: [The Python Tutorial](https://docs.python.org/2/tutorial/)
- Helpful Linux Commands:
```
~ $ cd internship/game/
```
**go to another folder (change directory)**
```
~ $ ipython notebook
```
**open up ipython notebook dashboard**
```
~ $ ipython notebook file.ipynb
```
**open up a specific .ipynb**
```
~ $ /opt/pycharm-community-4.5.1/bin/pycharm.sheuler
```
**open up pycharm**

*DAY 2 (6/24)*:  
- Started the day by searching for an online class about Python.  Found codecademy.com, started the 13 hr Python class.  
- Ran through iterations and recursions again on whiteboard.  Factorial both iterative and recursive.  
- Intro to random walks, then installed numpy to generate random lists and arrays.

*DAY 3 (6/25)*: 
- Learned how to trace through code to find errors. Project Euler questions 1 - 3.  [Project Euler problems](https://github.com/jakewahl/spawar_internship.github.io/blob/master/euler.ipynb)

***

###Week 2
*DAY 4 (6/29)*: 
- Project Eueler 4 - 5.  ipython notebook has new folders.    
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
- Look at the rest of my problems!:
[ProjectEuler1-6](http://127.0.0.1:8888/65ad8a2f-ffc8-4757-8249-9fa0b7e272d3)

*DAY 5 (6/30)*:
- Took a tour of 4 labs at the Photonic labs.  
- MATLAB class.  
- Started a simple math game.  Create/save accounts with usernames, passwords, and scores.  Gives two random numbers to be multiplied and the player must answer them within a time limit.  Started with the mapping project.

*DAY 6 (7/1)*:
- Finished multiplication game.  
- Program crashes when a non-integer is typed, so I will add an exception handler.

*DAY 7 (7/2)*:
- Added an exception handler to my game.  Now when any other type is inputed, they can repeat the question with no penalty.  Here is an example of my try statement:
```
try:
    question = int(raw_input("How many questions would you like?: "))
except ValueError:
    print "Please type a number!"
```
- Also plotted csv data on to a map using leaflet.  It looks something like this:

![pic](/mapping/index_cluster_pic.png)
***
###Week 3
*DAY 8 (7/6)*:
- Started the day off with linear algebra.  Learned about vectors and matrices and dot products.  Two ipython notebook programs for dot products and unit vectors.  
- Continued my game and made a few modifications.  Added a timer per question and some print statements to say if the question was wrong or not.  Currently trying to add an exception to handle a string input after the "how many questions" question is asked.

*DAY 9 (7/7)*:  
- Added an exception handler for the "how many questions?" part of my game.  
- A ton of linear algebra was taught and somewhat absorbed, ~ 3.5 hours worth.  
- MATLAB class in the morning, coded for 1089 game.  
- Learning commands and uses of MySQL (Structured Query Language).  SQL lets you access and manipulate databases and information within databases.  Will start adding the info from the mapping project to a database tomorrow. 
- Successfully changed the game to where it also has a random operator as well as random numbers.  Using these functions:

```
def multiply(num1, num2):
    return int(num1) * int(num2)

def subtract(num1, num2):
    return int(num1) - int(num2)

def add(num1, num2):
    return int(num1) + int(num2)

def get_op(op):
    if "*" == op:
        return multiply
    elif "-" == op:
        return subtract
    elif "+" == op:
        return add
```
*DAY 10 (7/8)*:
- Signal processing (in my notebook).  
- Trying to understand Aaron's code for creating a database and adding our ship information into tables inside of the database.  Writing own code for this step.  
- Continuing to think of ideas to improve my math game.

*DAY 11 (7/9)*:
- Worked out an error in my math game.  If you got an answer wrong, then typed a non-int it would crash.  Added another exception handler in that part of my code.  
- I wanted the passwords in the userInfo.txt file to be ecrypted so I used base64.b64encode() to hide the passwords from other users, and it was successful.  I am happy with the way the game is right now! If you want to see it: [Jake's Game](https://github.com/jakewahl/spawar_internship.github.io/blob/master/game/time_game.py)
- Spent multiple hours updating my README.md with Dillinger Markdown.

***
###Week 4
*DAY 12 (7/13)*:
- Scott gave us an in-depth talk about his brief.  The discovery of anomalies (locating ships and humans) in Full-Motion Video.
- I started to work on Project Euler again.  I completed problems 6 through 8 today and I am currently working on 9.  
- Went to an intern meeting at 1:00 at the LOF.  Met a UCI Ph.D student studying Software Engineering who did her undergrad in Computer Science at Northwestern.  She works with Virtual Reality.

*DAY 13 (7/14)*:
- Worked on more Project Euler.  Finished problem 9 and and 10.  
- Started to code for least squares, finished it.  Will upload/comment it/add pic to github tomorrow. 

*DAY 14 (7/15)*:
- Commented the plot_stuff.py code and changed the standard deviation (std) multiple times to see its effect.
[Least Squares](https://github.com/jakewahl/spawar_internship.github.io/blob/master/leastsquares/linalg/plot_stuff.py)

![pic](/leastsquares/linalg/leastsquaresplot.png)

- Went to a Computer Networks Seminar
- Irwin Jacobs gave a speech on his life, entrepeneurship, and innovation in technology.  
- Throughout the day I have been reading sections of this book: [Introduction to Linear ALgebra by Gilbert Strang, a professor at MIT](http://www.amazon.com/Introduction-Linear-Algebra-Fourth-Edition/dp/0980232716)

