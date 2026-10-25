import ast
import re
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import to_rgba


# ── Change these settings ──────────────────────────────────────
FORMULA = "(n*(n+1))"
FIGURE_NUMBERS = [1, 2, 3]

COLOR = "#0072b2"
FILL_ALPHA = 0.20
LINE_WIDTH = 1.5

SHOW_COUNTS = False
OUTPUT_NAME = FORMULA
# ──────────────────────────────────────────────────────────────


def read_formula(text):
    """Read an arithmetic expression without using eval()."""
    text = re.sub(r"\s+", "", text).replace("^", "**")

    # Allow 3n, 2(n+1), and n(n+1).
    text = re.sub(r"(\d)(?=n|\()", r"\1*", text)
    text = re.sub(r"n(?=\()", "n*", text)
    text = re.sub(r"\)(?=n|\d|\()", ")*", text)

    tree = ast.parse(text, mode="eval")

    def calculate(node, n):
        if isinstance(node, ast.Expression):
            return calculate(node.body, n)

        if isinstance(node, ast.Constant) and type(node.value) is int:
            return node.value

        if isinstance(node, ast.Name) and node.id == "n":
            return n

        if isinstance(node, ast.UnaryOp):
            value = calculate(node.operand, n)
            if isinstance(node.op, ast.USub):
                return -value
            if isinstance(node.op, ast.UAdd):
                return value

        if isinstance(node, ast.BinOp):
            left = calculate(node.left, n)
            right = calculate(node.right, n)

            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Pow):
                if not 0 <= right <= 6:
                    raise ValueError("Use an integer exponent from 0 to 6.")
                return left ** right

        raise ValueError("Use only n, integers, +, -, *, ^, and parentheses.")

    def square_count(n):
        count = calculate(tree, n)
        if not 1 <= count <= 1000:
            raise ValueError(
                f"Figure {n}: the number of squares must be from 1 to 1000."
            )
        return count

    return square_count


def square_positions(n, count):
    """Place count squares in rows of n squares, starting at the top."""
    return [
        (i % n, -(i // n))
        for i in range(count)
    ]


def draw_figures():
    if not FIGURE_NUMBERS or any(
        type(n) is not int or n < 1 for n in FIGURE_NUMBERS
    ):
        raise ValueError("FIGURE_NUMBERS must contain positive integers.")

    count_squares = read_formula(FORMULA)

    counts = [count_squares(n) for n in FIGURE_NUMBERS]
    patterns = [
        square_positions(n, count)
        for n, count in zip(FIGURE_NUMBERS, counts)
    ]

    # Shared limits keep every square the same size across the figures.
    max_width = max(max(x for x, y in points) + 1 for points in patterns)
    max_height = max(1 - min(y for x, y in points) for points in patterns)

    panel_width = max_width + 1.2
    panel_height = max_height + 1.8

    fig, axes = plt.subplots(
        1,
        len(FIGURE_NUMBERS),
        figsize=(
            0.55 * panel_width * len(FIGURE_NUMBERS),
            0.55 * panel_height,
        ),
        squeeze=False,
    )

    for ax, n, count, points in zip(
        axes[0], FIGURE_NUMBERS, counts, patterns
    ):
        width = max(x for x, y in points) + 1
        horizontal_offset = (max_width - width) / 2

        for x, y in points:
            ax.add_patch(
                Rectangle(
                    (x + horizontal_offset, y),
                    1,
                    1,
                    facecolor=to_rgba(COLOR, FILL_ALPHA),
                    edgecolor="black",
                    linewidth=LINE_WIDTH,
                    joinstyle="miter",
                )
            )

        ax.set_aspect("equal")
        ax.set_xlim(-0.6, max_width + 0.6)
        ax.set_ylim(1 - max_height - 0.4, 1.5)
        ax.axis("off")

        label = f"Figur {n}"
        if SHOW_COUNTS:
            label += f"\n{count} ruter"

        ax.text(
            0.5, -0.06, label,
            transform=ax.transAxes,
            ha="center", va="top",
            fontsize=16,
        )

    fig.subplots_adjust(
        left=0.02, right=0.98,
        bottom=0.23, top=0.98,
        wspace=0.25,
    )

    fig.savefig(f"{OUTPUT_NAME}.svg", transparent=True, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    draw_figures()