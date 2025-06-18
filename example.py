# W twoim kodzie:
from utils import print_coloured_at

def demo(screen):
    print_coloured_at(screen, "[red]Czerwony[/red] [yellow]żółty[/yellow] biały", 2, 2)
    screen.refresh()
    screen.wait_for_input(1)

if __name__ == "__main__":
    from asciimatics.screen import Screen
    Screen.wrapper(demo)
