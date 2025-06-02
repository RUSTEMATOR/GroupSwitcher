import re


with open('mash_of_info.txt', 'r') as file:
    mash_of_info = file.read()





# Regular expression to find emails and replace '_' with '@' before 'kingbilly.xyz'
email_pattern = r"([^\s@]+)_kingbilly\.xyz"
replacement = r"\1@kingbilly.xyz"

# Extract and replace to format as emails
extracted_emails = re.sub(email_pattern, replacement, mash_of_info)

# Further refine to only keep the emails, removing all other text
only_emails = re.findall(r"[^\s@]+@kingbilly\.xyz", extracted_emails)

# Join the emails into a single string separated by newlines
cleaned_emails = "\n".join(only_emails)



print(cleaned_emails)

# Write the cleaned emails to a new file
with open('cleaned_emails.txt', 'w') as file:
    file.write(cleaned_emails)

