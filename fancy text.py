#ask for name 

name = input("Good day! What is your name? ")
print("Hi, " + name + " You look great today!")

#ask for dream job
def sharing_dream_job(): 
    answer = input("Would you like to share your dream job? ")
    if answer.lower() in ("yes", "sure", "I would like to"):
        job = input("That's nice! What is your dream job then? ")
        return job
    else:
        print("That's okay! You going to figure it out like you always do!")
        return None
#call the funtion
job = sharing_dream_job()
if job: 
    print("That's an amzaing job! " + name)

#use fancy text


