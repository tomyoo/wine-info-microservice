import os


def project_path(subpath=None):
    """
    Get the absolute path of the project

    :param subpath: A subpath within the project.  If omitted,
    return the project root
    """
    p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if subpath:
        if isinstance(subpath, str):
            subpath = (subpath,)
        parts = (p,) + tuple(subpath)
        p = os.path.sep.join(parts)
    return p
