import os
from random import randint
from datetime import datetime, timedelta

# Change to the directory containing your Git repository if needed
# os.chdir('/path/to/your/repo')  # Uncomment and replace with your repo path if needed

# Function to generate a date string in ISO 8601 format
def generate_commit_date(days_ago):
    date = datetime.now() - timedelta(days=days_ago)
    return date.strftime('%Y-%m-%d %H:%M:%S')  # Use space instead of 'T' to avoid Git issues

# Loop through a range of days (e.g., 1 to 59 days ago)
for i in range(1, 60):
    for j in range(randint(1, 5)):  # Random number of commits per day (between 1 and 5)
        # Simulate a change by appending a string to a file
        change_description = f"Commit on {i} days ago"
        with open('file.txt', 'a') as file:
            file.write(change_description + '\n')  # Adding a line to the file
        
        # Stage the changes
        os.system('git add .')

        # Generate the commit date for the current day in the loop
        commit_date = generate_commit_date(i)

        # Print the commit date for debugging
        print(f"Committing with date: {commit_date}")

        # Commit the changes with the generated date
        commit_command = f'git commit --date="{commit_date}" -m "Commit {i} days ago"'
        os.system(commit_command)

# Push all commits to the remote repository
os.system('git push -u origin main')
