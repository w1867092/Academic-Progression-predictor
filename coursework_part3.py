Progress_count = 0
module_trailer_count = 0
module_retriever_count = 0
Exclude_count = 0

ProgressArr=[]
module_trailerArr=[]
module_retrieverArr=[]
ExcludeArr=[]

while True:
    try:
        while True:
            pass_mark = int(input("Please enter your credits at pass:"))
            if pass_mark not in range(0,121,20):
                print("Out  of range")
                print("")
            else:
                break
            
        while True:
            defer_mark = int(input("Please enter your credits at defer:"))
            if defer_mark not in range(0,121,20):
                print("Out  of range")
                print("")
            else:
                break
            
        while True:         
            fail_mark = int(input("Please enter your credits at fail:"))
            if fail_mark not in range(0,121,20):
                print("Out  of range")
                print("")
            else:
                break

        sum = pass_mark + defer_mark + fail_mark
        if sum != 120:
            print("Total incorrect")
            print("")
            
        elif pass_mark == 120:
            Progress_count += 1
            ProgressArr.append(str(pass_mark) + "," + str(defer_mark) + "," + str(fail_mark))
            print("Progress")
            print("")
            
        elif pass_mark == 100 and 0 <=defer_mark<=20  and  0 <=fail_mark<=20:
            module_trailer_count += 1
            module_trailerArr.append(str(pass_mark) + "," + str(defer_mark) + "," + str(fail_mark))
            print("Progress (module trailer)")
            print("")

        elif 0<=pass_mark<= 80 and 0 <= defer_mark<=120 and 0<=fail_mark<=60:
            module_retriever_count += 1
            module_retrieverArr.append(str(pass_mark) + "," + str(defer_mark) + "," + str(fail_mark))
            print("Do not Progress – module retriever")
            print("")

        elif 0<=pass_mark<= 40 and 0 <= defer_mark<=20 and 0<=fail_mark<=100:
            Exclude_count += 1
            ExcludeArr.append(str(pass_mark) + "," + str(defer_mark) + "," + str(fail_mark))
            print("Exclude")
            print("")
 
        user_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        print("")
        if user_input == "q":
            break
    except ValueError:
        print("Integer required")
        print("")

print("")        

for x in ProgressArr:
    print('Progress                              :- ',x)

for x in module_trailerArr:
    print('Progress (module trailer) :- ',x)
            
for x in module_retrieverArr:
    print('Module retriever                :- ',x)
            
for x in ExcludeArr:
    print('Exclude                                 :- ',x)



print("---------------------------------------------------------------")









































        

