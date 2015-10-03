
#from modules.importer import my_func
from .importer import my_func
# from . import x
# from ..importer import x
# and so on

__all__ = [my_func]

# "Define all exceptions in one dedicated module"
# Supposedly relative imports are all the rage
