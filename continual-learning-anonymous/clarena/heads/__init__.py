r"""

# Output Heads

This submodule provides the **output heads** in the package.

There are two types of continual learning / unlearning heads in the package:
`HeadsTIL`, `HeadsCIL` and `HeadDIL`, corresponding to three CL paradigms
respectively: Task-Incremental Learning (TIL), Class-Incremental Learning (CIL)
and Domain-Incremental Learning (DIL). For Multi-Task Learning (MTL), the
package provides `HeadsMTL`, which is a collection of independent heads for each
task.

Please note that this is API documentation. External documentation links are omitted in the anonymous release:
`<ANONYMIZED_URL>`.

"""

from .heads_cil import HeadsCIL
from .head_dil import HeadDIL
from .heads_til import HeadsTIL

from .heads_mtl import HeadsMTL

from .head_stl import HeadSTL

__all__ = ["HeadsTIL", "HeadsCIL", "HeadDIL", "HeadsMTL", "HeadSTL"]
