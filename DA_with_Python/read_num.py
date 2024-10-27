#initialize variables to hold total,count and avarage
count=0
total=0
while True:
    #prompt user for input
    inp=input('Enter a number:')
    if inp.lower()=='done':
        break
    try:
        #convert input to float and Updated the Total and Count
        num=float(inp)
        total=total+num
        count=count+1
    except ValueError:
        #if input is not a valid number,print an error message
        
        print("Invalid Input. Please enter a Valid Number")
        #calculate the avarage if there were any values entered
if count > 0:
    maximum=max({num})
    minimum=min({num})
    print(f"Total: {total}, Count: {count}, Max: {maximum}, Min: {minimum}")
else:
    print('No valid inputs were entered')
        

    
        
