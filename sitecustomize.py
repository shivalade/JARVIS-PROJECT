"""Project-level compatibility fixes for third-party libraries.

This avoids NumPy 2.5 deprecation warnings from sounddevice's internal
array reshaping logic by replacing the deprecated shape mutation with the
recommended reshape-based view.
"""

from __future__ import annotations

try:
    import numpy as np
    import sounddevice as _sd

    _original_array = getattr(_sd, "_array", None)
    if _original_array is not None:
        def _patched_array(buffer, channels, dtype):
            data = np.frombuffer(buffer, dtype=dtype)
            return data.reshape(-1, channels)

        _sd._array = _patched_array
except Exception:
    # The project may be started before dependencies are installed; keep startup
    # non-fatal and let normal dependency installation handle the rest.
    pass
