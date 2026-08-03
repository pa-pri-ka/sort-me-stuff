import datetime as dt
import os
from pathlib import Path

import pytest

from app.files.file import File
from app.files.file_actions import Actions, actionsOnFiles

PATH = Path(os.path.join("a", "file.txt"))
PATH_OTHER_LOCATION = Path(os.path.join("a", "b", "file.txt"))
PATH_OTHER_FILENAME = Path(os.path.join("a", "differentfile.txt"))
PATH_OTHER_LOCATION_AND_FILENAME = Path(os.path.join("a", "b", "differentfile.txt"))
SIZE = 100
SIZE_OTHER = 200
CREATED = dt.datetime(2025, 1, 1)  # noqa: DTZ001
CREATED_OTHER = dt.datetime(2026, 1, 1)  # noqa: DTZ001
UPDATED = dt.datetime(2025, 1, 1)  # noqa: DTZ001
UPDATED_OTHER = dt.datetime(2026, 1, 1)  # noqa: DTZ001
##
COPY_MOVE_REPLACE_DELETE = (
    Actions.COPY | Actions.MOVE | Actions.REPLACE | Actions.DELETE
)
DELETE = Actions.DELETE

files = [
    (File(PATH, SIZE, CREATED, UPDATED), "LFSCU"),
    (File(PATH, SIZE, CREATED, UPDATED_OTHER), "LFSC !U"),
    (File(PATH_OTHER_LOCATION, SIZE, CREATED, UPDATED_OTHER), "FSC !LU"),
    (File(PATH, SIZE_OTHER, CREATED, UPDATED_OTHER), "LFC !SU"),
    (File(PATH, SIZE, CREATED_OTHER, UPDATED_OTHER), "LFS !CU"),
    (File(PATH, SIZE_OTHER, CREATED_OTHER, UPDATED_OTHER), "LF !SCU"),
    (File(PATH_OTHER_FILENAME, SIZE, CREATED, UPDATED), "LSCU !F"),
    (File(PATH_OTHER_FILENAME, SIZE, CREATED, UPDATED_OTHER), "LSC !FU"),
    (File(PATH_OTHER_LOCATION_AND_FILENAME, SIZE, CREATED, UPDATED_OTHER), "SC !LFU"),
    (File(PATH_OTHER_FILENAME, SIZE_OTHER, CREATED, UPDATED_OTHER), "LC !FSU"),
    (File(PATH_OTHER_FILENAME, SIZE, CREATED_OTHER, UPDATED_OTHER), "LS !FCU"),
    (File(PATH_OTHER_FILENAME, SIZE_OTHER, CREATED_OTHER, UPDATED_OTHER), "L !FSCU"),
]

tests = []
for source in files:
    for target in files:
        test_id = source[1] + " || " + target[1]
        source_file = source[0]
        target_file = target[0]

        expected = Actions.NONE
        if source_file.compareWith(target_file) == File.Prop.NONE:
            expected = (DELETE, DELETE)
        else:
            expected = (COPY_MOVE_REPLACE_DELETE, COPY_MOVE_REPLACE_DELETE)

        tests.append(pytest.param(source_file, target_file, expected, id=test_id))


@pytest.mark.parametrize("source,target,expected", tests)
def it_returns_the_possible_actions_for_source_and_target_files(
    source, target, expected
):
    actions = actionsOnFiles(source, target)
    assert actions == expected
