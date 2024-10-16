def show_stars(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# # Test
# show_stars(23)

def show_sharps(rows):
    for i in range(1, rows + 1):
        blanks = rows - i
        print(' ' * blanks + '#' * i)


# # Test
# show_sharps(23)
import flask