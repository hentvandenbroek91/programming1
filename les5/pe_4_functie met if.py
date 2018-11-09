def new_password(oldpassword, newpassword):
    if newpassword == oldpassword:
        return False;

    if len(newpassword) < 6:
        return False;

    return True;

newpassword = raw_input("New Password: ");
oldpassword = raw_input("Old Password: ");
print(new_password(newpassword, oldpassword));