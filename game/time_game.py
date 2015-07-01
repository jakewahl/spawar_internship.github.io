__author__ = 'jakewahl'

import csv
import numpy

acct_dict = {"testAcct": ["testPw", 9000]}
current_player = None
current_score = 0
try:
    lst = []
    with open("userInfo.txt", 'r') as f:
        rdr = csv.reader(f)
        for x in rdr:
            acct_dict[x[0]] = [x[1], int(x[2])]
except IOError as e:
    acct_dict = {"testAcct": ["testPw", 9000]}

while current_player is None:
    username = raw_input("Username: ")
    playerExists = False
    for user in acct_dict:
        if user == username:
            playerExists = True
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
    else:
        if "yes" == raw_input("Are you trying to create a new account (yes or no)?"):
            password = raw_input("Password: ")
            while password == "exit":
                password = raw_input("choose new password, exit not acceptable: ")
            new_acct = [password, 0]
            acct_dict[username] = new_acct
            print "Starting points: " + str(acct_dict[username][1])
            current_player = username
current_score = acct_dict[username][1]
# play game

question = int(raw_input("How many questions would you like?: "))

# while they haven't lost against the timer
while question > 0:
    numb_lst = numpy.random.uniform(0, 13, 2)
    ans = raw_input("{0} * {1}".format(int(numb_lst[0]), int(numb_lst[1])))
    while int(ans) != int(numb_lst[0]) * int(numb_lst[1]):
        current_score -= 20
        ans = raw_input("{0} * {1}".format(int(numb_lst[0]), int(numb_lst[1])))
    else:
        current_score += 10
        question -= 1


print "You now have {} points".format(current_score)
acct_dict[username][1] = current_score
with open("userInfo.txt", "w") as infoFile:
    acct_string = ""
    for k,v in acct_dict.iteritems():
        acct_string = acct_string + "{}".format(k)
        for thing in v:
            acct_string = acct_string + ",{}".format(str(thing))
        acct_string = acct_string + "\n"
    infoFile.write(acct_string)

