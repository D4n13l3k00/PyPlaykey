from pathlib import Path
from typing import Union
import toml


class Config:
    def __init__(self, config_file: Union[Path, str] = None):
        self._config_file = config_file
        self._empty_config = {
            "Playkey": {
                "token": "token-here",
            }
        }

    def read(self) -> Union[dict, None]:
        if self._config_file is None:
            self._config_file = Path("config.toml")
        if not self._config_file.exists():
            toml.dump(self._empty_config, self._config_file.open("w", encoding="utf-8"))
            return None
        return toml.load(self._config_file)
