<<<<<<< HEAD
"""Regression guard for issue #1390 — the README banner / ASCII art was not in a
fenced code block, so GitHub's markdown collapsed its leading whitespace and the
box-drawing rules, rendering it misaligned instead of monospace-as-typed.

This pins that the decorative banner stays inside a ``` code fence.
=======
"""Regression guard for the README title presentation.

Originally (#1390) the README opened with an ASCII-art banner that had to live
inside a ``` code fence, otherwise GitHub's markdown collapsed its leading
whitespace and box-drawing rules and rendered it misaligned. The README refresh
(#4306) dropped that banner in favour of a centered wordmark image, so the guard
now pins the wordmark identity instead, while still catching the original failure
mode if an un-fenced ASCII banner is ever reintroduced.
>>>>>>> e3035826bce87dca91a6036e133f0f892ef50bdc
"""
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

<<<<<<< HEAD
# Distinctive bits of the banner (box-drawing rule + the kaomoji version line).
_RULE = "─" * 10
_BANNER_LINE = "Odysseus vers. 1.0"
=======
# Box-drawing rule from the legacy ASCII banner (the #1390 failure mode).
_RULE = "─" * 10
>>>>>>> e3035826bce87dca91a6036e133f0f892ef50bdc


def _fenced_segments(text: str):
    """Return the segments of *text* that sit INSIDE ``` fences."""
    parts = text.split("```")
    # parts[0] is before the first fence, parts[1] is inside the first fence, ...
    return parts[1::2]


<<<<<<< HEAD
def test_readme_banner_is_inside_a_code_fence():
    text = README.read_text(encoding="utf-8")
    assert _BANNER_LINE in text, "banner line missing from README"
    inside = "\n".join(_fenced_segments(text))
    assert _BANNER_LINE in inside, "banner version line must be inside a ``` code fence"
    assert _RULE in inside, "banner rule line must be inside a ``` code fence"


def test_readme_title_stays_a_heading():
    # The H1 must remain a real heading, not get swallowed into the fence.
    first = README.read_text(encoding="utf-8").splitlines()[0]
    assert first.strip() == "# Odysseus"
=======
def test_readme_opens_with_wordmark_title():
    # The README must still open with a recognizable Odysseus title: now the
    # centered wordmark image rather than an H1 / ASCII banner.
    head = "\n".join(README.read_text(encoding="utf-8").splitlines()[:15])
    assert 'alt="Odysseus"' in head, "README must open with the Odysseus wordmark image"


def test_reintroduced_ascii_banner_stays_fenced():
    # Defensive: if a box-drawing banner is ever added back, it must be fenced so
    # GitHub renders it monospace-as-typed (the original #1390 regression).
    text = README.read_text(encoding="utf-8")
    if _RULE not in text:
        return
    inside = "\n".join(_fenced_segments(text))
    assert _RULE in inside, "ASCII banner rule must be inside a ``` code fence"
>>>>>>> e3035826bce87dca91a6036e133f0f892ef50bdc
