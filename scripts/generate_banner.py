from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def generate_banner():
    repo_root = Path(__file__).resolve().parents[1]
    output = repo_root / "docs" / "assets" / "banner.png"
    output.parent.mkdir(parents=True, exist_ok=True)

    fig = plt.figure(figsize=(6, 5), dpi=180)
    ax = fig.add_axes([0, 0, 1, 1], projection="3d")
    ax.set_axis_off()
    ax.set_box_aspect((1, 1, 1))
    ax.set_proj_type("ortho")
    ax.view_init(elev=22, azim=12)
    ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2), zlim=(-1.2, 1.2))

    longitude, latitude = np.meshgrid(
        np.linspace(0, 2 * np.pi, 25),
        np.linspace(0, np.pi, 13),
    )
    ax.plot_wireframe(
        np.cos(longitude) * np.sin(latitude),
        np.sin(longitude) * np.sin(latitude),
        np.cos(latitude),
        color="#788696",
        alpha=0.35,
        linewidth=0.65,
    )

    equator = np.linspace(0, 2 * np.pi, 120)
    ax.plot(np.cos(equator), np.sin(equator), 0, "--", color="#788696", lw=1)

    angle = np.pi / 3
    drift = np.linspace(0, angle, 80)
    pulse = np.linspace(0, np.pi, 80)
    echo = np.linspace(-angle, 0, 80)

    ax.plot(np.cos(drift), np.sin(drift), 0, color="#009e8e", lw=3.5)
    ax.plot(
        np.full_like(pulse, np.cos(angle)),
        np.sin(angle) * np.cos(pulse),
        np.sin(angle) * np.sin(pulse),
        color="#d45ca4",
        linestyle=":",
        lw=3,
    )
    ax.plot(np.cos(echo), np.sin(echo), 0, color="#c88b18", lw=3.5)

    slate = "#788696"
    ax.quiver(0, 0, 0, 1, 0, 0, color=slate, lw=1.8, arrow_length_ratio=0.14)
    ax.scatter([1], [0], [0], color=slate, s=30, depthshade=False)

    ax.text(1.10, 0, -0.15, r"$|+\rangle$", color=slate, fontsize=14, ha="center")
    ax.text(0, 0, 1.12, r"$|0\rangle$", color=slate, fontsize=14, ha="center")
    ax.text(0, 0, -1.15, r"$|1\rangle$", color=slate, fontsize=14, ha="center")

    fig.savefig(output, transparent=True, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print(f"Saved {output}")


if __name__ == "__main__":
    generate_banner()