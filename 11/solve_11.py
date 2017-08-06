"""Solve the problem 11 on projecteuler using brute-force"""

# take a file as an input and convert it into a grid of integers.
def acquire(filename):
    """Return a grid of integers by parsing a file."""
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append([int(x) for x in line.split()])
    return grid

# generator that returns product of n numbers(up, down, diag) in a grid.
def generate_products(grid, number):
    """Generator returning products from a grid."""
    for j in range(len(grid)-number):
        for i in range(len(grid[j])-number):
            products = []
            h_prod, v_prod, d_prod_r = 1, 1, 1
            for k in range(number):
                # horizontal product
                h_prod *= grid[j][i+k]

                # vertical product
                v_prod *= grid[j+k][i]

                # diagonal product right
                d_prod_r *= grid[j+k][i+k]
            products.extend([h_prod, v_prod, d_prod_r])
            yield products
        for i in range(number-1, len(grid[j])):
            products = []
            d_prod_l = 1
            for k in range(number):
                # diagonal product left
                d_prod_l *= grid[j+k][i-k]
            products.append(d_prod_l)
            yield products

# find largest product.
def largest_product(product_list):
    """Find the largest product from a given list."""
    largest = 1
    for products in product_list:
        if largest < max(products):
            largest = max(products)
    return largest

if __name__ == '__main__':
    LARGEST_PRODUCT = largest_product(generate_products(acquire('11.txt'), 4))
    print("{} is the largest product".format(LARGEST_PRODUCT))
