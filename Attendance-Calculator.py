CurrentA = float(input("Enter Your current attendence:"))
NeededA = float(input("Enter the required attendence in your college:"))

if CurrentA >= NeededA:
    print("Dude chill out, this program is not written for you. You can chill out.")
else:
    subjects = int(input("Enter how many subjects your current sem have:"))
    subjectn = {}

    for i in range(subjects):
        subname = input(f"Enter the name of the subject {i+1}:")
        subjectn[subname] = float(input(f"Input your current attendence of subject {subname} :"))

    while True:
        for subname, subject in subjectn.items():
            print(f'Your current attendence of {subname} is {subject} :')

        iferror = input("If there is a mistake in any subject please enter the name of the subject to correct it, or if everything seems fine then type 'Confirm':")

        if iferror == "Confirm":
            break
        elif iferror in subjectn:
            subjectn[iferror] = float(input(f"Please enter the corrected score of the subject {iferror}:"))
        else:
            print("Please enter the correct subject name, try again.")

    lectures = {}
    lecturesPW=[]
    
   #for subname in subjectn:
        
    
    #    lectweek = float(input(f"Now enter how many lectures are there for the subject {subname} which has current attendence of {subjectn[subname]}:"))
     #  totallect=float(input(f"Now enter the total number of lectures till now of {subname}"))
    #    lectures[subname] = lectweek 
    for i in range(subjects):
      leccount=float(input("Enter How many total number of lectures are there of subject in order Per week:"))
      lecturesPW.append(leccount)
    
    lecturesPWSUM=sum(lecturesPW)
    Attentlec=float(input("Enter the Total Lectures attended by You (Sum of all attend lectures):"))
    TOTALLEC=float(input("Okay Last question:P, How many lectures have happended till now in this sem:"))
    
    
    for i in  range(20):
     Attentlec=Attentlec+lecturesPWSUM
     TOTALLEC=TOTALLEC+lecturesPWSUM
     res=int((Attentlec/TOTALLEC)*100)
     if res>=NeededA :
      print(f"You need to attend all the lectures for next {i+1} for meeting your collage attendeence criteria of {NeededA}")
      break         