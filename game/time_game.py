__author__ = 'jakewahl'

import csv
import numpy

# globals to be used in game:
acct_dict = {}
current_player = None
current_score = 0

# Load the acct_dict from file
try:
    with open("userInfo.txt", 'r') as f:
        rdr = csv.reader(f)
        # add each line as another account in acct_dict
        for acct_str in rdr:
            acct_dict[acct_str[0]] = [acct_str[1], int(acct_str[2])]
except IOError as e:
    # initialize the dictionary as non-empty because if empty the dictionary would not be iterable
    acct_dict = {"testAcct": ["testPw", 9000]}

# Loop through login sequence until they successfully find or create an account
while current_player is None:
    username = raw_input("Username: ")
    playerExists = False
    # Determine if username already exists
    for user in acct_dict:
        if user == username:
            playerExists = True
    # If player exists have them try to login
    if playerExists:
        password = raw_input("Password: ")
        while password != acct_dict[username][0] and password != "exit":
            print "Incorrect, type exit to leave or try again"
            password = raw_input("Password: ")
        else:
            if password != "exit":
                current_score = acct_dict[username][1]
                print "Starting points: " + str(acct_dict[username][1])
                current_player = username
    # Otherwise make a new account
    else:
        if "yes" == raw_input("Are you trying to create a new account (yes or no)?"):
            password = raw_input("Password: ")
            # 'Exit' is unacceptable because it used to restart login
            while password == "exit":
                password = raw_input("choose new password, exit not acceptable: ")
            acct_dict[username] = [password, 0]
            print "Starting points: " + str(acct_dict[username][1])
            current_player = username
current_score = acct_dict[username][1]
# play game

question = int(raw_input("How many questions would you like?: "))

while question > 0:
    # Create two floats from 0 to 12
    numb_lst = numpy.random.uniform(0, 13, 2)
    # Cast the floats as integers multiplied by each other in a string
    ans = raw_input("{0} * {1}: ".format(int(numb_lst[0]), int(numb_lst[1])))
    # If user types in a non-integer, program won't crash, question will be asked again
    while True:
        try:
            x = int(ans)
            break
        except ValueError:
            print "Oops! Not an acceptable integer!"
            ans = raw_input("{0} * {1}: ".format(int(numb_lst[0]), int(numb_lst[1])))
    # Check if the user answer is correct
    while int(ans) != int(numb_lst[0]) * int(numb_lst[1]):
        current_score -= 50
        ans = raw_input("{0} * {1}".format(int(numb_lst[0]), int(numb_lst[1])))
    else:
        current_score += 10
        question -= 1

print "You now have {} points".format(current_score)
# Update acct_dict with current user score
acct_dict[username][1] = current_score
# For every line in the acct_dict, cast as string and write to a file
with open("userInfo.txt", "w") as infoFile:
    acct_string = ""
    for k,v in acct_dict.iteritems():
        acct_string = acct_string + "{}".format(k)
        for thing in v:
            acct_string = acct_string + ",{}".format(str(thing))
        acct_string = acct_string + "\n"
    infoFile.write(acct_string)