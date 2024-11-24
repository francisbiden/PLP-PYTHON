# PLP PYTHON MODULE

# WEEK 1 ASSIGNMENT
Create a new Python file and name it "user_input.py"
Use the input() function to ask the user for their name and store it in a variable called "name".
Use the input() function to ask the user for their age and store it in a variable called "age".
Use the input() function to ask the user for their location and store it in a variable called "location".
Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
Save and run the program to see the output.

# WEEK 2 ASSIGNMENT
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.

# WEEK 3 ASSIGNMENT
Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.


# WEEK 4 ASSIGNMENT
Create a Python class named Person.
The Person class should have the following attributes:
name: representing the person's name.
age: representing the person's age.
gender: representing the person's gender.
Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
Create an instance of the Person class and call the introduce method to display the person's information.

# WEEK 5 ASSIGNMENT
Demonstrate your understanding of Python file handling by completing the following tasks.

Tasks:

File Creation:
Create a Python script (file_handling_assignment.py) that does the following:
Creates a new text file named "my_file.txt" in write mode ('w').
Write at least three lines of text to the file, including a mix of strings and numbers.




File Reading and Display:
Enhance your script to read the contents of "my_file.txt" and display them on the console.




File Appending:
Modify the script to open "my_file.txt" in append mode ('a').
Append three additional lines of text to the existing content.




Error Handling:
Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).


# WEEK 7 ASSIGNMENT
d Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.

Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.

Task 3: Data Visualization
Create at least four different types of visualizations:
Line chart showing trends over time (for example, a time-series of sales data).
Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
Histogram of a numerical column to understand its distribution.
Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
Customize your plots with titles, labels for axes, and legends where necessary.



Additional Instructions

Dataset Suggestions:

You can use publicly available datasets from sites like Kaggle or UCI Machine Learning Repository.
The Iris dataset (a classic dataset for classification problems) can be accessed via sklearn.datasets.load_iris(), which can be used for the analysis.

Plot Customization:

Customize the plots using the matplotlib library to add titles, axis labels, and legends.
Use seaborn for additional plotting styles, which can make your charts more visually appealing.

Error Handling:

Handle possible errors during the file reading (e.g., file not found), missing data, or incorrect data types by using exception-handling mechanisms (try, except).

Submission:

Ensure your submission is complete with all necessary code and explanations. Make sure that each plot is properly labeled and provides insights into the dataset.