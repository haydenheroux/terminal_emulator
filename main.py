from term import Terminal


def show_window(term):
    """
    Shows four lines of the terminal.
    Note that the `print` here can be changed for a GUI text-renderer!
    """
    # This is here to make seeing the beginning and end of each window easier
    debug_separator = "=" * 40

    print(debug_separator)

    # This is just a loop through four lines of the terminal!
    # Each line is just a string and can be displayed however you want!
    for line in term.get_lines(4):
        # For this example, display to a console
        print(line)

    print(debug_separator)


def attack_menu(term):
    """
    Puts the attack menu into the terminal.
    """
    term.add_line("1. ATTACK")
    term.add_line("2. DEFEND")
    term.add_line("3. ITEMS")
    term.add_line("4. RETREAT")


def empty_line(term):
    """
    Puts an empty (blank) line into the terminal.
    Used for making space between menus.
    """
    term.add_line("")


def items_menu(term):
    """
    Puts the items menu into the terminal.
    """
    term.add_line("1. POISON GRENADE")
    term.add_line("2. LIGHT GRENADE")
    term.add_line("3. WEIRD STEAK")
    term.add_line("4. STREETWATER")
    term.add_line("5. GUNPOWDER GRENADE")


if __name__ == "__main__":
    term = Terminal()

    # Attack menu
    attack_menu(term)

    # Show the user their options
    term.scroll_to_bottom()
    show_window(term)

    # Pretend the user selected the items option
    empty_line(term)
    items_menu(term)

    # Show the user their items
    term.scroll_to_bottom()
    show_window(term)

    # I can't see all of my items! Scroll up please!
    term.scroll_up(4)
    # Show the user the rest of their items
    show_window(term)

    # Where was I again?
    term.scroll_to_top()
    show_window(term)
