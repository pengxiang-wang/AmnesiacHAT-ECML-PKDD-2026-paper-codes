r"""

# Single-Task Learning Algorithms

This submodule provides the **single-task learning algorithms** in the package.

Here are the base classes for STL algorithms, which inherit from PyTorch Lightning `LightningModule`:

- `STLAlgorithm`: the base class for all single-task learning algorithms.

Please note that this is API documentation. External documentation links are omitted in the anonymous release:
`<ANONYMIZED_URL>`.

"""

from .base import STLAlgorithm

from .single_learning import SingleLearning

__all__ = ["STLAlgorithm", "single_learning"]
