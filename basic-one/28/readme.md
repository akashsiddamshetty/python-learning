Q. Write a Python program to print out all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.

Sample numbers list:

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

solution - 

    1) we have to run for loop to exucte number array one bye one 
    2) in for loop first we will add if statement if its gets true then we we break the for loop and return the array
    3) if if- condition was not satisfied then we will print even numbers in the loop by similly divided number with 2 if its reminder gets zero then is even number 

pseudocode
    for loop 
    if number === 237 break loop
    else print number % 2 === 0 