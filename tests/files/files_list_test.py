import datetime as dt
import os
from pathlib import Path

import pytest

from app.files.files_list import FilesList

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


@pytest.fixture(scope="session")
def root_location(tmp_path_factory):
    temp_location = tmp_path_factory.mktemp("file_paths_test")
    source_location = Path(os.path.join(temp_location, "source"))
    os.makedirs(source_location)
    subfolder = os.path.join(source_location, "subfolder")
    os.makedirs(subfolder)

    file1_path = os.path.join(source_location, "file.txt")
    with open(file1_path, "w") as f:
        f.write("This is a test file.")

    other_file1_path = os.path.join(source_location, "otherfile.txt")
    with open(other_file1_path, "w") as f:
        f.write("This is another test file.")

    subfolder_file1_path = os.path.join(subfolder, "file.txt")
    with open(subfolder_file1_path, "w") as f:
        f.write("This is a subfolder test file.")

    subfolder_other_file1_path = os.path.join(subfolder, "otherfile.txt")
    with open(subfolder_other_file1_path, "w") as f:
        f.write("This is another subfolder test file.")

    return temp_location


def it_scans_all_files_under_a_given_path(root_location):
    files_list = FilesList(root_location).scan_location()
    assert files_list.len() == 4


def it_indicates_whether_a_file_in_the_list_ends_with_a_given_path(root_location):
    files_list = FilesList(root_location).scan_location()

    assert files_list.contains_file_with_path("source\\file.txt")
    assert files_list.contains_file_with_path("source\\otherfile.txt")
    assert not files_list.contains_file_with_path("source\\imnotthere.txt")
    assert files_list.contains_file_with_path("source\\subfolder\\file.txt")
    assert files_list.contains_file_with_path("source\\subfolder\\otherfile.txt")
