
import pyodbc
# for random review ID
import random
import string

conn = pyodbc.connect('driver={SQL Server};server=CS-DB-MS1;uid=s_dba56;pwd=q2jqLLEFf2F3RtPA;database=dba56354')

print(conn)

# check the validity of user input
# def chech_invalid_input(menuInput):
#     while menuInput != (1 or 2 or 3 or 4 or 0):
#         menuInput = input("Invalid input. Possible inputs are (0, 1, 2, 3, 4) Try again ==> ")
#     return menuInput

# ask for user id
userID = str(input("User ID ==> "))
def checkUserId(userID):
    cursor = conn.cursor()
    SQLCommand = ("""Select * From user_yelp U where U.user_id = '""" + (userID) + """'""")
    cursor.execute(SQLCommand)
    result = cursor.fetchone()
    return result

def checkYesNoBlankInput(input):
    if(input == 'y' or input == 'n'):
        return True
    else:
        return False

def checkIntegerValidity(value):
    try:
        int(value)
    except:
        return True
    return False

results = checkUserId(userID)

while results == None:
    userID = input("Not such User ID. Try again ==> ")
    results = checkUserId(userID)

# main menu
menu = -1
while menu != 0:
    menu = input(
            """Choose (number of) menu option:
            (1) Seach Business
            (2) Search Users
            (3) Make Friend
            (4) Write Review
            (0) Exit Application
            ==> """)
    while checkIntegerValidity(menu):
        print(ValueError)
        menu = input("Invalid input. Possible inputs are (0, 1, 2, 3, 4) Try again ==> ")
        print(menu, type(menu))
    while int(menu) < 0 or int(menu) > 4:
        menu = input("Invalid input. Possible inputs are (0, 1, 2, 3, 4) Try again ==> ")
        print(menu, type(menu))
        while checkIntegerValidity(menu):
            print(ValueError)
            menu = input("Invalid input. Possible inputs are (0, 1, 2, 3, 4) Try again ==> ")
            print(menu, type(menu))
    menu = int(menu)
    ####################################################### search business options ############################################
    if(int(menu) == 1):
        isSearched = False
        while isSearched == False:
            print("Choose filters options for Business:")
            minStarsOption = input("(1) Minimum number of stars (y/n) ==> ")
            while checkYesNoBlankInput(minStarsOption) == False:
                minStarsOption = input("Invalid filtering input. (1) Minimum number of stars (y/n) ==> ")
            maxStarsOption = input("(2) Maximum number of stars (y/n) ==> ")
            while checkYesNoBlankInput(maxStarsOption) == False:
                maxStarsOption = input("Invalid filtering input. (2) Maximum number of stars (y/n) ==> ")
            cityNameOption = input("(3) City name (or leave blank) ==> ").casefold()
            businessNameOption = input("(4) Business name (partial or leave blank) ==> ").casefold()
            isInputCorrect = input("""The following filtering will be : 
                    Minimum number of stars: """ + str(minStarsOption) + """
                    Maximum number of stars: """ + str(maxStarsOption) + """
                    City name: """ + str(cityNameOption) + """
                    Business name: """ + str(businessNameOption) + """
                        Choose (number of) next step:
                        (1) Do you want to procced?  
                        (2) Do you want to change filtering options?
                        (0) Do you want to go back to the main menu? 
                        ==>""")
            while int(isInputCorrect) < 0 or int(isInputCorrect) > 2 == True:
                isInputCorrect = input("Invalid input. Try again ==> ")
            if(int(isInputCorrect) == 1):
                #print the outputs of filtering
                i = 1
                cursor = conn.cursor()
                SQLCommand = ("""Select * From business B where 1 = 1""")
                if(cityNameOption != ""):
                    SQLCommand += (""" and B.city = '""" + cityNameOption + """'""")
                if(businessNameOption != ""):
                    SQLCommand += (""" and B.name like '%""" + businessNameOption + """%'""")
                if(minStarsOption == 'y'):
                    SQLCommand1 = SQLCommand + (" and B.stars = (select MIN(B.stars) from business B)")
                    print(SQLCommand1)
                    cursor.execute(SQLCommand1)
                    for rows in cursor.fetchall():
                        print("---------- Busuness %d ----------"%i)
                        print("business_id:  " + str(rows[0]))
                        print("name:         " + str(rows[1]))
                        print("address:      " + str(rows[2]))
                        print("city:         " + str(rows[3]))
                        print("postal_code:  " + str(rows[4]))
                        print("stars:        " + str(rows[5]))
                        print("review_count: " + str(rows[6]))
                        print("------------------------")
                        i += 1
                    if not cursor.fetchall():
                        print("Nothing found")
                if(maxStarsOption == 'y'):
                    SQLCommand2 = SQLCommand + (""" and B.stars = (select MAX(B.stars) from business B)""")
                    cursor.execute(SQLCommand2)
                    for rows in cursor.fetchall():
                        print("---------- Busuness %d ----------"%i)
                        print("business_id:  " + str(rows[0]))
                        print("name:         " + str(rows[1]))
                        print("address:      " + str(rows[2]))
                        print("city:         " + str(rows[3]))
                        print("postal_code:  " + str(rows[4]))
                        print("stars:        " + str(rows[5]))
                        print("review_count: " + str(rows[6]))
                        print("------------------------")
                        i += 1
                    if not cursor.fetchall():
                        print("Nothing found")
                if(minStarsOption == 'n' and maxStarsOption == 'n'):
                    cursor.execute(SQLCommand)
                    for rows in cursor.fetchall():
                        print("---------- Busuness %d ----------"%i)
                        print("business_id:  " + str(rows[0]))
                        print("name:         " + str(rows[1]))
                        print("address:      " + str(rows[2]))
                        print("city:         " + str(rows[3]))
                        print("postal_code:  " + str(rows[4]))
                        print("stars:        " + str(rows[5]))
                        print("review_count: " + str(rows[6]))
                        print("------------------------")
                        i += 1
                    if not cursor.fetchall():
                        print("Nothing found")
                isSearched = True
            if(int(isInputCorrect) == 0):
                # search is done. Go back to manu
                isSearched = True
            #go back to filtering     
    #################################################### search users #################################################################
    if(int(menu) == 2):
            isSearched = False
            while isSearched == False:
                userNameOption = input("(1) Name (full or partial) ==> ").casefold()
                
                isUsefulOption = input("(2) Useful (y/n) ==> ")
                while checkYesNoBlankInput(isUsefulOption) == False:
                    isUsefulOption = input("Invalid filtering input. (2) Useful (y/n) ==> ")
                isFunnyOption = input("(3) Funny (y/n) ==> ")
                while checkYesNoBlankInput(isFunnyOption) == False:
                    isFunnyOption = input("Invalid filtering input. (3) Funny (y/n) ==> ")
                isCoolOption = input("(4) Cool (y/n) ==> ")
                while checkYesNoBlankInput(isCoolOption) == False:
                    isCoolOption = input("Invalid filtering input. (4) Cool (y/n) ==> ")
                
                isInputCorrect = input("""The following filtering will be : 
                        User Name: """ + str(userNameOption) + """
                        Useful (y/n): """ + str(isUsefulOption) + """
                        Funny (y/n): """ + str(isFunnyOption) + """
                        Cool (y/n): """ + str(isCoolOption) + """
                            Choose (number of) next step:
                            (1) Do you want to procced?  
                            (2) Do you want to change filtering options?
                            (0) Do you want to go back to the main menu? 
                            ==>""")
                while int(isInputCorrect) < 0 or int(isInputCorrect) > 2 == True:
                    isInputCorrect = input("Invalid input. Try again ==> ")
                if(int(isInputCorrect) == 1):
                    #print the outputs of filtering
                    i = 1
                    cursor = conn.cursor()
                    SQLCommand = ("""Select * From user_yelp U where 1 = 1""")
                    if(userNameOption != ""):
                        SQLCommand += (""" and U.name like '%""" + userNameOption + """%'""")
                    if(isUsefulOption == 'y'):
                        SQLCommand += (""" and U.useful > 0 """)
                    if(isFunnyOption == 'y'):
                        SQLCommand += (""" and U.funny > 0 """)
                    if(isCoolOption == 'y'):
                        SQLCommand += (""" and U.cool > 0 """)
                    
                    print(SQLCommand)
                    cursor.execute(SQLCommand)
                    for rows in cursor.fetchall():
                        print("---------- User %d ----------"%i)
                        print("user_id:       " + str(rows[0]))
                        print("name:          " + str(rows[1]))
                        print("yelping_since: " + str(rows[3]))
                        print("useful:        " + str(rows[4]))
                        print("funny:         " + str(rows[5]))
                        print("cool:          " + str(rows[6]))
                        print("------------------------")
                        i += 1
                    if not cursor.fetchall():
                        print("Nothing found")
                if(int(isInputCorrect) == 0):
                    # search is done. Go back to manu
                    isSearched = True
            #go back to filtering
    ###################################################### make friends ####################################################################
    if(int(menu) == 3):
            friendSearchOption = int(input(
            """Search user to befriend:
            (1) Input User ID manually
            (0) Go Back
            ==> """))
            while friendSearchOption < 0 or friendSearchOption > 1:
                friendSearchOption = int(input("Invalid input. Possible inputs are (0, 1) Try again ==> "))
            if(friendSearchOption == 1):
                isSearched = False
                while isSearched == False:
                    friendID = input("Please enter user ID to befriend ==> ")
                    while friendID == "":
                        friendID = input("No ID given. Try again ==> ")
                    cursor = conn.cursor()
                    # finding if user with friend ID exists
                    SQLCommand = ("""Select * From friendship F where F.user_id = '""" + friendID + """'""")
                    cursor.execute(SQLCommand)
                    result = cursor.fetchone()
                    if not result:
                        print("No such user ID found.")
                        isSearched = True
                    else:
                        #cheching if users are already frineds
                        cursor = conn.cursor()
                        SQLCommand1 = ("""Select * From friendship F where F.user_id = '""" + userID + """' and F.friend = '""" + friendID + """'""")
                        cursor.execute(SQLCommand1)
                        result = cursor.fetchone()
                        if result:
                            print("User is already friends with selected ID.")
                            isSearched = True
                        else:
                            cursor = conn.cursor()
                            SQLCommand = ("insert into friendship(user_id, friend) values (?, ?)")
                            valuesToInsert = [userID, friendID]
                            cursor.execute(SQLCommand, valuesToInsert)
                            conn.commit()
                            print("You became friends.")
                            isSearched = True

    ####################################################### write review ###################################################################
    if(int(menu) == 4):
            reviewBusinessSearchOption = int(input(
            """Search user to befriend:
            (1) Input Business ID manually
            (0) Go Back
            ==> """))
            while reviewBusinessSearchOption < 0 or reviewBusinessSearchOption > 1:
                reviewBusinessSearchOption = int(input("Invalid input. Possible inputs are (0, 1) Try again ==> "))
            if(reviewBusinessSearchOption == 1):  
                isSearched = False
                while isSearched == False:
                    businessID = input("Please enter business ID to review ==> ")
                    while businessID == "":
                        businessID = input("No ID given. Try again ==> ")
                    cursor = conn.cursor()
                    # finding if business with given ID exists
                    SQLCommand = ("""Select * From business B where B.business_id = '""" + businessID + """'""")
                    cursor.execute(SQLCommand)
                    result = cursor.fetchone()
                    if not result:
                        print("No such business ID found.")
                        isSearched = True
                    else:
                        starsForReview = int(input("Please provide number of stars (integer between 1 and 5) ==>"))
                        while starsForReview < 1 or starsForReview > 5:
                            starsForReview = int(input("Invalid umber of stars. \nPlease provide number of stars (integer between 1 and 5) ==>"))
                        reviewID = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(22))
                        cursor = conn.cursor()
                        # finding if random review ID exists already
                        SQLCommand = ("""Select * From review R where R.review_id = '""" + reviewID + """'""")
                        cursor.execute(SQLCommand)
                        result = cursor.fetchone()
                        while result:
                            reviewID = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(22))
                            cursor = conn.cursor()
                            # finding if new random review ID exists already
                            SQLCommand = ("""Select * From review R where R.review_id = '""" + reviewID + """'""")
                            cursor.execute(SQLCommand)
                            result = cursor.fetchone()
                        print("review ID: "+ reviewID +" user ID: " + userID + " business ID: " + businessID + " num of stars: " + str(starsForReview) + " to be added to DB")
                        cursor = conn.cursor()
                        SQLCommand = ("insert into review(review_id, user_id, business_id, stars) values (?, ?, ?, ?)")
                        valuesToInsert = [reviewID, userID, businessID, starsForReview]
                        cursor.execute(SQLCommand, valuesToInsert)
                        conn.commit()
                        isSearched = True

conn.commit()
conn.close()
print(conn)