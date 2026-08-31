'''
follow_acc = eval(input("Follows account: "))
close_frnd = eval(input("Close friend: "))
if follow_acc:
    if close_frnd:
        print("Story Visible")
    else:
        print("Not in close friend list")
else:
    print("Follow the account firsr")
    '''

'''
register=eval(input("Are you registered? (True/False): "))
entry_fee = eval(input("Entry fee paid? (True/False): "))
if register:
    if entry_fee:
        print("Tournament entry confirmed")
    else:
        print("Entry fee not paid")
else:
    print("Not registered, please register first")
    '''

link_active = eval(input("Is the link active? (True/False): "))
access = eval(input("Do you have access? (True/False): "))
if link_active:
    if access:
        print("File opened successfully")
    else:
        print("Access denied")
else:
    print("Invalid file link")
