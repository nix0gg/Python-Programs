emails = tuple()  # Initializes an empty tuple for emails
username = tuple()  # Initializes an empty tuple for usernames
domainname = tuple()  # Initialize an empty tuple for domain names
n = int(input("How many Email-IDs do you want to enter? :"))  # Accepts number of email IDs from user
for i in range(0, n):  # Loops for each email ID
    emid = input("> ")  # Accepts email ID from user
    emails = emails + (emid,)  # Adds an email to emails tuple
    spl = emid.split("@")  # Splits the email into username and domain
    username = username + (spl[0],)  # Adds a username to tuple
    domainname = domainname + (spl[1],)  # Adds a domain name to tuple
print("\nThe Email-IDs you entered are :")  # Prints all entered email IDs
print(emails)  # Prints emails tuple
print("\nThe username in the Email-IDs are :")  # Prints all usernames
print(username)  # Prints usernames tuple
print("\nThe domain names in the Email-IDs are :")  # Prints all domain names
print(domainname)  # Prints domain names tuple