import os
from pathlib import Path


def find_scripts(path):
    path = Path(path)
    scripts = path.glob("**/*.py")
    scripts = sorted(n for n in scripts if n.is_file())
    return scripts


def fn_to_module(base, fn):
    base = Path(base)
    module = fn.relative_to(base.parent).with_suffix("")
    module = str(module).replace(os.sep, ".")
    return module



