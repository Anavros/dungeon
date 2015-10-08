# Dungeon -> Interface

def get_command(options, inFn=input, outFn=print):
    """Loops until input matches a keyword from options."""

    pass
#    if len(options) > 0:
#        raise  "There are no options for the user to choose from!"
#    else:
#        print("Commands:", options + ['HELP'])
#        print("===")
#        while True:
#            keyword = input()
#            if included_case_check(keyword, options):
#                print("===")
#                return keyword.upper()
#            elif keyword.upper() == 'HELP':
#                print("Commands:", options + ['HELP'])
#                print("===")
#            else:
#                pass


# Lightly Tested
def included(keyword, options):
    """Check if keyword is in a list of options regardless of case."""

    if type(options) is not list: options = (options,)  # Prevents scalars
    return keyword.upper() in [opt.upper() for opt in options]


# Untested
def get_free_input(inFn=input):
    string = ""
    while string == "":
        string = inFn()
    return string


# Untested
def wait_for_input(inFn=input, outFn=print):
    outFn("...")
    inFn()
