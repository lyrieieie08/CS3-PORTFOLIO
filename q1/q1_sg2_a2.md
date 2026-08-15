Section: 9 Balingkilat                                      Score:____________

C# / Name: 19-20-21 / Bondoc, Carbungco, Cato               Date: 08/14/26


The problem: Finding the highest (Maximum) number from a given list of numbers.


PseudoCode 1

Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm

PseudoCode 2

Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm


1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

   The faster algorithm would likely end up being pseudocode 1, as it utilizes a simpler, more straightforward code using only one nested loop with fewer steps that pseudocode 2.


2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

   At a glance, Pseudocode 1 is shorter in terms of text and the variable names are considerably easier to understand and descriptive than Pseudocode 2. The logic is also simpler for pseudocode 1, it will sort through the given list of numbers in increasing order and stopping once there are no more higher numbers, all in a few lines of code, unlike the expanded Pseudocode 2.


3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________


4. Testability
Which algorithm is easier to test with different inputs? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________


5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
 

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
