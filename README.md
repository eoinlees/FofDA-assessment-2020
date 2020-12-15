# Fundamentals of Data Analytics - Tasks 2020 - Assignment
## Eoin Lees - G00387888 - December 2020


The following program is an assignment for the Fundamentals of Data Analytics module in December 2020. 

A total of four tasks were given throughout the semester with a deadline of December 18th 2020

It is run using Jupyter notebooks.

It can be read directly from git hub, however for full functionallity please download and run directly from your desktop. 

### Jupyter notebooks
* Installation
    Visit https://jupyter.org/ and follow instructions to install on your macine
* To Run
    Navigate to the correct folder in the console and type the following command: Jupyter notebooks
    Use the gui provided in the web explorer and select `Tasks 2020.ipynb`

### Assignment Brief

The assignment brief was the following:

**Task 1. October 5th, 2020:** Write a Python function called `counts` that takes a list as
input and returns a dictionary of unique items in the list as keys and the number of
times each item appears as values. So, the input `['A', 'A', 'B', 'C', 'A']`
should have output `{'A': 3, 'B': 1, 'C': 1}` . Your code should not depend
on any module from the standard library1 or otherwise. You should research
the task first and include a description with references of your algorithm in the
notebook.
    
**Task 2. November 2nd, 2020:** Write a Python function called `dicerolls` that simulates
rolling dice. Your function should take two parameters: the number of dice k and
the number of times to roll the dice n. The function should simulate randomly
rolling k dice n times, keeping track of each total face value. It should then return
a dictionary with the number of times each possible total face value occurred. So,
calling the function as `diceroll(k=2, n=1000)` should return a dictionary like:
`{2:19,3:50,4:82,5:112,6:135,7:174,8:133,9:114,10:75,11:70,12:36}`

**Task 3. November 16th, 2020:** The `numpy.random.binomial` function can be used to simulate flipping a coin with a 50/50 chance of heads or tails. Interestingly, if a coin is flipped many times then the number of heads is well approximated by a bell-shaped curve. For instance, if we flip a coin 100 times in a row the chance of getting 50 heads is relatively high, the chances of getting 0 or 100 heads is relatively low, and the chances of getting any other number of heads decreases as you move away from 50 in either direction towards 0 or 100. Write some python code that simulates flipping a coin 100 times. Then run this code 1,000 times, keeping track of the number of heads in each of the 1,000 simulations. Select an appropriate plot to depict the resulting list of 1,000 numbers, showing that it roughly follows a bell-shaped curve. You should explain your work in a Markdown cell above the code.

**Task 4. November 30th, 2020:** Simpson’s paradox is a well-known statistical paradox
where a trend evident in a number of groups reverses when the groups are combined
into one big data set. Use numpy to create four data sets, each with an x array
and a corresponding y array, to demonstrate Simpson’s paradox. You might
create your x arrays using `numpy.linspace` and create the y array for each
x using notation like `y = a * x + b` where you choose the a and b for each
x , y pair to demonstrate the paradox. You might see the Wikipedia page for
Simpson’s paradox for inspiration.
2
It was broken down into 4 sections and answered with examples. Each section has its references built in along with a full list at the end of each task. 

### Results

After compiling all of the research and information into the jupyter notebook document I believe I have a much better understanding of what it means to analyise data. It has sparked an interest in statistics that i hope to persue further. I am confident that in future work I will be able to refer back to this document and use it as a starting off point for working on problems. 
