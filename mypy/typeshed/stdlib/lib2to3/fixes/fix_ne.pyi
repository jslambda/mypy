from typing import ClassVar
from typing_extensions import Literal

from .. import fixer_base

class FixNe(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[False]]
    def match(self, node): ...
    def transform(self, node, results): ...
