while 3 == 3:
    import random
    a = ["Heyo!", "Hey!", "Hi there!"]
    b = random.choice(a)
    import random
    c = ["Have a good day/night!", "Leave a potato if I helped!", "Glad I helped!", "PM me if you have any questions!"]
    d = random.choice(c)
    print ("Welcome to Trainee Tryhard post writer")
    print ("What kind of post would you like? Only type in the number.")
    print ("1: Unfair punishment complaint")
    print ("2: Trainee app got denied")
    print ("3: Misc. idea (disagree)")
    print ("4: Misc. idea (agree)") 
    print ("5: Misc. question")
    print ("6: Application")
    print ("7: New update")
    print ("8: First reply")
    answer = input()

    if answer == "1":
        print ("Was the punishment by a staff member (1) , or a false GWEN ban (2)?")
        print ("Answer with the number")
        type1 = input()
        if type1 == "1":
            print (b)
            print ("I think your punishment was fair. Please refrain from breaking the rules.",d)
        else:
            print (b)
            print ("Go to https://xen.mineplex.com/appeals to appeal your false ban.",d)
    if answer == "2":
        print (b)
        print ("Please PM the recruiter about your application.",d)
    if answer == "3":
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
    if answer == "8":
        print (b)
        print ("First reply!",d)
    print (" ")
    print (" ")
