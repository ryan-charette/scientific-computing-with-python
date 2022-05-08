<<<<<<< HEAD
<<<<<<< HEAD
# arithmetic-formatter
"Arithmetic Formatter" project from freeCodeCamp's Scientific Computing with Python certificate. The goal is to make a program using Python that meets the following rules.

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
~~~text
  235   
+  52   
-----
~~~
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Function Call:
~~~text
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
~~~
Output:
~~~text
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
~~~
Function Call:
~~~text
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
~~~
Output:
~~~text
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
~~~
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
  - If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
  - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
  - Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
  - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

If the user supplied the correct format of problems, the conversion you return will follow these rules:
  - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
  - Numbers should be right-aligned.
  - There should be four spaces between each problem.
  - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
=======
# time-calculator
Write a function named ```add_time``` that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show ```(next day)``` after the time. If the result will be more than one day later, it should show ```(n days later)``` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

```
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```
Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
>>>>>>> aa6f71088f280025c5eee9f883be7d9064a93a95
=======
# budget-app

Complete the ```Category``` class in ```budget.py```. It should be able to instantiate objects based on different budget categories like *food*, *clothing*, and *entertainment*. When objects are created, they are passed in the name of the category. The class should have an instance variable called ```ledger``` that is a list. The class should also contain the following methods:

A ```deposit``` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of ```{"amount": amount, "description": description}```.
A ```withdraw``` method that is similar to the ```deposit``` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return ```True``` if the withdrawal took place, and ```False``` otherwise.
A ```get_balance``` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A ```transfer``` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return ```True``` if the transfer took place, and False otherwise.
A ```check_funds``` method that accepts an amount as an argument. It returns ```False``` if the amount is greater than the balance of the budget category and returns ```True``` otherwise. This method should be used by both the ```withdraw``` method and ```transfer``` method.
When the budget object is printed it should display:

A title line of 30 characters where the name of the category is centered in a line of ```*``` characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.
Here is an example of the output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```
Besides the ```Category``` class, create a function (outside of the class) called ```create_spend_chart``` that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```
>>>>>>> c9502a4142baa2e0d21320158bef6709e8b2f68b
