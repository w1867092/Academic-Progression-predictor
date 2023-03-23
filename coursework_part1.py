Progress_count = 0
module_trailer_count = 0
module_retriever_count = 0
Exclude_count = 0

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
            print("Progress")
            print("")
            
        elif pass_mark == 100 and 0 <=defer_mark<=20  and  0 <=fail_mark<=20:
            module_trailer_count += 1
            print("Progress (module trailer)")
            print("")

        elif 0<=pass_mark<= 80 and 0 <= defer_mark<=120 and 0<=fail_mark<=60:
            module_retriever_count += 1
            print("Do not Progress – module retriever")
            print("")

        elif 0<=pass_mark<= 40 and 0 <= defer_mark<=20 and 0<=fail_mark<=100:
            Exclude_count += 1
            print("Exclude")
            print("")
 
        user_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        print("")
        if user_input == "q":
            break
    except ValueError:
        print("Integer required")
        print("")

print("---------------------------------------------------------------")

print("Horizontal Histogram")
print("Progress      :","*" * Progress_count)
print("Trailer          :","*" * module_trailer_count)
print("Retriever     :","*" * module_retriever_count)
print("Excluded     :","*" * Exclude_count)
print("")
total=(Progress_count+module_trailer_count+module_retriever_count+Exclude_count) 
print(total,'outcomes in total')
print("---------------------------------------------------------------")








































