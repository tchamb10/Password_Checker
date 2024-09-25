# Password Checker based on standards for a Strong Password set by the CyberSecurity & Infrastructure Security Agency https://www.cisa.gov/

# Passwords must maintain three key components
# Long - atleast 16 characters long
# Random - string of mixed letters, numbers, and symbols OR a passphrase containing 4-7 random words.
# Unique - used for one and only one account

# This script will check for the first two components; Length and presence of mixed letters, numbers, and symbols. 
# An output of GOOD or BAD will be given based on the given passphrase.


def check_case(passphrase):
    lower = False
    upper = False

    lower = any(char.islower() for char in passphrase)
    upper = any(char.isupper() for char in passphrase)

    return lower, upper


def check_symbols(passphrase):
    return any(not char.isalnum() for char in passphrase)


def check_numbers(passphrase):
    return any(char.isnumeric() for char in passphrase)


#####################################################################
############################# CHECKER ###############################
#####################################################################

def checker(passphrase):
    pass_bad = {
        'invalid' : 'the passphrase is invalid',
        'length' : 'make sure the length exceeds 15 characters',
        'lower' : 'please include an lowercase letter',
        'upper' : 'please include an uppercase letter',
        'number' : 'please include numeric characters',
        'symbol' : 'please include a non alphanumeric symbol'
    }


    pass_good = {
        'valid' : 'the passphrase is valid',
        'length' : 'length exceeds 15 characters',
        'lower' : 'passphrase contains lowercase letters',
        'upper' : 'passphrase contains uppercase letters',
        'number': 'passphrase contains numeric characters',
        'symbol' : 'passphrase contains non alphanumeric symbols'
    }
    

    if (len(passphrase) < 16):
        print(pass_bad['length'])
    else:
        print(pass_good['length'])


    match check_case(passphrase):
        case False, False:
            print(pass_bad['lower'], '\n', pass_bad['upper'])
        case False, True:
            print(pass_bad['lower'], '\n', pass_good['upper'])
        case True, False:
            print(pass_good['lower'], '\n', pass_bad['upper'])
        case True, True:
            print(pass_good['lower'], '\n', pass_good['upper'])


    match check_symbols(passphrase):
        case True:
            print(pass_good['symbol'])
        case False:
            print(pass_bad['symbol'])


    match check_numbers(passphrase):
        case True:
            print(pass_good['number'])
        case False:
            print(pass_bad['number'])







checker('Go0dP@ssw0rd')