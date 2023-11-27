from screens import Menu
fase = 1

if fase == 3:
    from screens.planet_mars import Marte

if fase == 2:
    from screens.galaxy import Galaxy

if fase == 1:
    if __name__ == "__main__":
        Menu.main()
