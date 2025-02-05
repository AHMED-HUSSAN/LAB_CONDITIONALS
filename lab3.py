
#movie name
Movie = str("Interstaller")

#movie rate
The_rate = 3

#popularity rate
Popularity = 75

#if conditional checks
if The_rate >= 4 and Popularity > 80 :
     print("Highly recommended")
     
elif The_rate >= 3 and Popularity > 70 :
     print("I recommended it . It is good")
    
elif The_rate <= 2 and Popularity > 60 :
    print("You should check it out!")

elif The_rate <= 2 and Popularity < 50 :
     print("Don't watch it. It is a waste of time")
     
