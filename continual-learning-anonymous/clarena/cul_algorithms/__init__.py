r"""

# Continual Unlearning Algorithms

This submodule provides the **continual unlearning algorithms** in the package.

Here are the base classes for CUL algorithms:

- `CULAlgorithm`: the base class for all continual unlearning algorithms.
    - `AmnesiacCULAlgorithm`: the base class for Amnesiac continual unlearning algorithms.

Please note that this is API documentation. External documentation links are omitted in the anonymous release:
`<ANONYMIZED_URL>`.



"""

from .base import CULAlgorithm, AmnesiacCULAlgorithm
from .independent_unlearn import IndependentUnlearn

from .finetuning_unlearn import AmnesiacFinetuningUnlearn
from .lwf_unlearn import AmnesiacLwFUnlearn
from .ewc_unlearn import AmnesiacEWCUnlearn
from .der_unlearn import AmnesiacDERUnlearn, AmnesiacDERppUnlearn

from .clpu_derpp_unlearn import CLPUDERppUnlearn
from .amnesiac_hat_unlearn import AmnesiacHATUnlearn

__all__ = [
    "CULAlgorithm",
    "AmnesiacCULAlgorithm",
    "independent_unlearn",
    "finetuning_unlearn",
    "lwf_unlearn",
    "ewc_unlearn",
    "der_unlearn",
    "clpu_derpp_unlearn",
    "amnesiac_hat_unlearn",
]
