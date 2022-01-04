def main():

 data=input("Do you want to convert 'String' or 'Integer' to Binary?: (S/I)") #getting an input (String or Integer)

 if data=="S" or data=="s": #if input is S or s do:
   sitring=str(input("What text should I convert to  Binary?:")) #get a text input
   print(' '.join(format(ord(x), 'b') for x in sitring)) #simply gets the string input's unicode equivalent and turns that into binary
 if data=="I" or data=="i": #if first iput is I or i do:
   intecir=int(input("What number should I convert to Binary?:")) #want a number input
   i=bin(intecir) #convert that number onto binary with a build-in function
   print(i[2:]) #print the i without it's first 2 characters
   print("This program is made by me, Karan. I hope this program helped you. See ya!")
main()
again=str(input("Do you want to reuse this program (Y/N)"))
if again=="Y" or "y":
  main()
else:
  exit()
