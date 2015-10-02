# Dungeon -> Interface


# TODO: Could include built-in help
def get_command(options):
    """Reads input from STDIN and ensures it matches a given keyword.
    Please only give it capital options like NEW or it will cause problems."""
    assert len(options) > 0, "There are no options for the user to choose from!"
    print("Commands:", options + ['HELP'])
    print("===")
    while True:
        keyword = input()
        if included_case_check(keyword, options):
            print("===")
            return keyword.upper()
        elif keyword.upper() == 'HELP':
            print("Commands:", options + ['HELP'])
            print("===")
        else:
            pass


def included_case_check(keyword, options):
    return keyword.upper() in [opt.upper() for opt in options]


def get_free_input():
    string = ""
    while string == "":
        string = input()
    return string


def wait_for_input():
    print("...")
    input()


def print_stat_table(table):
    print("HP: %s | PW: %s | DF: %s | SP: %s" %
        (table['HP'], table['PW'], table['DF'], table['SP']))


if __name__ == "__main__":
    options = ['Done', 'New', 'Attack']
    print(included_case_check('done', options) == True)
    print(included_case_check('NEW', options) == True)
    print(included_case_check('hElP', options) == False)
    
    #get_command([])
    #get_command([''])
    get_command(['Done', 'New'])
