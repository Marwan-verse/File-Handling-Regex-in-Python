from time import sleep  #importing sleep function to pause execution for a moment

#

with open('filename.txt', 'r') as f:   # read mode
    for line in f: #loop for every line to print
        print(line) #to print
        line.strip()  #display each line without extra spaces or newlines at the start or end

with open('filename.txt', 'w') as f:   # write mode (overwrites)
    f.write("Hello World\n")    #writes Hello World to file and delete everything else

sleep(1)  # Pause for a moment to ensure file write is complete

with open('filename.txt', 'r') as f:   # read mode
    for line in f:  #loop for every line to print
        print(line) #to print
        line.strip()  #display each line without extra spaces or newlines at the start or end

with open('filename.txt', 'a') as f:   # append mode
    f.write("line ammended\n")  #appends line ammended to the end of the file

sleep(1)  # Pause for a moment to ensure file write is complete

with open('filename.txt', 'r') as f:   # read mode
    for line in f:  #loop for every line to print
        print(line) #to print
        line.strip()  #display each line without extra spaces or newlines at the start or end


with open('filename.txt', 'w') as f:   # write mode (overwrites)
     f.write("""Beneath the sky, a whisper flows,
Where sunlight dances, softly glows.
A fleeting breeze, a gentle tune,
The world awakes beneath the moon.

Leaves will flutter, rivers run,
Dreams take flight with setting sun.
In quiet moments, hearts may find
A spark of hope, a peace of mind.\n""") #random poem
 
    
