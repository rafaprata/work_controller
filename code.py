import file_manipulation as f
import menu as m

def initialize():
    f.createFile()
    menu = m.Menu()
    menu.run()


if __name__ == "__main__":
    initialize()
