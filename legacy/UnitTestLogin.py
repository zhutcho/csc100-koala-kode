import keyring as kr

service_id = 'Wildlife Hospital'
username = ""

def TestLogin(username, password, expected):

    #Check password
    actual = True
    check_pass_word = kr.get_password(
        service_id, username)
    print(check_pass_word)

    #Password Requirement Checks
    if check_pass_word == None:
        actual = False
        return print(username + ", " + password + ", Expected: " + expected + ", actual: " + str(actual))

    elif check_pass_word != None and check_pass_word == password:
        if username == "admin":
            actual = True
            return print(username + ", " + password + ", Expected: " + expected + ", actual: " + str(actual) + " as admin")
        elif username != "admin":
            actual = True

            return print(username + ", " + password + ", Expected: " + expected + ", actual: " + str(actual) + " as staff")

    elif check_pass_word != None and check_pass_word != username:
        actual = False
        return print(username + ", " + password + ", Expected: " + expected + ", actual: " + str(actual))
    
x = 'admin'
y = 'Password1!'
test_expected = "True"
TestLogin(x, y, test_expected)