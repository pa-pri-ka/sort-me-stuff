from __future__ import annotations

import datetime as dt
import os
from enum import IntFlag
from pathlib import Path


class File:
    def __init__(
        self,
        file_path: Path,
        size: int | None = None,
        created: dt.datetime | None = None,
        updated: dt.datetime | None = None,
    ) -> None:
        (location, file_name) = os.path.split(file_path)
        self.__location = location
        self.__file_name = file_name
        self.__size = size
        self.__created = created
        self.__updated = updated

    def compareWith(self, other: File):
        dir_name_diff = (
            File.Prop.DIR if self.__location != other.__location else File.Prop.NONE
        )
        file_name_diff = (
            File.Prop.NAME if self.__file_name != other.__file_name else File.Prop.NONE
        )
        size_diff = File.Prop.SIZE if self.__size != other.__size else File.Prop.NONE
        created_diff = (
            File.Prop.CREATED if self.__created != other.__created else File.Prop.NONE
        )
        updated_diff = (
            File.Prop.UPDATED if self.__updated != other.__updated else File.Prop.NONE
        )
        return dir_name_diff | file_name_diff | size_diff | created_diff | updated_diff

    

    class Prop(IntFlag):
        NONE = 0
        DIR = 1
        NAME = 2
        SIZE = 4
        CREATED = 8
        UPDATED = 16
