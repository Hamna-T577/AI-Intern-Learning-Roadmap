def save_emails(emails):

    with open("emails.txt", "w") as file:

        for email in emails:

            file.write(email + "\n")

    print("Emails saved to emails.txt")