from enum import IntFlag

from app.files.file import File


class Actions(IntFlag):
        NONE = 0
        COPY = 1
        MOVE = 2
        REPLACE = 4
        DELETE = 8

COPY_MOVE_REPLACE_DELETE = (
    Actions.COPY | Actions.MOVE | Actions.REPLACE | Actions.DELETE
)
DELETE = Actions.DELETE

def actionsOnFiles(source: File, target: File):
    if source.compareWith(target) == File.Prop.NONE:
        return (DELETE, DELETE)
    else:
        return (COPY_MOVE_REPLACE_DELETE, COPY_MOVE_REPLACE_DELETE)


