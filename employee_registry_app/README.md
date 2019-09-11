# Employee Registry App

This app is a very basic interpretation of what I have learnt with python after 1 week

It isn't much, and in fact it looks very ugly, but I applied almost all the concepts of what I have learnt so far

## Concepts used

### Object Oriented Programing

So I created a class called Employee and defined the basic values like first name, last name, and pay. I also added global class variables; employee count, that I used as an id for each employee instance created, and pay raise amount.

In the class I created 2 methods. The first is only to print the employee's full name and the second method is to update the employee salary after being given the raise.

as you can see, very simple and basic stuff

### Flask

_What good is an employee registry if only people who are comfortable with the command line can use it._

I decided to create a web application that allows users to input employee information and saves each instance in a list (**this is horrible because when the server restarts all the employee data is gone!!!**).

The homepage shows a form for the user to fill the employee information and also can click "Employee List" to check on all the employees added previously.

in the employee_list page, the user can click on any employee name to check their info

in the employee info page, the user can apply the raise to the selected employee

## Next steps

Now as I mentioned this is a very simplistic bare bones app with a lot (and I can't stress **a lot** enough) of improvements needed

### ideas for improvements

[ ] create a function that checks if the employee being added has been added before or not
[ ] create a search feature in the employee_list page that helps the user filter through a long list of employees
[ ] scratch the object oriented feature and replace is with SQLight so that the employee list is saved even after a server has been restarted
[ ] add some pixy dust to make this visually appealing

Thank you for checking this project out, and please take it easy on me. As of Sept. 11 2019, it would be only a week since I picked up python
