import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("WEED_ROOT", "~/.weed/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("WEED_KEYS_ROOT", "~/.weed_keys"))).resolve()
