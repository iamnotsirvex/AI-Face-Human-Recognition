def parse_source(source: str):
    """Return int when source is a digit (camera index), else string as given."""
    if isinstance(source, str) and source.isdigit():
        return int(source)
    return source
