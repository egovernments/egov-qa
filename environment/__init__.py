from .common import *

from .dev import *

import os

TEST_ENV = os.getenv("TEST_ENV", "dev")


def to_absolute_path(path):
    return list(map(lambda p: os.path.abspath(p), path))


DEFAULT_IMAGELIST = to_absolute_path(DEFAULT_IMAGELIST)

DEFAULT_IMAGELIST_ONE = DEFAULT_IMAGELIST[:1]
DEFAULT_IMAGELIST_TWO = DEFAULT_IMAGELIST[:2]
DEFAULT_IMAGELIST_THREE = DEFAULT_IMAGELIST[:3]
PROFILE_IMAGE = DEFAULT_IMAGELIST[3:]