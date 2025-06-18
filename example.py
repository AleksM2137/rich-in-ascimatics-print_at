from utils import print_coloured_at

def demo(screen):
    print_coloured_at(screen, "[red]red[/red] [yellow]yellow[/yellow] white", 2, 2)
    screen.refresh()
    screen.wait_for_input(1)

if __name__ == "__main__":
    from asciimatics.screen import Screen
    Screen.wrapper(demo)
