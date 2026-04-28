from __future__ import annotations

import re
import typing as t
from importlib.util import find_spec

__all__ = ['LinearSegmentedColormap', 'ListedColormap', 'register_cmap']


if find_spec("matplotlib") or t.TYPE_CHECKING:
    import matplotlib as mpl
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap

    MPL_VERSION = tuple(map(int, re.findall(r"\d+", mpl.__version__)[:3]))

    if MPL_VERSION >= (3, 6, 0):
        from matplotlib import colormaps
        def register_cmap(name: str, cmap: t.Any) -> None:
            if name not in colormaps or colormaps[name] != cmap:
                # The last condition will raise an error
                colormaps.register(cmap, name=name)
    else:
        from matplotlib.cm import register_cmap  # type: ignore
else:
    MPL_VERSION = (0, 0, 0)
    class LinearSegmentedColormap:
        def __init__(self, name: str, segmentdata: dict[str, t.Any], N: int = 256, gamma: float = 1.0) -> None: ...
        @classmethod
        def from_list(cls, name: str, colors: t.Any, N: int = 256, gamma: float = 1.0) -> LinearSegmentedColormap: ...

    class ListedColormap:
        def __init__(self, colors: t.Any, name: str = "from_list", N: int | None = None) -> None: ...

    def register_cmap(name: str, cmap: t.Any) -> None: ...
