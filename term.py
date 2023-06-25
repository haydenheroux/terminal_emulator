class Terminal:
    """
    Defines a terminal emulator, with scroll-forward and scroll-back support.
    """

    def __init__(self):
        self.lines = list()
        self.index = 0

    def add_line(self, line):
        """
        Adds a line to the terminal history.
        """
        self.lines.append(line)

    def get_lines(self, number_of_lines):
        """
        Gets a number of lines from the terminal.

        :param number_of_lines: The number of lines to get.
        :return: Returns a list of lines from the terminal.
        """
        not_enough_lines = number_of_lines > len(self.lines)

        if not_enough_lines:
            return self.lines

        would_overflow = self.index + number_of_lines > len(self.lines)

        if would_overflow:
            return self.lines[-number_of_lines:]

        first_index = self.index
        last_index = self.index + number_of_lines

        return self.lines[first_index:last_index]

    def jump_to(self, line_number):
        """
        Jump to a line in the terminal.

        param line_number: The line to jump to.
        """
        is_valid_index = line_number > 0 and line_number < len(self.lines)

        if not is_valid_index:
            return

        self.index = line_number

    def scroll_up(self, n=1):
        """
        Scrolls up (backwards through history).

        :param n: Number of lines to scroll up.
        """
        if self.index >= n:
            self.index -= n

    def scroll_down(self, n=1):
        """
        Scrolls down (forwards through history).

        :param n: Number of lines to scroll down.
        """
        if self.index + n < len(self.lines) - 1:
            self.index += n

    def scroll_to_top(self):
        """
        Scrolls to the top (beginning of history).
        """
        self.index = 0

    def scroll_to_bottom(self):
        """
        Scrolls to the bottom (end of history).
        """
        self.index = len(self.lines) - 1
