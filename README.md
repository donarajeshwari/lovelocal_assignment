##Algorithm for easy 1
User Input:Prompt the user to input a string.
Variable Initialization:Initialize variables str1 with the user input, ans to 0, count to 0.
Loop through Characters:Start a loop to iterate through each character i in the input string str1.
Check for Space:Within the loop, check if the current character i is a space (" ").
Update Variables:If a space is found, update ans with the current value of count, and reset count to 0.If the character is not a space, increment the count by 1.
Print the Final Count:After the loop, print the final value of count.


##Algorithm for medium 2
Initialization:initialize the list values with elements [1, 2].
Calculate the threshold n as the floor division of the length of values by 3.
Initialize an empty dictionary count to store the count of each element.
Initialize an empty list ans to store elements occurring more than n times.
Counting Occurrences:Iterate through each element i in the values list.
If i is already a key in the count dictionary, increment its count.
If not, add i as a key in the count dictionary with a count of 1.
Checking Count against Threshold:Iterate through the items (element, count) in the count dictionary.
If the count of an element is greater than n, add that element to the ans list.
Print the Result:Print the final list ans containing elements that occurred more than n times.


##Algorithm for hard 3
User Input:Prompt the user to input an integer n.
Variable Initialization:Initialize a variable count to 0.
Loop through Range:Start a loop to iterate through each integer i in the range from 0 to n (inclusive).
Convert Integer to List of Digits:Convert the integer i to a list of its digits using list(str(i)).
Convert Digits to Integers:Convert each digit in the list to an integer using list comprehension.
Count Occurrences of 1:Inside a nested loop, iterate through the digits (j) in the list.
If the digit is 1, increment the count by 1.
Print the Final Count:After the outer loop, print the final value of count.
