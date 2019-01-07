print """In this project, we'll build a basic calendar that the user will be able to interact with from the command line. """

from time import sleep, strftime

user_name = "Aileen"

calendar = {}

def welcome():
  print "Welcome to your calendar " + user_name + "!"
  print "Calendar is opening."
  sleep(1)
  print "Current date is " + strftime("%A %b %d %Y")
  print "Current time is " + strftime("%I:%M:%S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else: 
       print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update successful!"
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "Invalid date"
        try_again = raw_input("Try Again? Y for Yes, N for No:  ")
        try_again = try_again.uppercase()
        if try_again == "Y":
          continue
        else:
          start == False
      else: 
        calendar[date] = event
        print "Added successfully!"
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        event = raw_input("What Event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print "Date deleted"
            print calendar
          else: 
            print "This date does not exist"
    elif user_choice == "X":
      start == False
      break
    else: 
      print "Invalid command"
      start == False
      
start_calendar()