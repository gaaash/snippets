import os 


# APT related commands
aptupdate = "sudo apt update && sudo apt upgrade -y"

# UV related commands
uvselfupdate = "uv self update"
check_venv = 'echo "$VIRTUAL_ENV"'
activate_venv = "avenv"
uv_vevn_update = "uv lock --upgrade"
deactivate_venv = "dvenv"

# BREW related commands
brew_self_update = "brew upgrade"
brews_formula_update = "brew upgrade --cask"
brew_cleanup = "brew cleanup"

# FLATPAK realted commands 
flatpak_update = "flatpak update"
flatpak_cleanup = "flatpak uninstall --unused"


# Update system APT packages
def apt_updater():
    state_type = ''
    try:
        os.system(aptupdate)
        state_type = "APT DONE..."
        return state_type
    except Exception:
        state_type = "ERROR: unable to update APT packages"
        return state_type

# Update UV
def uv_updater():
    state_type = ''
    os.system(uvselfupdate)
    userinput = input("Update venv packages in this Dir ? (y/n) ") or "n"
    if userinput.lower() == "y":
        if os.path.exists(".venv"):
            output = os.system(check_venv)
            if output == "":
                os.system(activate_venv)
            os.system(uv_vevn_update)
            os.system(deactivate_venv)
        else:
            state_type = "UV ERROR: There is no venv in this directory..."
            return state_type
    state_type = "UV DONE..."
    return state_type

# Update Brew  
def brew_updater():
    state_type = ''
    try:
        os.system(brew_self_update)
        os.system(brews_formula_update)
        os.system(brew_cleanup)
        state_type = "Brew DONE..."
        return state_type
    except Exception:
        state_type = "ERROR: unable to update HomeBrew"
        return state_type


# Update Flatpak 
def flatpak_updater():
    state_type = ''
    try:
        os.system(flatpak_update)
        os.system(flatpak_cleanup)
        state_type = "Flatpak DONE..."
        return state_type
    except Exception:
        state_type = "ERROR: unable to update Flatpak"
        return state_type



def main():
    os.system('clear')
    separator = "#" * __import__("shutil").get_terminal_size().columns 
    apt     = False
    uv      = False
    brew    = False
    flatpak = False
    menu    = '''
1) All
2) APT 
3) UV
4) HomeBrew
5) Flatpak
    '''
    
    print(menu)
    update_user_selections = (input('Select updates you want to run (default -> 1): ').strip() or "1").split() 

    os.system("clear")
    if len(update_user_selections) == 1 and '1' in update_user_selections:
        apt     = True
        uv      = True
        brew    = True
        flatpak = True
        print(separator)
        apt_status_code= apt_updater()
        print(separator)
        uv_status_code= uv_updater()
        print(separator)
        brew_status_code  = brew_updater()
        print(separator)
        flatpak_status_code = flatpak_updater()
    
    elif len(update_user_selections) > 1 and '1' in update_user_selections:
        print("ERROR: wrong input (can't use All with other options)")
    else:
        for i in update_user_selections:
            match i:
                case '2':
                    apt = True
                    apt_status_code= apt_updater()
                    print(separator)
                case '3':
                    uv = True
                    uv_status_code= uv_updater()
                    print(separator)
                case '4':
                    brew = True
                    brew_status_code  = brew_updater()
                    print(separator)
                case '5':
                    flatpak = True
                    flatpak_status_code = flatpak_updater()
                    print(separator)
    print('\n',f'''
{separator}
{apt_status_code if apt else "apt not selected"}
{uv_status_code if uv else "uv not selected"}
{brew_status_code if brew else "brew not selected"}
{flatpak_status_code if flatpak else "flatpak not selected"}
{separator}
    ''')

if __name__ == '__main__':
    main()
