import datetime as dt
import os
from pathlib import Path

from app.files.file import File


class FilesList:
    __files: list[File]
    __root_location: Path

    def __init__(self, root_location: Path):
        self.__files = []
        self.__root_location = root_location

    def contains_file_with_path(self, path: str):
        files_ending_with_path = list(
            filter(lambda file: file.path_ends_with(path), self.__files)
        )
        return len(files_ending_with_path) > 0

    def len(self):
        return len(self.__files)

    def scan_location(self):
        walk = os.walk(self.__root_location, topdown=True, followlinks=False)
        for root, _, file_paths in walk:
            for file_path in file_paths:
                path = Path(os.path.join(root, file_path))
                stat = path.stat()
                size = stat.st_size
                created = dt.datetime.fromtimestamp(stat.st_birthtime)  # noqa: DTZ006
                updated = dt.datetime.fromtimestamp(stat.st_mtime)  # noqa: DTZ006
                file = File(path, size, created, updated)
                self.__files.append(file)
        return self
