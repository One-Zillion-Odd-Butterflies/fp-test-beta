def greet(name: str) -> str:
    return f"Hi, {name}!"


def render_banner(message: str) -> str:
    width = len(message) + 4
    top = "+" + "-" * (width - 2) + "+"
    middle = f"| {message} |"
    return "\n".join([top, middle, top])


if __name__ == "__main__":
    print(render_banner("Footprints"))
    print(greet("Footprints"))
