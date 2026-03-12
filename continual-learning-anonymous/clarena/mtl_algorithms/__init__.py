r"""

# Multi-Task Learning Algorithms

This submodule provides the **multi-task learning algorithms** in the package.

Here are the base classes for MTL algorithms, which inherit from PyTorch Lightning `LightningModule`:

- `MTLAlgorithm`: the base class for all multi-task learning algorithms.


Please note that this is API documentation. External documentation links are omitted in the anonymous release:
`<ANONYMIZED_URL>`.

"""

from .base import MTLAlgorithm

from .joint_learning import JointLearning

__all__ = ["MTLAlgorithm", "joint_learning"]
