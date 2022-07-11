class CustomException(Exception):
    """Custom Execption Class"""
    pass
class NotUniqueUsername(CustomException):
    """Raise if the exeption occurs when username is not unique"""
    pass
class NegetiveAgeInteger(CustomException):
    """Raise if age is assigned negetive value"""
    pass
class UnderAge(CustomException):
    """Raised when Age is less than 16 years """
    pass
class EmailNotValid(CustomException):
    """Raised when Email is not valid"""
    pass
data = [("Joe", "Joe@Joe.com", 17), ("Adam", "adam@adam.com", 17)]
directory = dict()
for name, email, age in data:
    try:
        if name in directory:
            raise NotUniqueUsername()
        if age < 0:
            raise NegetiveAgeInteger()
        if age < 16:
            raise UnderAge()
        if not ("@" in email):
            raise EmailNotValid()
    except NotUniqueUsername:
        print("Error: "+name+" username not unique.")
    except NegetiveAgeInteger:
        print("Error: Age can not be negetive.")
    except UnderAge:
        print("Error: User "+name+" is underage.")
    except EmailNotValid:
        print("Error: Email is not valid.")
    else:
        directory["Username"] = (name, email)
