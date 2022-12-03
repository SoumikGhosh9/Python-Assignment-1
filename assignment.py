
# You are a pilot, cruising at an altitude of 33000 ft,
# you want to land your plane, to land your plane, you need
# to be under 5000ft take input from the pilot, what
# is your current altitude, and suggest
# the pilot to go around if the altitude is more than 10K feet,
# if its more than 5K suggest the pilot to land the plane
# by bringing it to 1000ft

print("Pilot cruising in 33000 feet and want to land his plane")
a = int(input ("hey please enter your altitude :"))
print("current altitude is :",a)
b=5000
c=10000
d=1000
if(a <= d):
    print("land safely")
elif(a >= b):
    print ("bring the plane into 1000 feet and then land")
elif(a <= c):
    print ("Go around")




