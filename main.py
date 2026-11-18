"""Emit the pre-built front page image for news-image-20261117.

The newspaper front page itself lives in entry.png next to this file.
This program only carries those exact bytes to /output/entry.png,
checking size and PNG magic first so a corrupt input fails loudly
instead of producing a broken submission. Nothing is generated or
re-encoded here: the PNG is the entry, byte for byte.
"""

import hashlib
import os
import sys

SOURCE_NAME = "entry.png"
DEST_DIR = "/output"
DEST_NAME = "entry.png"
MAX_BYTES = 1_048_576  # 1 MiB submission ceiling
MIN_BYTES = 1024  # a real 1024x1024 front page is far bigger than this
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def load_image(path):
    with open(path, "rb") as handle:
        data = handle.read()
    if not data:
        raise ValueError("entry.png is empty")
    if len(data) < MIN_BYTES:
        raise ValueError("entry.png is only %d bytes, too small to be the front page" % len(data))
    if len(data) > MAX_BYTES:
        raise ValueError("entry.png is %d bytes, over the 1 MiB limit" % len(data))
    if data[:8] != PNG_MAGIC:
        raise ValueError("entry.png does not start with PNG magic bytes")
    return data


def write_output(data):
    os.makedirs(DEST_DIR, exist_ok=True)
    dest = os.path.join(DEST_DIR, DEST_NAME)
    with open(dest, "wb") as handle:
        handle.write(data)
    return dest


def main():
    data = load_image(source_path())
    dest = write_output(data)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (dest, len(data), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
