import copy
import sys

class ConsistencyError(Exception):
    pass

class SudokuBoard(object):
    def __init__(self):
        self.cells = {}
        for i in xrange(9):
            for j in xrange(9):
                self.cells[(i, j)] = set(xrange(1, 10))

    @staticmethod
    def from_text(text):
        """Text is each row of the board separated by spaces, e.g.:
        ..53..... 8......2. .7..1.5.. 4....53.. .1..7...6 ..32...8. .6.5....9 ..4....3. .....97..
        """
        b = SudokuBoard()
        for i, row in enumerate(text.strip().split()):
            for j, col in enumerate(row):
                if col != '.':
                    b.set_cell((i, j), int(col))
        return b

    @staticmethod
    def linked_cells((i, j)):
        linked = set()
        linked |= set((i, k) for k in xrange(9))
        linked |= set((k, j) for k in xrange(9))
        linked |= set((i - i%3 + t, j - j%3 + u) for t in xrange(3) for u in xrange(3))
        linked.remove((i, j))
        return linked

    def is_fixed(self, (i, j)):
        return len(self.cells[(i, j)]) == 1

    def fixed_val(self, (i, j)):
        assert self.is_fixed((i, j))
        return iter(self.cells[(i, j)]).next()

    def set_cell(self, (i, j), val):
        if val not in self.cells[(i, j)]:
            raise ConsistencyError('not a valid choice for this cell')

        self.cells[(i, j)] = set([val])
        for lc in SudokuBoard.linked_cells((i, j)):
            was_fixed = self.is_fixed(lc)
            self.cells[lc] -= set([val])
            if not self.cells[lc]:
                raise ConsistencyError('no remaining possibilites for linked cell')
            if not was_fixed and self.is_fixed(lc):
                # propagate
                self.set_cell(lc, self.fixed_val(lc))

    def is_solved(self):
        return all(self.is_fixed(c) for c in self.cells.iterkeys())

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        def chr((i, j)):
            return str(self.fixed_val((i, j))) if self.is_fixed((i, j)) else '.'
        return '\n'.join(''.join(chr((i, j)) for j in xrange(9)) for i in xrange(9))

    def solve(self):
        if self.is_solved():
            yield self
            return

        unfixed = (c for c in self.cells.iterkeys() if not self.is_fixed(c))
        most_constrained = min(unfixed, key=lambda c: len(self.cells[c]))

        for choice in self.cells[most_constrained]:
            new_board = self.clone()

            try:
                new_board.set_cell(most_constrained, choice)
            except ConsistencyError:
                continue

            for solution in new_board.solve():
                yield solution

if __name__ == "__main__":

    """Usage:

    sudoku.py \
      ..53..... \
      8......2. \
      .7..1.5.. \
      4....53.. \
      .1..7...6 \
      ..32...8. \
      .6.5....9 \
      ..4....3. \
      .....97..
    """
 
    for i, board in enumerate(SudokuBoard.from_text(' '.join(sys.argv[1:])).solve()):
        print board
        print

    print '%d solution(s)' % (i + 1)


