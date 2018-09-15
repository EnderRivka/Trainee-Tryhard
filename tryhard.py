while 3 == 3: #this keeps the program in a loop
    import random #selects a random 
    a = ["Heyo!", "Hey!", "Hey there!"] #these are some greetings
    b = random.choice(a) #this chooses which greeting
    import random #imports another random for closing
    c = ["Have a good day/night!", "Leave a potato if I helped!", "Glad I helped!", "PM me if you have any questions!"] #these are the closings
    d = random.choice(c) #this selects a closing
    print ("Welcome to Trainee Tryhard post writer") 
    print ("What kind of post would you like? Only type in the number.")
    print ("1: Unfair punishment complaint")
    print ("2: Trainee app got denied")
    print ("3: Misc. idea (disagree)")
    print ("4: Misc. idea (agree)") 
    print ("5: Misc. question")
    print ("6: Application")
    print ("7: New update")
    answer = input() #asks you what option you want

    if answer == "1":
        print ("Was the punishment by a staff member (1) , or a false GWEN ban (2)?") #over here it asks you which type of ban, then after that will give you 2 different responses based on that
        print ("Answer with the number")
        type1 = input()
        if type1 == "1": #if they choose a punishment from a staff member it will show this one
            print (b)
            print ("I think your punishment was fair. Please refrain from breaking the rules.",d)
        else:
            print (b) #this is if they choose the other one
            print ("Go to https://xen.mineplex.com/appeals to appeal your false ban.",d)
    if answer == "2":#another one, but it doesn't ask you, it just prints out the text
        print (b)
        print ("Please PM the recruiter about your application.",d)
    if answer == "3": #same as previous
        print (b)
        print ("I think it's fine the way it is now.",d)
    if answer == "4":
        print (b)
        print ("I think that's a great idea and it will benifit Mineplex!",d)
    if answer == "5":
        print (b)
        print ("Go to https://xen.mineplex.com/support/ and the support staff should be able to help you!",d)
    if answer == "6":
        print (b)
        print (" You can apply for Trainee at https://xen.mineplex.com/application. Go to https://xen.mineplex.com/apps to see the list of applications.",d)
    if answer == "7":
        print (b)
        print ("This update sounds really great! Thank you devs for making this update!",d)
    print (" ") #since it loops, I added these blanks so you can distinguish between the times it loops.
    print (" ")
