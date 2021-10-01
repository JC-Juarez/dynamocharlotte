import dynamocharlotte as dc

dc.run('''

// Sorting Vector Algorith (Selection Sort) - Example Program 
// Author: Juan Carlos Juárez https://github.com/JC-Juarez
// Date: May 2021
// Dynamo Charlotte

// Traditional Variables //

var i as number
var j as number
var temp as number
var size as number

// Vector //

vector(50) nums

function getSize
    do
        print("*** Sort Vector Algorithm ***")
        println("Please insert size of the vector: ")
        input(size)
    loopwhile(size <= 0)
return

function getVector
    for i = 0 to (size - 1)
        input(nums[i])
    next
return

function sortVector
    for i = 0 to (size - 2)
        for j = (i + 1) to (size - 1)
            if(nums[i] > nums[j])
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            endif
        next
    next
return

function displayVector
    print(endl)
    for i = 0 to (size - 1)
        print(nums[i])
    next
return

main

call getSize
call getVector
call sortVector
call displayVector

end

''')