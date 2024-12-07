"""Hometask 18_2."""

"""
Ітератори:
Реалізуйте ітератор для зворотного виведення елементів списку.
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('03'))


class ReverseList:
    """Reverse elements in the list."""

    def __init__(self, lst):
        """Initialize list and the list's length."""
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        """Iterate over values."""
        return self

    def __next__(self):
        """Return the next element in reverse order."""
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]


lst1 = (':)', 'homework', 'my', 'checking', 'for', 'Thanks')
rev_iter = ReverseList(lst1)
print('Iterating in reverse order: \n')
for item in rev_iter:
    print(item)


"""
Ітератори:
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""

print(TASK_START_TEMPLATE.format('04'))


class AllEvenSearcher:
    """Search for even numbers in a range from 0 to limit."""

    def __init__(self, limit):
        """Initialize limit and set current value to 0."""
        self.limit = limit
        self.current = 0

    def __iter__(self):
        """Return the iterator object."""
        return self

    def __next__(self):
        """Return the next even number in the range."""
        while self.current < self.limit:
            if self.current % 2 == 0:
                res = self.current
                self.current += 1
                return res
            self.current += 1
        raise StopIteration


lim = 20
result = AllEvenSearcher(lim)
print(f'All even numbers up to {lim}:')
for item in result:
    print(item, end=' ')
