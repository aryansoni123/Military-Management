import pickle
import csv
import mysql.connector



def perinsert():
    f=open("Personel_Details.dat", "ab")
    print("\n********************************************************\n")
    name=input("Enter Name: ")
    sv_num=input("Enter Sevice No.: ")
    age = input("Enter Age: ")
    while True:
        a=input("Enter Gender(Male/Female/Custom):")
        if a.upper()=="MALE":
            gender=a.upper()
            break
        elif a.upper()=="FEMALE":
            gender=a.upper()
            break
        elif a.upper()=="CUSTOM":
            gender=a.upper()
            break
        else:
            print("Please Enter Valid Answer")
    while True:
        x=input("Enter Maritial Status(Married/Divorced/Single):")
        if x.upper()=="MARRIED":
            maritial=x.upper()
            break
        elif x.upper()=="DIVORCED":
            maritial=x.upper()
            break
        elif x.upper()=="SINGLE":
            maritial=x.upper()
            break
        else:
            print("Please Enter Valid Answer")
    health=input("Enter Health Details: ")
    dom_torreto=input("Enter Family Details: ")
    address=input("Enter Address: ")
    sal=int(input("Enter Salary: "))
    detl=[name,sv_num,age,gender,health,maritial,dom_torreto, address, sal]
    pickle.dump(detl,f)
    f.close()
    print("Details Entered Successfully!!!!")
    print("\n********************************************************\n")





def persearch():
    f=open("Personel_Details.dat", "rb")
    print("\n********************************************************\n")
    sv_num=(input("Enter Sevice No.: "))
    flag=False
    while True:
        try:
            det=pickle.load(f)
            if sv_num==det[1]:
                print("Service No.: ", det[1])
                print("Name.: ", det[0])
                print("Age: ", det[2])
                print("Gender: ", det[3])
                print("Heath Details: ", det[4])
                print("Marital Status.: ", det[5])
                print("Family Details.: ", det[6])
                print("Address: ", det[7])
                print("Salary: ", det[8],"/-")
                flag=True
        except EOFError:
            break
    if flag==False:
        print("No Record Found") 
    print("\n********************************************************\n")
    f.close()





def perdisplay_all():
    f=open("Personel_Details.dat", "rb")
    while True:
        try:
            det=pickle.load(f)
            print("\n*********************************************\n")
            print("Service No.: ",det[1] )
            print("Name.: ", det[0])
            print("Age: ", det[2])
            print("Gender: ", det[3])
            print("Heath Details: ", det[4])
            print("Marital Status.: ", det[5])
            print("Family Details.: ", det[6])
            print("Address: ", det[7])
            print("Salary: ", det[8],"/-")
            print("\n*********************************************\n")
        except EOFError:
            break
    f.close()





def pernamemodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter New Name: ")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][0]=n
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def peragemodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Name: ")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][2]=n
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def perhealmodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Current Health Status : ")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][4]=n
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def perfammodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Current Family Details: ")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][6]=n
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def peraddmodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Current Address: ")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][7]=n
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def persalmodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Salary: ")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][8]=n
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def permaritialmodify():
    s=input("Enter Sevice No.: ")
    while True:
        n=input("Enter Current Maritial Status (Married/Divorced/Single): ")
        if n.upper()=="MARRIED":
            m=n.upper()
            break
        elif n.upper=="DIVORCED":
            m=n.upper()
            break
        elif n.upper()=="SINGLE":
            m=n.upper()
            break
        else:
            print("Enter Valid answer")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][5]=m
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def pergenmodify():
    s=input("Enter Sevice No.: ")
    while True:
        n=input("Enter Gender (Male/Female/Custom): ")
        if n.upper()=="MALE":
            m=n.upper()
            break
        elif n.upper=="FEMALE":
            m=n.upper()
            break
        elif n.upper()=="CUSTOM":
            m=n.upper()
            break
        else:
            print("Enter Valid answer")
    f=open("Personel_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][1]==s:
            detlist[i][5]=m
    f=open("Personel_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Details of Personnel",s,"has been Updated")





def permodify():
    print("Press 1 to change Name\nPress 2 to change Age\nPress 3 to change Gender\nPress 4 to change Health Status\nPress 5 to change Maritial Status\nPress 6 to change Family Detailts\nPress 7 to change Address\nPress 8 to change Salary")
    n=input("What do you like to Change")
    if n=="1":
        print("\n********************************************************\n")
        pernamemodify()
        print("\n********************************************************\n")
    elif n=="2":
        print("\n********************************************************\n")
        peragemodify()
        print("\n********************************************************\n")
    elif n=="3":
        print("\n********************************************************\n")
        pergenmodify()
        print("\n********************************************************\n")
    elif n=="4":
        print("\n********************************************************\n")
        perhealmodify()
        print("\n********************************************************\n")
    elif n=="5":
        print("\n********************************************************\n")
        permaritialmodify()
        print("\n********************************************************\n")
    elif n=="6":
        print("\n********************************************************\n")
        perfammodify()
        print("\n********************************************************\n")
    elif n=="7":
        print("\n********************************************************\n")
        peraddmodify()
        print("\n********************************************************\n")
    elif n=="8":
        print("\n********************************************************\n")
        persalmodify()
        print("\n********************************************************\n")
    else:
        print("Enter Valid Answer")





def perdeldetails():
    print("\n********************************************************\n")
    r=input("Enter Service No. to delete")
    f=open("Personel_Details.dat", "rb")
    delt=[]
    fin=[]
    pdata=pickle.load(f)
    for i in pdata:
        delt.append(i)
    f.close()
    f=open("Personel_Details.dat", "wb")
    for i in delt:
        if i[0]==r:
            del(i)
        else:
            fin.append(i)
    for x in fin:
        pickle.dump(x,f)
    f.close()
    print("        Details of Personnel", r , "has been deleted      ")
    print("\n********************************************************\n")





def personal_details():
    while True:
        print("\n********************************************************\n")
        print("Enter 1 to Insert Details")
        print("Enter 2 to Display all Details")
        print("Enter 3 to search for Detail")
        print("Enter 4 to Modify Details")
        print("Enter 5 to Delete Details")
        print("Enter 6 to Exit")
        print("\n********************************************************\n")
        ch=input("Enter Choice: ")
        if ch=="1":
            perinsert()
        elif ch=="2":
            perdisplay_all()
        elif ch=="3":
            persearch()
        elif ch=="4":
            permodify()
        elif ch=="5":
            perdeldetails()
        elif ch=="6":
            break
        else:
            print("Enter Valid Answer")





def military_details():
    while True:
        print("\n********************************************************\n")
        print("Enter 1 to Insert Details")
        print("Enter 2 to Display all Details")
        print("Enter 3 to search for Detail")
        print("Enter 4 to Modify Details")
        print("Enter 5 to Delete Details")
        print("Enter 6 to Exit")
        print("\n********************************************************\n")
        ch=input("Enter Choice: ")
        if ch=="1":
            milinsert()
        elif ch=="2":
            mildisplay_all()
        elif ch=="3":
            milsearch()
        elif ch=="4":
            permilmodify()
        elif ch=="5":
            mildeldetails()
        elif ch=="6":
            break
        else:
            print("Enter Valid Answer")





def milinsert():
    print("\n********************************************************\n")
    f=open("Military_Details.dat", "ab")
    sv_num=input("Enter Sevice No.: ")
    desg=input("Enter Personnel Designation: ")
    batt=input("Enter Personnel Battilion: ")
    squad=input("Enter Personnel Squad: ")
    rank=input("Enter Personnel Rank: ")
    posting=input("Enter the Place where Personnel is Posted: ")
    b=int(input("Enter No. of Accessories Provided (If None Enter '0'): "))
    acc=[]
    for i in range(b):
        if b>0:
            ass=input("Enter Accesory: ")
            acc.append(ass.upper())
        elif b==0:
            acc="Nil"
            break
        else:
            print("Enter Valid Answer")
    a=int(input("Enter No. of Awards Recieved (If None Enter '0'): "))
    award=[]
    for i in range(a):
        if a>0:
            aw=input("Enter Award: ")
            award.append(aw.upper())
        elif a==0:
            break
        else:
            print("Enter Valid Answer")
    while True:
        s=input("Enter Current Life Status (Alive / Martyred / Voluntarily Retired / Retired by Force): ")
        if s.upper()=="ALIVE":
            stat=s.upper()
            break
        elif s.upper()=="MARTYRED":
            stat=s.upper()
            print("May his/her Soul Rest in Peace")
            break
        elif s.upper()=="VOLUNTARILY RETIRED":
            stat=s.upper()
            break
        elif s.upper()=="RETIRED BY FORCE":
            stat=s.upper()
            break
        else:
            print("Please Enter Valid Answer")
    while True:
        u=input("Enter Personnel Force (Air Force / Navy / Army): ")
        if u.upper()==" AIR FORCE":
            force=u.upper()
            break
        elif u.upper()=="NAVY":
            force=u.upper()
            break
        elif u.upper()=="ARMY":
            force=u.upper()
            break
        else:
            print("Please Enter Valid Answer")
    mildetl=[sv_num,desg,batt,squad,rank,posting,acc,award,stat,force]
    pickle.dump(mildetl,f)
    f.close()
    print("Details Entered Successfully!!!!")
    print("\n********************************************************\n")





def mildisplay_all():
    f=open("Military_Details.dat", "rb")
    while True:
        try:
            det=pickle.load(f)
            print("\n*********************************************\n")
            print("Service No.: ",det[0] )
            print("Designation: ", det[1])
            print("Battalion: ", det[2])
            print("Squad: ", det[3])
            print("Rank: ", det[4])
            print("Posting: ", det[5])
            print("Accesories Provided: ")
            for x in range (len(det[6])):
                print(x+1,'.',det[6][x])
            print("Awards: ")
            for i in range (len(det[7])):
                print(i+1,'.',det[7][i])
            print("Current Status: ", det[8])
            print("Force: ", det[9])
            print("\n*********************************************\n")
        except EOFError:
            break
    f.close()





def mildeldetails():
    print("\n********************************************************\n")
    r=input("Enter Vehicle ID to delete")
    f=open("Military_Details.dat", "rb")
    lst=[]
    search=[]
    while True:
        try:
            mdata=pickle.load(f)
            search.append(mdata)
        except EOFError:
            break
    f.close()
    for i in search:
        if i[0]==r:
            del(i)
        else:
            lst.append(i)
    f=open("Military_Details.dat", "wb")
    for x in lst:
        pickle.dump(x,f)  
    f.close()
    print("Details of Personnel", r , "has been deleted")
    print("\n********************************************************\n")





def milsearch():
    f=open("Military_Details.dat", "rb")
    sv_num=(input("Enter Sevice No.: "))
    flag=False
    while True:
        try:
            det=pickle.load(f)
            if sv_num==det[0]:
                print("\n********************************************************\n")
                print("Service No.: ",det[0] )
                print("Designation: ", det[1])
                print("Battalion: ", det[2])
                print("Squad: ", det[3])
                print("Rank: ", det[4])
                print("Posting: ", det[5])
                print("Accesories Provided: ")
                for x in range (len(det[6])):
                    print(x+1,'.',det[6][x])
                print("Awards: ")
                for i in range (len(det[7])):
                    print(i+1,'.',det[7][i])
                print("Current Status: ", det[8])
                print("Force: ", det[9])
                print("\n********************************************************\n")
                flag=True
        except EOFError:
            break
    if flag== False:
        print("No Record Found")
    f.close()





def mildesgmodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter New Designation: ")
    f=open("Military_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][0]==s:
            detlist[i][1]=n
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def milbattmodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Persennel New Battalion: ")
    f=open("Military_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][0]==s:
            detlist[i][2]=n
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def milsquadmodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Persennel New Squad: ")
    f=open("Military_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][0]==s:
            detlist[i][3]=n
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def milrankmodify():
    s=input("Enter Sevice No.: ")
    t=input("Promoted or Demoted")
    n=input("Enter Persennel",t," Rank: ")
    f=open("Military_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][0]==s:
            detlist[i][4]=n
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def milpostmodify():
    s=input("Enter Sevice No.: ")
    n=input("Enter Persennel New Posting Area: ")
    f=open("Military_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][0]==s:
            detlist[i][5]=n
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def milaccmodify():
    s=input("Enter Sevice No.: ")
    y=int(input("Press 1 If Accessorries were given\nPress 2 If Accessorries were taken\nPress 0 To go Back"))
    while True:
        try:
            if y==1:
                b=int(input("Enter No. of New Accessories Provided (If None Enter '0'): "))
                acc=[]
                for i in range(b):
                    if b>0:
                        ass=input("Enter New Accesory: ")
                        acc.append(ass.upper())
                    elif b==0:
                        break
                    else:
                        print("Enter Valid Answer")
                f=open("Military_Details.dat", "rb")
                detlist=[]
                while True:
                    try:
                        det=pickle.load(f)
                        detlist.append(det)
                    except EOFError:
                        break
                f.close()   
                for i in range(len(detlist)):
                    if detlist[i][0]==s:
                        detlist[i][6]=detlist[i][6]+acc
                break
            elif y==2:
                b=int(input("Enter No. of New Accessories Provided (If None Enter '0'): "))
                acc=[]
                for i in range(b):
                    if b>0:
                        ass=input("Enter New Accesory: ")
                        acc.append(ass.upper())
                    elif b==0:
                        break
                    else:
                        print("Enter Valid Answer")
                f=open("Military_Details.dat", "rb")
                detlist=[]
                while True:
                    try:
                        det=pickle.load(f)                  
                        detlist.append(det)
                    except EOFError:
                        break             
                f.close()
                acc3=[]                              
                for i in range(len(detlist)):
                    acc2=detlist[i][6]
                    if detlist[i][0]==s:
                        for x in range(len(acc2)):
                            for p in range(len(acc)):
                                if acc2[x]==acc[p]:
                                    del(acc2[x])
                        detlist[i][6]=acc2
                break
            elif y==0:
                break
        except EOFError:
            break
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def millifestatmodify():
    t=input("Enter Sevice No.: ")
    while True:
        s=input("Enter NCurrent Life Status (Alive / Martyred / Voluntarily Retired / Retired by Force): ")
        if s.upper()=="ALIVE":
            stat=s.upper()
            break
        elif s.upper()=="MARTYRED":
            stat=s.upper()
            print("May his/her Soul Rest in Peace")
            break
        elif s.upper()=="VOLUNTARILY RETIRED":
            stat=s.upper()
            break
        elif s.upper()=="RETIRED BY FORCE":
            stat=s.upper()
            break
        else:
            print("Please Enter Valid Answer")
    f=open("Military_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][0]==t:
            detlist[i][8]=stat
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",t,"has been Updated")





def milforcemodify():
    s=input("Enter Sevice No.: ")
    while True:
        u=input("Enter Personnel Force (Air Force / Navy / Army): ")
        if u.upper()==" AIR FORCE":
            force=u.upper()
            break
        elif u.upper()=="NAVY":
            force=u.upper()
            break
        elif u.upper()=="ARMY":
            force=u.upper()
            break
        else:
            print("Please Enter Valid Answer")
    f=open("Military_Details.dat", "rb")
    detlist=[]
    while True:
        try:
            det=pickle.load(f)
            detlist.append(det)
        except EOFError:
            break
    f.close()
    for i in range(len(detlist)):
        if detlist[i][0]==s:
            detlist[i][9]=force
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def permilmodify():
    print("\n************************************************************************\n")
    print("Press 1 to change Personnel Designation\nPress 2 to change Personnel Battalion\nPress 3 to change Personnel Squad\nPress 4 to change Personnel Rank\nPress 5 to change Personnel Posting Area\nPress 6 to change Personnel Accesdories\nPress 7 to change Personnel Awards\nPress 8 to Enter Personnel Current Life Status\nPress 9 to Change Personnel Force")
    print("\n************************************************************************\n")
    n=input("What do you like to Change? ")
    print("\n************************************************************************\n")
    if n=="1":
        print("\n********************************************************\n")
        mildesgmodify()
        print("\n********************************************************\n")
    elif n=="2":
        print("\n********************************************************\n")
        milbattmodify()
        print("\n********************************************************\n")
    elif n=="3":
        print("\n********************************************************\n")
        milsquadmodify()
        print("\n********************************************************\n")
    elif n=="4":
        print("\n********************************************************\n")
        milrankmodify()
        print("\n********************************************************\n")
    elif n=="5":
        print("\n********************************************************\n")
        milpostmodify()
        print("\n********************************************************\n")
    elif n=="6":
        print("\n********************************************************\n")
        milaccmodify()
        print("\n********************************************************\n")
    elif n=="7":
        print("\n********************************************************\n")
        milawardmodify()
        print("\n********************************************************\n")
    elif n=="8":
        print("\n********************************************************\n")
        millifestatmodify()
        print("\n********************************************************\n")
    elif n=="9":
        print("\n********************************************************\n")
        milforcemodify()
        print("\n********************************************************\n")
    else:
        print("Enter Valid Answer")





def milawardmodify():
    s=input("Enter Sevice No.: ")
    print("Press 1 to add new Awards\nPress 0 to go back")
    y=int(input("Enter Your Choice: "))
    while True:
        try:
            if y==1:
                b=int(input("Enter No. of New Awards (If None Enter '0'): "))
                awa=[]
                for i in range(b):
                    if b>0:
                        ass=input("Enter New Award: ")
                        awa.append(ass.upper())
                    elif b==0:
                        break
                    else:
                        print("Enter Valid Answer")
                f=open("Military_Details.dat", "rb")
                detlist=[]
                while True:
                    try:
                        det=pickle.load(f)
                        detlist.append(det)
                    except EOFError:
                        break
                f.close()   
                awa2=detlist[i][7]
                for i in range(len(detlist)):
                    if detlist[i][0]==s:
                        detlist[i][7]=awa2+awa
                break
            elif y==0:
                break
        except EOFError:
            break
    f=open("Military_Details.dat", "wb")
    for x in detlist:
        pickle.dump(x,f)
    f.close()
    print("Military Details of Personnel",s,"has been Updated")





def PersonnelDetails():
    while True:
        print("\n********************************************************\n")
        print("Press 1 to Access Personnel Personal Details\nPress 2 to Access Personnel Military Details\nPress 0 to Go Back")
        print("\n********************************************************\n")
        ch=input("What Would You Like To Do? ")
        print("\n********************************************************\n")
        if ch=="1":
            personal_details()
        elif ch=="2":
            military_details()
        elif ch=="0":
            break
        else:
            print("Enter Valid Anwser")





def MotorcadeDetails():
    while True:
        print("To enter new details press a\nTo change old details press b\nTo display all data press c\nTo search press d\nTo delete details press e\nTo return to Main Menu press z")
        print("***************************************************************************************")
        choice=input("What would you like to do")
        print("***************************************************************************************")
        if choice.lower()=="a":
            addingmdetails()
        elif choice.lower()=="b":
            changingmdetails()
        elif choice.lower()=="c":
            displaymdetails()
        elif choice.lower()=="d":
            searchmdetails()
        elif choice.lower()=="e":
            deletemdetails()
        elif choice.lower()=="z":
            break
        else:
            print("Enter Valid Operation")
            print("***************************************************************************************")





def addingmdetails():
    details=[]
    while True:
        vehicle_ID=input("Enter Vehicle ID")
        vehicle_name=input("Enter Vehicle Name")
        vehicle_type=input("Enter the purpose vehicle is used for")
        vehicle_class=input("Enter Vehicle class")
        vehicle_units=input("Enter the number of similar units available")
        vehicle_fuel=input("Enter type of fuel required")
        ans=input("Enter the ammunition compatible (IF ANY else enter NIL)")
        if ans.upper()=="NIL":
            vehicle_ammo=ans.upper()
        else:
            vehicle_ammo=ans
        while True:
            ans=input("Enter vehicle's current status (Commisioned/Decommisioned/Maintainence)")
            if ans.upper()=="COMMISIONED":
                vehicle_status=ans.upper()
                break
            elif ans.upper()=="DECOMMISIONED":
                vehicle_status=ans.upper()
                break
            elif ans.upper()=="MAINTAINENCE":
                vehicle_status=ans.upper()
                break
            else:
                print("Enter Valid answer")
        vehicle_cost=input("Enter the cost")
        while True:
            ans=input("Enter vehicle's current affiliation (Army/ Navy/ Air Force)")
            if ans.upper()=="ARMY":
                vehicle_affiliation=ans.upper()
                break
            elif ans.upper()=="NAVY":
                vehicle_affiliation=ans.upper()
                break
            elif ans.upper()=="AIR FORCE":
                vehicle_affiliation=ans.upper()
                break
            else:
                print("Enter Valid answer")

        add=[vehicle_ID,vehicle_name,vehicle_type,vehicle_class,vehicle_units,vehicle_fuel,vehicle_ammo,vehicle_status,vehicle_cost,vehicle_affiliation]
        details.append(add)
        opt=input("Do want to add more? If 'Yes' press any key else enter 'No'")
        if opt.lower()=="no":
            break
        else:
            print("***************************************************************************************")
    print("***************************************************************************************")
    f=open("Military Details.dat", "wb")
    pickle.dump(details,f)
    print("Data has been added")
    f.close()





def changingmdetails():
    while True:
        print("To change:\nName press a\nType press b\nClass press c\nUnit count press d\nFuel Type press e\nCompatible Ammunition press f\nStatus press g\nCost press h\nAffiliation press i\nTo exit press j\n")
        option=input()
        if option.upper()=="A":
            changingmdetailsname()
            print("***************************************************************************************")
            break
        elif option.upper()=="B":
            changingmdetailstype()
            print("***************************************************************************************")
            break
        elif option.upper()=="C":
            changingmdetailsclass()
            break
        elif option.upper()=="D":
            changingmdetailsunits()
            print("***************************************************************************************")
            break
        elif option.upper()=="E":
            changingmdetailsfuel()
            print("***************************************************************************************")
            break
        elif option.upper()=="F":
            changingmdetailsammo()
            print("***************************************************************************************")
            break
        elif option.upper()=="G":
            changingmdetailsstatus()
            print("***************************************************************************************")
            break
        elif option.upper()=="H":
            changingmdetailscost()
            print("***************************************************************************************")
            break
        elif option.upper()=="I":
            changingmdetailsaffl()
            print("***************************************************************************************")
            break
        elif option.upper()=="J":
            break
        else:
            print("Enter Valid Operation")
            print("***************************************************************************************")






def changingmdetailsname():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    new=input("Enter new name")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[1]=(i[1].replace(i[1],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")





def changingmdetailstype():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    new=input("Enter current type")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[2]=(i[2].replace(i[2],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")



def changingmdetailsclass():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    new=input("Enter current class")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[3]=(i[3].replace(i[3],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")





def changingmdetailsunits():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    new=input("Enter current units")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[4]=(i[4].replace(i[4],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")




def changingmdetailsfuel():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    new=input("Enter current fuel requirement")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[5]=(i[5].replace(i[5],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")





def changingmdetailsammo():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    ans=input("Enter new Ammunition details")
    if ans.upper()=="NIL":
        ans=ans.upper()
    else:
        new=ans
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[6]=(i[6].replace(i[6],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")





def changingmdetailsstatus():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    while True:
        ans=input("Enter current status")
        if ans.upper()=="COMMISIONED":
            new=ans.upper()
            break
        elif ans.upper()=="DECOMMISIONED":
            new=ans.upper()
            break
        elif ans.upper()=="MAINTAINENCE":
            new=ans.upper()
            break
        else:
            print("Enter Valid answer")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[7]=(i[7].replace(i[7],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")






def changingmdetailscost():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    new=input("Enter new cost")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[8]=(i[8].replace(i[8],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")





def changingmdetailsaffl():
    f=open("Military Details.dat", "rb")
    change_ID=input("Enter the Vehicle ID to be updated")
    while True:
            ans=input("Enter vehicle's current affiliation (Army/ Navy/ Air Force)")
            if ans.upper()=="ARMY":
                new=ans.upper()
                break
            elif ans.upper()=="NAVY":
                new=ans.upper()
                break
            elif ans.upper()=="AIR FORCE":
                new=ans.upper()
                break
            else:
                print("Enter Valid answer")
    uplst=[]
    mdata=pickle.load(f)
    for j in mdata:
        uplst.append(j)
    f.close()
    for i in uplst:
        if i[0]==change_ID:
            i[9]=(i[9].replace(i[9],new))
    f=open("Military Details.dat","wb")
    pickle.dump(uplst,f)
    f.close()
    print("Details have been updated")






def displaymdetails():
    f=open("Military Details.dat", "rb")
    while True:
        try:
            display=pickle.load(f)
            print(display)
        except EOFError:
            break
    f.close()
    print("***************************************************************************************")





def searchmdetails():
    search=input("Enter the Vehicle ID you want to search")
    f=open("Military Details.dat", "rb")
    flag=False
    while True:
        try:
            data=pickle.load(f)
            for i in data:
                if i[0]==search:
                    print("The details of Vehicle", search, "are", i)
                    flag=True
        except EOFError:
            break
    if flag==False:
        print("No records found for Vehicle", search)
    f.close()
    print("***************************************************************************************")


                


def deletemdetails():
    r=input("Enter Vehicle ID to delete")
    f=open("Military Details.dat", "rb")
    search=[]
    lst=[]
    mdata=pickle.load(f)
    for i in mdata:
        search.append(i)
    f.close()
    f=open("Military Details.dat", "wb")
    for i in search:
        if i[0]==r:
            del(i)
        else:
            lst.append(i)
    pickle.dump(lst,f)
    f.close()
    print("Details of Vehicle", r , "has been deleted")
    print("***************************************************************************************")





def ammo_insert():
    print("\n********************************************************\n")
    Ammo_ID=input('Enter Ammunition ID: ')
    Ammo_name=input("Enter Ammunition Name: ")
    Ammo_compatible=input("Enter Compatible Weapon/Vehicle: ")
    Ammo_range=0
    while True:
        Ammo_range0=input("Enter Ammunition Rangefrom 1 to 10: ")
        if Ammo_range0.isdigit() and int(Ammo_range0)<=10:
            Ammo_range=int(Ammo_range0)
            break
        else:
            print('Enter Valid Input')
    Ammo_capacity=0
    while True:
        Ammo_capacity0=input("Enter Ammunition Destructive Capacity from 1 to 10: ")
        if Ammo_capacity0.isdigit() and int(Ammo_capacity0)<=10:
            Ammo_capacity=int(Ammo_capacity0)
            break
        else:
            print('Enter Valid Input')
    Ammo_force=''
    while True:
        Ammo_force0=input("Enter Force Affilated (Air Force / Navy / Army): ")
        if Ammo_force0.upper()=="ARMY":
            Ammo_force="ARMY"
            break
        elif Ammo_force0.upper()=="NAVY":
            Ammo_force="NAVY"
            break
        elif Ammo_force0.upper()=="AIR FORCE":
            Ammo_force="AIR FORCE"
            break
        else:
            print('Enter a Valid Answer.')
    Ammo_class=input("Enter Ammunition class: ")
    Ammo_stock=input("Enter stock of Ammunition available:")
    Ammo_cost=input("Enter the cost: ")
    detl=[Ammo_ID,Ammo_name,Ammo_compatible,Ammo_range,Ammo_capacity,Ammo_force,Ammo_class,Ammo_stock,Ammo_cost]
    fields=['Ammunition ID','Name','Weapon/Vehicle','Range','Capacity','Affilated Force','Class','Stock','Cost']
    ans=input('Is there an Existing File?\n1 for yes\n0 for no\n')
    csv_row=[]
    while True:
        if ans=='0':
            x=open('Ammunition_Details.csv','w')
            csv_x=csv.writer(x)
            csv_x.writerow(fields)
            x.close()
            break
        elif ans=='1':
            break
        else:
            print('Enter valid Answer')
    csv_row.append(detl)
    with open('Ammunition_Details.csv','a', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(csv_row)
    f.close()
    print("\nDetails Entered Successfully!!!!")
    print("\n********************************************************\n")





def ammo_displayall():
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    for i in csv_r:
        if csv_r.line_num == 1:
            continue
        else:
            row.append(i)
    for det in row:
        print("\n*********************************************\n")
        print("Ammunition ID: ",det[0] )
        print("Ammunition Name: ",det[1] )
        print("Compatible Weapon/Vehicle.: ", det[2])
        print("Range: ", det[3])
        print("Destructive Capacity: ", det[4])
        print("Force Affiliated: ", det[5])
        print("Class: ", det[6])
        print("Stock: ", det[7])
        print("Cost: ", det[8],"/-")
        print("\n*********************************************\n")
    f.close()





def ammo_search():
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    Ammo_ID=(input("Enter Ammunition ID to search: "))
    for i in csv_r:
        if csv_r.line_num == 1:
            continue
        else:
            row.append(i)
    for det in row:
        if det[0]==Ammo_ID:
            print("\n*********************************************\n")
            print("Ammunition ID: ",det[0] )
            print("Ammunition Name: ",det[1] )
            print("Compatible Weapon/Vehicle.: ", det[2])
            print("Range: ", det[3])
            print("Destructive Capacity: ", det[4])
            print("Force Affiliated: ", det[5])
            print("Class: ", det[6])
            print("Stock: ", det[7])
            print("Cost: ", det[8],"/-")
            print("\n*********************************************\n")
    f.close()





def ammo_namemodify():
    s=input("Enter Ammunition ID: ")
    n=input("Enter New Name: ")
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[1]=n
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_weaponmodify():
    s=input("Enter Ammunition ID: ")
    n=input("Enter New Compatible Weapon: ")
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[2]=n
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_rangemodify():
    s=input("Enter Ammunition ID: ")
    print("\n************************************************************************\n")
    while True:
        Ammo_range0=input("Enter Ammunition Range from 1 to 10: ")
        if Ammo_range0.isdigit() and int(Ammo_range0)<=10:
            Ammo_range=int(Ammo_range0)
            break
        else:
            print('Enter Valid Input')
            print("\n************************************************************************\n")
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[3]=Ammo_range
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_capacitymodify():
    s=input("Enter Ammunition ID: ")
    print("\n************************************************************************\n")
    while True:
        Ammo_cap0=input("Enter Ammunition Destructive Capacity from 1 to 10: ")
        if Ammo_cap0.isdigit() and int(Ammo_cap0)<=10:
            Ammo_cap=int(Ammo_cap0)
            break
        else:
            print('Enter Valid Input')
            print("\n************************************************************************\n")
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[4]=Ammo_cap
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_forcemodify():
    s=input("Enter Ammunition ID: ")
    print("\n************************************************************************\n")
    while True:
        u=input("Enter Affilated Force (Air Force / Navy / Army): ")
        if u.upper()=="AIR FORCE":
            force=u.upper()
            break
        elif u.upper()=="NAVY":
            force=u.upper()
            break
        elif u.upper()=="ARMY":
            force=u.upper()
            break
        else:
            print("Please Enter Valid Answer")
            print("\n************************************************************************\n")
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[5]=force
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_classmodify():
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    s=input("Enter Ammunition ID: ")
    n=input("Enter New Class: ")
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[6]=n
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_stockmodify():
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    s=input("Enter Ammunition ID: ")
    n=input("Enter New Stock: ")
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[7]=n
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_costmodify():
    f=open('Ammunition_Details.csv','r')
    csv_r=csv.reader(f)
    row=[]
    s=input("Enter Ammunition ID: ")
    n=input("Enter New Cost: ")
    for i in csv_r:
        row.append(i)
    for det in row:
        if det[0]==s:
            det[8]=n
    f.close()
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(row)
    f.close()
    print("Ammunition Details of ",s,"has been Updated")





def ammo_modify():
    while True:
        print("\n************************************************************************\n")
        print("Press 1 to change Ammunition Name\nPress 2 to change Ammunition Compatible Weapon/Vehicle\nPress 3 to change Ammunition Range From 1 to 10\nPress 4 to change Ammunition Destructive Capacity from 1 to 10\nPress 5 to change Ammunition Affilated Force\nPress 6 to change Ammunition Class\nPress 7 to change Ammunition Stock\nPress 8 to change Ammunition Cost\nPress 0 to go back")
        print("\n************************************************************************\n")
        n=input("What do you like to Change? ")
        print("\n************************************************************************\n")
        if n=="1":
            print("\n********************************************************\n")
            ammo_namemodify()
            break
            print("\n********************************************************\n")
        elif n=="2":
            print("\n********************************************************\n")
            ammo_weaponmodify()
            break
            print("\n********************************************************\n")
        elif n=="3":
            print("\n********************************************************\n")
            ammo_rangemodify()
            print("\n********************************************************\n")
            break
        elif n=="4":
            print("\n********************************************************\n")
            ammo_capacitymodify()
            print("\n********************************************************\n")
            break
        elif n=="5":
            print("\n********************************************************\n")
            ammo_forcemodify()
            print("\n********************************************************\n")
            break
        elif n=="6":
            print("\n********************************************************\n")
            ammo_classmodify()
            print("\n********************************************************\n")
            break
        elif n=="7":
            print("\n********************************************************\n")
            ammo_stockmodify()
            print("\n********************************************************\n")
            break
        elif n=="8":
            print("\n********************************************************\n")
            ammo_costmodify()
            print("\n********************************************************\n")
            break
        elif n=="0":
            break
        else:
            print("Enter Valid Answer")





def ammo_deldetails():
    print("\n********************************************************\n")
    r=input("Enter Ammunition ID to delete: ")
    f=open('Ammunition_Details.csv','r')
    lst=[]
    search=[]
    csv_r=csv.reader(f)
    for i in csv_r:
        search.append(i)
    f.close()
    print(search)
    for x in search:
        if x[0]==r:
            del(x)
        else:
            lst.append(x)
    print(lst)
    with open('Ammunition_Details.csv','w', newline='') as f:
        csv_f=csv.writer(f)
        csv_f.writerows(lst)
    f.close()
    print("Ammunition Details of ",r,"has been Deleted")





def AmmunationDetails():
    while True:
        print("\n********************************************************\n")
        print("Enter 1 to Insert Details")
        print("Enter 2 to Display all Details")
        print("Enter 3 to search for Detail")
        print("Enter 4 to Modify Details")
        print("Enter 5 to Delete Details")
        print("Enter 0 to Exit")
        print("\n********************************************************\n")
        ch=input("Enter Choice: ")
        if ch=="1":
            print("\n************************************************************************\n")
            ammo_insert()
            print("\n************************************************************************\n")
        elif ch=="2":
            print("\n************************************************************************\n")
            ammo_displayall()
            print("\n************************************************************************\n")
        elif ch=="3":
            print("\n************************************************************************\n")
            ammo_search()
            print("\n************************************************************************\n")
        elif ch=="4":
            print("\n************************************************************************\n")
            ammo_modify()
            print("\n************************************************************************\n")
        elif ch=="5":
            print("\n************************************************************************\n")
            ammo_deldetails()
            print("\n************************************************************************\n")
        elif ch=="0":
            break
        else:
            print("Enter Valid Answer")




'''
connect=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="weapons"
)
cursor=connect.cursor()
#cursor.execute('create database weapons')
#cursor.execute('create table Weapon_Details(Weapon_ID varchar(10),Weapon_Name varchar(50),Cost float,Type varchar(10),Current_Owner varchar(100),Units integer)')

'''



def WeaponDetails():
    while True:
        print('To add new records press a')
        print('To change old records press b')
        print('To display all records all press c')
        print('To search records press d')
        print('To delete records press e')
        print('To return to Main Menu press z')
        print("***************************************************************************************")
        choice=input('Enter your desired command')
        print("***************************************************************************************")
        if choice.lower()=='a':
            addwdetails()
        elif choice.lower()=='b':
            changewdetails()
        elif choice.lower()=='c':
            displaywdetails()
        elif choice.lower()=='d':
            searchwdetails()
        elif choice.lower()=='e':
            deletewdetails()
        elif choice.lower()=='z':
            break
        else:
            print("Enter Valid Operation")
            print("***************************************************************************************")





def addwdetails():
    while True:
        name=input('Enter the weapon name')
        name=name.upper()
        Id=input('Enter the weapon ID')
        cost=input('Enter the cost of the weapon')
        while True:
            Type=input('Enter the weapon type.(Mountable/handheld/installed)')
            if Type.lower()=='mountable':
                Type='MOUNTABLE'
                break
            elif Type.lower()=='handheld':
                Type='HANDHELD'
                break
            elif Type.lower()=='installed':
                Type='INSTALLED'
                break
            else:
                print('Enter valid Weapon type')
        owner=input('Enter the name of the current possessor')
        owner=owner.upper()
        unit=input('Enter the number of units currently available')
        query=('insert into Weapon_details(weapon_name,weapon_id,cost,type,current_owner,units) values(%s,%s,%s,%s,%s,%s)')
        values=(name,Id,cost,Type,owner,unit)
        cursor.execute(query,values)
        connect.commit()
        answer=input('Do you wish to enter more records? press "no" for no')
        if answer.lower()=='no':
            print('***************************************************************************************')
            break
        else:
            print('***************************************************************************************')




def changewdetails():
    while True:
        print('Press 1 to update Weapon name')
        print('Press 2 to update cost of weapon')
        print('Press 3 to update the Weapon type')
        print('Press 4 to update the Weapon owner')
        print('Press 5 to update the number of units available')
        print('***************************************************************************************')
        answer=input('Enter the value you wish to update')
        print('***************************************************************************************')
        if answer.lower()=='1':
            updatewname()
            break
        elif answer.lower=='2':
            updatewcost()
            break
        elif answer.lower()=='3':
            updatewtype()
            break
        elif answer.lower()=='4':
            updatewowner()
            break
        elif answer.lower=='5':
            updatewunits()
            break
        else:
            print('Enter valid option')




def updatewname():
    value=input('Enter the weapon ID of which you wish to update')
    new=input('Enter the new name of the weapon')
    new=new.upper()
    print('***************************************************************************************')
    query='update weapon_details set weapon_name=%s where weapon_id=%s'
    val=(new,value)
    cursor.execute(query,val)
    connect.commit()
    print('Data has been updated')
    print('***************************************************************************************')






def updatewcost():
    value=input('Enter the weapon ID of which you wish to update')
    new=input('Enter the new cost of the weapon')
    print('***************************************************************************************')
    query='update weapon_details set cost=%s where weapon_id=%s'
    val=(new,value)
    cursor.execute(query,val)
    connect.commit()
    print('Data has been updated')
    print('***************************************************************************************')





def updatewtype():
    value=input('Enter the weapon ID of which you wish to update')
    new=input('Enter the new Type of the weapon')
    new=new.upper()
    print('***************************************************************************************')
    query='update weapon_details set type=%s where weapon_id=%s'
    val=(new,value)
    cursor.execute(query,val)
    connect.commit()
    print('Data has been updated')
    print('***************************************************************************************')




def updatewowner():
    value=input('Enter the weapon ID of which you wish to update')
    new=input('Enter the new Owner of the weapon')
    new=new.upper()
    print('***************************************************************************************')
    query='update weapon_details set current_owner=%s where weapon_id=%s'
    val=(new,value)
    cursor.execute(query,val)
    connect.commit()
    print('Data has been updated')
    print('***************************************************************************************')




def updatewunits():
    value=input('Enter the weapon ID of which you wish to update')
    new=input('Enter the new number of units of the weapon')
    new=new.upper()
    print('***************************************************************************************')
    query='update weapon_details set units=%s where weapon_id=%s'
    val=(new,value)
    cursor.execute(query,val)
    connect.commit()
    print('Data has been updated')
    print('***************************************************************************************')





def deletewdetails():
    value=input('Enter the weapon ID of which you wish to delete')
    print('***************************************************************************************')
    query='delete from weapon_details where weapon_id=%s'
    val=(value,)
    cursor.execute(query,val)
    connect.commit()
    print('Record has been deleted')
    print('***************************************************************************************')




def searchwdetails():
    value=input('Enter the weapon ID of which you wish to search')
    print('***************************************************************************************')
    query='select * from weapon_details where weapon_id=%s'
    val=(value,)
    cursor.execute(query,val)
    data=cursor.fetchone()
    print(data)
    print('***************************************************************************************')
    




def displaywdetails():
    print('***************************************************************************************')
    cursor.execute('select * from weapon_details')
    data=cursor.fetchall()
    for i in data:
        print(i,'\n')














while True:
    print("***************************************************************************************")
    print("1) To deal with Personnel details press 1\n2) To deal with weapons press 2\n3) To deal with motorcade details press 3\n4)To deal with ammunation details press 4\nTo exit press 0")
    print("***************************************************************************************")
    action=input("What do you want to do")
    if action=="1":
        print("***************************************************************************************")
        PersonnelDetails()
    elif action=="2":
        print("***************************************************************************************")
        WeaponDetails()
    elif action=="3":
        print("***************************************************************************************")
        MotorcadeDetails()
    elif action=="4":
        print("***************************************************************************************")
        AmmunationDetails()
    elif action=="0":
        print("***************************************************************************************")
        print('###################')
        print("Bye!!!")
        print('###################')
        break
    else:
        print("Enter Valid Operation")
