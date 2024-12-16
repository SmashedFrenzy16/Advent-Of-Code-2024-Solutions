with open("i.txt") as file:

    inp = file.read()


num_safe = 0
safe = 0
increasing = False
decreasing = False

for line in inp.split("\n"):

    num_safe = 0

    increasing = False
    decreasing = False
    
    temp_arr = [val for val in line.split()]

    for i in temp_arr:

        if i == " " or i == "\n":

            temp_arr.remove(i)

    for i in range(len(temp_arr) - 1):

        if int(temp_arr[i]) < int(temp_arr[i + 1]):

            if (int(temp_arr[i + 1]) - int(temp_arr[i])) >= 1 and (int(temp_arr[i + 1]) - int(temp_arr[i])) <= 3:

                num_safe += 1

                increasing = True

                print(num_safe)
        
        elif int(temp_arr[i + 1]) < int(temp_arr[i]):

            if (int(temp_arr[i]) - int(temp_arr[i + 1])) >= 1 and (int(temp_arr[i]) - int(temp_arr[i + 1])) <= 3:

                num_safe += 1

                decreasing = True

                print(num_safe)
        
        if increasing == True and decreasing == False:

            if (num_safe == (len(temp_arr) - 1)):

                safe += 1

                print(safe)

        elif increasing == False and decreasing == True:

            if (num_safe == (len(temp_arr) - 1)):

                safe += 1
        
        
        elif increasing == True and decreasing == True:

            pass

        elif increasing == False and decreasing == False:

            pass

print(f"Is safe, {safe}")
