#ask for name 

name = input("\033[1;36;40mGood day! What is your name? ")
print("Hi, " + name + " You look great today!")

#ask for dream job
def sharing_dream_job(): 
    answer = input("Would you like to share your dream job? ")
    if answer.lower() =="no":
        print("That's okay! You going to figure it out like you always do!")
        return None
    else:
        job = input("That's nice! What is your dream job then? ")
        return job
    
#call the funtion
job = sharing_dream_job()

if job: 
    print("That's an amzaing job! " + name)

#use fancy text
import pyfiglet
fancy_text = pyfiglet.figlet_format("Padayon! Our Future " + job + "!", font="slant")
print(fancy_text)

