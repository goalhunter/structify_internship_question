# structify_internship_question
It is a repository created for the internship question given by Structify

# The time complexity of the provided code is less than O(n^2), where 'n' is the number of elements in the data.

## algorithm
1.	Function Definition:
     •	Define a function called count_intersections with a single parameter data.
2.	Initialize Lists:
    •	Initialize two lists:
      •	intersections: to store intersection labels.
      •	unique_endpoints: to store unique ending points.
3.	Constants:
    •	Set the value of π (pie) to 3.14.
4.	Iterate through Data:
    •	Iterate through the range of the number of records in data, denoted by n.
      •	Use a nested loop (i and j), ranging from i = 0 to n for the outer loop and j = i + 1 to n for the inner loop.
5.	Check Angle Values:
    •	Check if the values in the first list of data (angles) are within the valid range (0 to 2 * π).
    •	If not, return an error message.
6.	Check Chord Labels:
    •	Check if the labels in the second list of data indicate different starting and ending points for each line (data[1][i][2:] != data[1][j][2:]).
    •	If true:
      •	Check if the points are already in the list of unique ending points.
      •	If not in the list, check if the label is already in the list of intersections.
          •	If present, remove it from the intersections list.
          •	If not present, add it to the intersections list.
    •	Check if the labels in data indicate the starting and ending points of the same line (data[1][i][2:] == data[1][j][2:]).
      •	If true:
        •	Add the ending point to the list of unique ending points.
7.	Return Result:
    •	Return the length of the intersections list.

![Notes_240204_174448](https://github.com/goalhunter/structify_internship_question/assets/39577705/3d2957a9-6218-4448-a76e-ab52337541b5)
