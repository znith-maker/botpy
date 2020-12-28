import datetime # importing datetime module 
import pywhatkit#importinh pywhatkit module
try:  # handeling an error for clearity
    show_date_and_time = datetime.datetime.now()#methods to use datetime module
    print(show_date_and_time)#for printing date and time
except:
    pass#exceptions may pass
sendng_number = input("Type number: ")#for own profit breaking a part
send_message = input("Enter your message: ")
add_time = int(input("when do you want to send(international time):"))
add_min = int(input("add min: "))

try: #onother handeling error
    pywhatkit.sendwhatmsg(sendng_number, send_message, add_time, add_min)   
except:
    print("code didn't work")#exception may print that