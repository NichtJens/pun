
def itemize(iterable, header=None, bullet="-"):
    if not bullet.endswith(" "):
        bullet += " "

    iterable = sorted(iterable)
    lines = [f"{bullet}{i}" for i in iterable]
    lines.append("")

    if header:
        header = format_header(header)
        lines = [header] + lines

    return "\n".join(lines)


def format_header(msg, line="-"):
    msg = f"{msg}:"
    line = line * len(msg)
    return f"{msg}\n{line}"



