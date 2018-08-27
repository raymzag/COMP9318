## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    # pass # **replace** this line with your code
    low = 1
    high = x
    while low <= high:
        mid = low + high >> 1
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            high = mid - 1
        else:
            low = mid + 1
    return high

################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    # pass # **replace** this line with your code
    x_1 = x_0 - (f(x_0) / fprime(x_0))
    for _ in range(1, MAX_ITER):
        x_0 = x_1
        x_1 = x_0 - (f(x_0) / fprime(x_0))
        if x_0 - x_1 < EPSILON:
            break
    return x_1

################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_sub_tree(tree, tokens):
    i = 0 
    while i < len(tokens):
        if tokens[i] == ']':
            break
        t = Tree(tokens[i])
        tree.add_child(t)
        if i + 1 != len(tokens) and tokens[i + 1] == '[':
            make_sub_tree(t, tokens[i + 2: find_close_index(tokens, i + 2)])
            i = find_close_index(tokens, i + 2)
            continue
        i += 1

def find_close_index(tokens, start):
    count = 1
    i = start
    while count != 0:
        if tokens[i] == '[':
            count += 1
        elif tokens[i] == ']':
            count -= 1
        i += 1
    return i

def make_tree(tokens): # do not change the heading of the function
    # pass # **replace** this line with your code    
    t = Tree(tokens[0])
    make_sub_tree(t, tokens[2:find_close_index(tokens, 2)])
    return t

def depth_helper(tree):
    if len(tree.children) == 0:
        return 0
    else:
        return 1 + max([depth_helper(child) for child in tree.children])

def max_depth(root): # do not change the heading of the function
    # pass # **replace** this line with your code
    return depth_helper(root) + 1
