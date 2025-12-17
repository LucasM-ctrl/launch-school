from datetime import datetime

age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))

current_year = 2025 #should have done [ datetime.now().year ]
years_left = retire_age - age

print(f"It's {current_year}. You will retire in {current_year + years_left}.")

print(f'You have only {years_left} years of work to go!')