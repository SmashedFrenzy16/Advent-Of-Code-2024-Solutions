with open("i.txt") as file:

    inp = file.read()

first_arr = []
second_arr = []

distance_tally = 0

for i in inp.split("/n"):
    
    for index, val in enumerate(i.split()):

        if index % 2 == 0:

            first_arr.append(val)
        
        else:

            second_arr.append(val)

first_arr.sort()
second_arr.sort()

for i in range(len(first_arr)):

    if (int(first_arr[i]) > int(second_arr[i])):

            tally = int(first_arr[i]) - int(second_arr[i])
            distance_tally += tally

    elif (int(second_arr[i]) > int(first_arr[i])):

        tally = int(second_arr[i]) - int(first_arr[i])
        distance_tally += tally

print(distance_tally)

final_sim = 0

first_arr = [int(i) for i in first_arr]
second_arr = [int(i) for i in second_arr]

for i in first_arr:

    count = second_arr.count(i)

    final_sim += (i * count)

print(final_sim)
    

