import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# ============================================================
# SETTINGS — change these
# ============================================================

# Number of squares in figure n:
formula = lambda n: 3*n + 1

# Other examples:
# formula = lambda n: n**2
# formula = lambda n: n + (n + 1)**2

figure_numbers = [1, 2, 3]

# None: automatically make the arrangement roughly square.
# Alternatively: columns = lambda n: n + 1
columns = None

fill_color = "#b3d5e8"
edge_color = "black"
line_width = 2
gap = 2
label_size = 16
label_offset = 0.65
square_size_inches = 0.42

# Set to None to skip saving.
save_svg = "figures_new.svg"
save_png = "figures.png"


# ============================================================
# BUILD THE FIGURES
# ============================================================

def square_positions(n):
    """Return the lower-left corner of each square in figure n."""
    count = formula(n)

    if count < 1 or int(count) != count:
        raise ValueError(
            f"Formula must give a positive integer; "
            f"for n={n}, it gave {count}."
        )

    count = int(count)

    if columns is None:
        ncols = math.ceil(math.sqrt(count))
    else:
        ncols = columns(n)

        if ncols < 1 or int(ncols) != ncols:
            raise ValueError(
                "The number of columns must be a positive integer."
            )

        ncols = int(ncols)

    # Fill rows from left to right, starting at the bottom.
    return [(i % ncols, i // ncols) for i in range(count)]


layouts = [square_positions(n) for n in figure_numbers]

widths = [max(x for x, y in points) + 1 for points in layouts]
heights = [max(y for x, y in points) + 1 for points in layouts]

total_width = sum(widths) + gap * (len(layouts) - 1)
max_height = max(heights)

fig, ax = plt.subplots(
    figsize=(
        (total_width + 1) * square_size_inches,
        (max_height + 2) * square_size_inches,
    )
)

# Transparent figure and axes backgrounds.
fig.patch.set_facecolor("none")
ax.patch.set_facecolor("none")

x_offset = 0

for n, points, width in zip(figure_numbers, layouts, widths):
    # Draw the colored squares without individual borders.
    for x, y in points:
        ax.add_patch(
            Rectangle(
                (x_offset + x, y),
                1,
                1,
                facecolor=fill_color,
                edgecolor="none",
            )
        )

    # Draw shared borders only once.
    edges = set()

    for x, y in points:
        corners = [
            (x, y),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
        ]

        for start, end in zip(corners, corners[1:] + corners[:1]):
            edges.add(tuple(sorted((start, end))))

    for (x1, y1), (x2, y2) in sorted(edges):
        ax.plot(
            [x_offset + x1, x_offset + x2],
            [y1, y2],
            color=edge_color,
            linewidth=line_width,
            solid_capstyle="butt",
        )

    ax.text(
        x_offset + width / 2,
        -label_offset,
        f"Figur {n}",
        ha="center",
        va="top",
        fontsize=label_size,
    )

    x_offset += width + gap

ax.set_aspect("equal")
ax.set_xlim(-0.5, total_width + 0.5)
ax.set_ylim(-1.5, max_height + 0.5)
ax.axis("off")

fig.tight_layout(pad=0.3)

if save_svg:
    fig.savefig(
        save_svg,
        transparent=True,
        facecolor="none",
        edgecolor="none",
        bbox_inches="tight",
    )

if save_png:
    fig.savefig(
        save_png,
        dpi=300,
        transparent=True,
        facecolor="none",
        edgecolor="none",
        bbox_inches="tight",
    )

plt.show()