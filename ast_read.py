import ast


def ast_read(fn):
    with open(fn) as f:
        data = f.read()
    return ast.parse(data)



