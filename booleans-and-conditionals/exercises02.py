engine_indicator_light = "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttle_speed = 15000

# 3) Write conditional expressions to satisfy the following safety rules:

# a) If crew_status is true, print "Crew Ready" else print "Crew Not Ready".
if crewStatus == True:
    print("Crew Ready")
else:
    print ("Crew Not Ready")

# b) If computerStatusCodeis 200, print "Please stand by. Computer is rebooting." Else if computerStatusCodeis 400, print "Success! Computer online." Else print "ALERT: Computer offline!"
if computerStatusCode == 200:
    print("Please stand by. Computer is rebooting.")
elif computerStatusCode == 400:
    print("Success! Computer online.")
else:
    print("ALERT: Computer offline!")

# c) If shuttle_speed is > 17,500, print "ALERT: Escape velocity reached!" Else if shuttle_speed is < 8000, print "ALERT: Cannot maintain orbit!" Else print "Stable speed".
if shuttleSpeed > 17500:
    print("ALERT: Escape velocity reached!")
elif shuttleSpeed < 8000:
    print("ALERT: Cannot maintain orbit!")
else:
    print("stable speed")

# 4) PREDICT: Do the code blocks shown in the Section D produce the same result?

<<<<<<< HEAD
if crewStatus and computerStatusCode== 200 and space_suits_on:
   print("all systems go")
else:
   print("WARNING. Not ready")

if crewStatus != True or computerStatusCode!= 200 or not(space_suits_on):
   print("WARNING. Not ready")
else:
   print("all systems go")

# print("Yes" or "No")
print("yes")
=======
# print("Yes" or "No")
>>>>>>> upstream/main
