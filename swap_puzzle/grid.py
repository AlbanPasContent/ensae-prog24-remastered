"""
This is the grid module. It contains the Grid class and its associated methods.
"""


import random


class Grid:
    """
    A class representing the grid from the swap puzzle. It supports
    rectangular grids.

    Attributes
    ----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the
        number in the cell (i, j), i.e., in the i-th line and j-th column.
        Note: lines are numbered 0..m-1 and columns are numbered 0..n-1.
    """

    def __init__(self, initial_state: list[list[int]]):
        """
        Initializes the grid.

        Parameters
        ----------
        initial_state: list[list[int]]
            The initial state of the grid.

        Raises
        ------
        ValueError
            If the grid is empty, contains an empty row or not rectangular.
        """
        if not initial_state:  # Check if the grid is empty
            raise ValueError("The grid cannot be empty.")
        if any(len(row) == 0 for row in initial_state):
            raise ValueError("The grid contains an empty row.")

        self.m = len(initial_state)
        self.n = len(initial_state[0])

        if not all(len(i_line) == self.n for i_line in initial_state):
            raise ValueError("The grid must be rectangular.")

        self.state = initial_state

    def __str__(self) -> str:
        """
        Returns the state of the grid as text.

        Returns
        -------
        output: str
            A string representation of the grid's state, including a header
            line and one line per grid row.
        """
        output = "The grid is in the following state:\n"
        for i in range(self.m):
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self) -> str:
        """
        Returns a representation of the grid with number of lines and columns.

        Returns
        -------
        output: str
            A formal representation of the grid, indicating its class,
            number of lines (m), and number of columns (n).
        """
        output = f"<grid.Grid: m={self.m}, n={self.n}>"
        return output

    def is_sorted(self) -> bool:
        """
        Checks if the current state of the grid is sorted and returns the
        answer as a boolean.
        """
        # TODO: Implement this function
        # NOTE: Remove the line "raise NotImplementedError"
        raise NotImplementedError

    def swap(self, cell1: tuple[int], cell2: tuple[int]):
        """
        Implements the swap operation between two cells. Raises an exception
        if the swap is not allowed.

        Parameters
        ----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i
            is the line and j the column number of the cell.

        Raises
        ------
        Exception
            If the two cells to swap are not side by side (diagonal swaps
            aren't allowed).
        """
        # TODO: Implement this function
        # NOTE: Remove the line "raise NotImplementedError"
        raise NotImplementedError

    def swap_seq(self, cell_pair_list: list[tuple[tuple[int]]]):
        """
        Executes a sequence of swaps.

        Parameters
        ----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell
            being a tuple of integers).
            So the format should be :
            [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # TODO: Implement this function
        # NOTE: Remove the line "raise NotImplementedError"
        raise NotImplementedError

    @classmethod
    def create_sorted(cls, m: int, n: int):
        """
        Create an m*n sorted grid.

        Parameters
        ----------
        m : int
            Number of lines in the grid.
        n : int
            Number of columns in the grid.

        Returns
        -------
        grid: Grid
            An m*n size sorted grid.

        Raises
        ------
        ValueError
            If either m or n is not a positive integer, indicating that the
            dimensions of the grid are invalid.
        """
        if m <= 0 or n <= 0:
            raise ValueError("Both m and n must be positive integers.")

        initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        grid = cls(initial_state)
        return grid

    @classmethod
    def create_random(cls, m: int, n: int):
        """
        Create an m*n grid where the cells are randomly placed.

        Parameters
        ----------
        m : int
            Number of lines in the grid.
        n : int
            Number of columns in the grid.

        Returns
        -------
        grid: Grid
            An m*n random grid.

        Raises
        ------
        ValueError
            If either m or n is not a positive integer, indicating that the
            dimensions of the grid are invalid.
        """
        if m <= 0 or n <= 0:
            raise ValueError("Both m and n must be positive integers.")

        int_list = list(range(1, m * n + 1))
        random.shuffle(int_list)  # Shuffle the list directly into place
        initial_state = [int_list[i * n:(i + 1) * n] for i in range(m)]
        grid = cls(initial_state)
        return grid

    @classmethod
    def grid_from_file(cls, file_name: str):
        """
        Creates a grid object from class Grid, initialized with the
        information from the file file_name.

        Parameters
        ----------
        file_name: str
            Name of the file to load. The file must be of the format:
            - first line contains "m n"
            - next m lines contain n integers that represent the state of the
            corresponding cell

        Returns
        -------
        grid: Grid
            The grid.
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n:
                    raise ValueError("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(initial_state)
        return grid
