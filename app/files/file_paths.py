import os
from pathlib import Path


class FilePaths:
    def __init__(self, root_location: Path):
        self.__root_location = root_location

    def scan_location(self) -> tuple[Path, list[Path]]:
        walk = os.walk(self.__root_location, topdown=True, followlinks=False)
        file_paths = []
        for root, _, files in walk:
            for file in files:
                file_paths.append(Path(os.path.join(root, file)))
        return (self.__root_location, file_paths)
