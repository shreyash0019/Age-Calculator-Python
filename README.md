# Age Calculation Program

This program calculates a user's age in years, months, and days based on their input. It uses the `time` and `calendar` modules to handle date and time operations.

## Features

- **Leap Year Calculation**: The program includes a function to determine if a given year is a leap year.
- **Month Days Calculation**: The program includes a function to return the number of days in a given month, accounting for leap years.
- **User Input**: The program prompts the user to input their name and age.
- **Current Date and Time**: The program retrieves the current local date and time.
- **Age Calculation**: The program calculates the user's age in:
  - Years
  - Months
  - Days
- **Result Display**: The program displays the calculated age in a formatted string.

## Functions

1. **judge_leap_year(year)**:
   - Determines if a given year is a leap year using the `calendar.isleap` function.

2. **month_days(month, leap_year)**:
   - Returns the number of days in a given month.
   - Accounts for leap years when determining the number of days in February.

## Usage

1. **Input User's Name and Age**:
   - The user is prompted to enter their name and age.

2. **Retrieve Current Local Time**:
   - The program retrieves the current local date and time using the `time.localtime` function.

3. **Calculate Total Number of Years, Months, and Days**:
   - The program calculates the total number of years, months, and days based on the user's input and the current date.

4. **Display the Result**:
   - The program prints the user's age in years, months, and days in a formatted string.

## Example

When the user inputs their name as "John" and age as "25":

```
John's age is 25 years or 300 months or 9125 days
```

## Dependencies

- Python 3.x
- `time` module (standard library)
- `calendar` module (standard library)
