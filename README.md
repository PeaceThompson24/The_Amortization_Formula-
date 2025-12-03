0. Simple SDLC Explanation for My Loan Amortization Project
1. REQUIREMENT ANALYSIS:This is where I tried to understand what the project is supposed to do.The goal is to create a Python program that calculates how much a person will pay every month when they borrow money from a bank. I identified the main requirements:The user should enter the
LOAN AMOUNT (principal),
ANNUAL INTEREST RATE(%), and
LOAN DURATION(years).The program should calculate the monthly payment using the amortization formula.It should show the final monthly payment clearly.
3. SYSTEM DESIGN:Here I planned how the program will work.The program needs a function for the amortization formula.It should take user inputs.It should calculate the LOAN AMOUNT(Principal),
ANNUAL INTEREST RATE(%) and
LOAN DURATION(years).It should then apply the formula and return the monthly payment.The output should be simple and easy to read.
4. IMPLEMENT:This is where I wrote the actual Python code based on my design.I created a function called
[CALCULATE_MONTHLY_PAYMENT(): This function takes LOAN AMOUNT(principal), ANNUAL INTEREST RATE(%)(r) *under this function, this particular variables is converted to months*, LOAN DURATION(years)(n)]
Also another function [MAIN, *that handles users input, calls CALCULATE_MONTHLY_PAYMENT,and print results*
*then input the variables of*     LOAN AMOUNT(principal):        ANNUAL INTEREST RATE(%) and       LOAN DURATION (years):].
The amortization formula therefore is,
M = P × /r(1+r)^n/(1+r)^n-1
this formula would be used to run the code as the user input values to the various variables.
6. TESTING: I tested the program using different loan amounts and interest rates to check if the answer matches what online calculators give.I also tested wrong inputs zero or negative numbers Very large numbers.This helped ensure the program works correctly.
7. DEPLOYMENT AFTER TESTING: I packaged the code and uploaded it to GitHub.This makes it easy to submit and share.
8. MAINTENANCE:This is where I can make improvements later, such as,showing a full amortization table (monthly breakdown)Adding error handling Adding a GUI or HTML version making it run on a mobile app.
