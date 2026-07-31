import datetime as dt
import os
from pathlib import Path

from app.file import File

LOCATION = "some" + os.path.sep + "path"
FILE_NAME = "filename.txt"
PATH = Path(LOCATION + os.path.sep + FILE_NAME)
SIZE = 15_000
CREATED = dt.datetime(2025, 1, 1)  # noqa: DTZ001
UPDATED = dt.datetime(2026, 1, 1)  # noqa: DTZ001


def it_instantiates_a_file_and_adds_properties_to_it():
    file = File(PATH, SIZE, CREATED, UPDATED)

    assert file._File__location == LOCATION  # pyright: ignore[reportAttributeAccessIssue]
    assert file._File__file_name == FILE_NAME  # pyright: ignore[reportAttributeAccessIssue]
    assert file._File__size == SIZE  # pyright: ignore[reportAttributeAccessIssue]
    assert file._File__created == CREATED  # pyright: ignore[reportAttributeAccessIssue]
    assert file._File__updated == UPDATED  # pyright: ignore[reportAttributeAccessIssue]


class TestFilesComparison:
    file = File(PATH, SIZE, CREATED, UPDATED)

    def it_indicates_the_files_are_equal(self):
        assert self.file.compareWith(File(PATH, SIZE, CREATED, UPDATED)) == 0

    def it_indicates_a_file_name_difference(self):
        assert (
            self.file.compareWith(
                File(Path(os.path.join(LOCATION, "other.txt")), SIZE, CREATED, UPDATED)
            )
            == File.Prop.NAME
        )

    def it_indicates_a_dir_name_difference(self):
        assert (
            self.file.compareWith(
                File(
                    Path(os.path.join("another", "path", FILE_NAME)),
                    SIZE,
                    CREATED,
                    UPDATED,
                )
            )
            == File.Prop.DIR
        )

    def it_indicates_a_size_difference(self):
        assert (
            self.file.compareWith(File(Path(PATH), SIZE + 100, CREATED, UPDATED))
            == File.Prop.SIZE
        )

    def it_indicates_a_creation_date_difference(self):
        assert (
            self.file.compareWith(
                File(Path(PATH), SIZE, CREATED + dt.timedelta(days=1), UPDATED)
            )
            == File.Prop.CREATED
        )

    def it_indicates_an_update_date_difference(self):
        assert (
            self.file.compareWith(
                File(Path(PATH), SIZE, CREATED, UPDATED + dt.timedelta(days=1))
            )
            == File.Prop.UPDATED
        )

    def it_indicates_differences_in_dir_and_name(self):
        other_file_path = Path(os.path.join("some", "other", "path", "other.txt"))
        assert self.file.compareWith(File(other_file_path, SIZE, CREATED, UPDATED)) == (
            File.Prop.DIR | File.Prop.NAME
        )

    def it_indicates_differences_in_size_and_update(self):
        other_update = UPDATED + dt.timedelta(days=1)
        assert self.file.compareWith(File(PATH, SIZE + 100, CREATED, other_update)) == (
            File.Prop.SIZE | File.Prop.UPDATED
        )
