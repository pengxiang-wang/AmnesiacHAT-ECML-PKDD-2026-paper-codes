r"""

# Continual Learning Regularizers

This submodule provides the **regularizers** which are added to the loss function of corresponding continual learning algorithms. It can promote forgetting preventing which is the major mechanism in regularization-based approaches, or for other purposes.

The regularizers inherit from `nn.Module`.

Please note that this is API documentation. External documentation links are omitted in the anonymous release:
`<ANONYMIZED_URL>`.



"""

from .distillation import DistillationReg
from .hat_mask_sparsity import HATMaskSparsityReg
from .parameter_change import ParameterChangeReg

__all__ = ["distillation", "hat_mask_sparsity", "parameter_change"]
