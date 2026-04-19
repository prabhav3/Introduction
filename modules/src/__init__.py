"""
When Python sees a folder with __init__.py, it treats that folder as a package (importable module namespace). And whatever code you put inside __init__.py can control what happens when the package is imported.
"""

from .core import gcf, lcm

__all__ = ["gcf", "lcm"]
__version__ = "0.1.0"

