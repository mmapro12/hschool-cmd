from colorama import Fore

# COLORAMA themes

hc = Fore.LIGHTWHITE_EX + '$ '
hsc = Fore.LIGHTGREEN_EX + "hschool "
inpc = Fore.LIGHTYELLOW_EX + ">> "
sc = Fore.WHITE
oc = Fore.LIGHTRED_EX


# COMMAND filter

def cmd_filter(cmd: str):
    cmd = cmd.lower()
    cmd = cmd.split()
    cmd = cmd[0]

    return cmd


# COMMANDS lists

new_s = ["newstudent", "news"]
get_s = ["getstudent", "gets"]
del_s = ["delstudent", "dels"]
set_s_s = ["setscore"]
q = ["quit", "q", "e", "exit"]
