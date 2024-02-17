import ast


class Collector(ast.NodeVisitor):

    def __init__(self, start, ignore=None):
        self.start = start
        self.ignore = ignore or []
        self.collected = {"import": [], "from": []}

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name not in self.ignore:
                self.collected["import"].append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module
        level = node.level

        if level:
            base = self.start.rsplit(".", level)[0]
            if module is None:
                module = base
            else:
                module = f"{base}.{module}"

        if module not in self.ignore:
            for alias in node.names:
                self.collected["from"].append((module, alias.name))
        self.generic_visit(node)

    def report(self):
        imp = self.collected["import"]
        fro = self.collected["from"]

        if imp:
            for i in imp:
                print(i)
        else:
            print("<no imports>")

        if fro:
            for i in fro:
                m, n = i
                print(f"{m}:{n}")
        else:
            print("<no from imports>")



