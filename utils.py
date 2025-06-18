import re
from asciimatics.screen import Screen

# Mapowanie znaczników na kolory asciimatics
COLOUR_MAP = {
    "black": Screen.COLOUR_BLACK,
    "red": Screen.COLOUR_RED,
    "green": Screen.COLOUR_GREEN,
    "yellow": Screen.COLOUR_YELLOW,
    "blue": Screen.COLOUR_BLUE,
    "magenta": Screen.COLOUR_MAGENTA,
    "cyan": Screen.COLOUR_CYAN,
    "white": Screen.COLOUR_WHITE,
}

def print_coloured_at(screen, text, x, y, default_colour=Screen.COLOUR_WHITE):
    """
    Wypisuje tekst z kolorami w stylu [red]czerwony[/red] biały.
    """
    pattern = re.compile(r'\[(\w+)\](.*?)\[/\1\]', re.DOTALL)
    pos = 0
    curr_x = x
    last_colour = default_colour

    for match in pattern.finditer(text):
        start, end = match.span()
        # Wypisz tekst przed znacznikiem
        if start > pos:
            fragment = text[pos:start]
            screen.print_at(fragment, curr_x, y, last_colour)
            curr_x += len(fragment)
        # Wypisz tekst w znaczniku
        colour_name = match.group(1).lower()
        fragment = match.group(2)
        colour = COLOUR_MAP.get(colour_name, default_colour)
        screen.print_at(fragment, curr_x, y, colour)
        curr_x += len(fragment)
        pos = end
    # Wypisz resztę tekstu po ostatnim znaczniku
    if pos < len(text):
        fragment = text[pos:]
        screen.print_at(fragment, curr_x, y, last_colour)
def visible_length(text):
    """
    Zwraca długość tekstu bez znaczników [coś]...[/coś].
    """
    # Usuwa wszystkie [nazwa]...[/nazwa]
    clean = re.sub(r'\[(\w+)\](.*?)\[/\1\]', r'\2', text)
    return len(clean)
