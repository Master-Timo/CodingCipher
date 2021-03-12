# Function to demonstrate printing pattern :  Left Triangle
def py_pattern(n):
    # number of spaces
    k = 2 * n - 2

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 2

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


def py_pattern_alphabets(n):
    # initializing starting number
    num = 65

    # outer loop to handle number of rows
    for i in range(0, n):

        # not re assigning num
        # num = 65

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            print(chr(num), end=" ")

            # incrementing number at each column
            num = num + 1

        # ending line after each row
        print("\r")


# ===================== Driver Code ================================#
if __name__ == '__main__':
    number_of_elements = 5      # Controls both the pattern blocks
    
    py_pattern(number_of_elements)
                #           *
                #         * *
                #       * * *
                #     * * * *
                #   * * * * *
    py_pattern_alphabets(number_of_elements)
                #    A
                #    B C
                #    D E F
                #    G H I J
                #    K L M N O 