import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("PEAS_ROOT", "~/.peas/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("PEAS_KEYS_ROOT", "~/.peas_keys"))).resolve()
