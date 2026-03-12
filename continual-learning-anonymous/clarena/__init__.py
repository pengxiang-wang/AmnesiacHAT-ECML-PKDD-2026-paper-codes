r"""

# Anonymous Continual Learning Package

This is an anonymized Python package designed for **Continual Learning (CL)**
research. It provides an integrated environment with extensive APIs for
conducting CL experiments, along with pre-implemented algorithms and datasets.
This package also supports **Continual Unlearning (CUL)**,
**Multi-Task Learning (MTL)** and **Single-Task Learning (STL)**.

External documentation links are omitted in the anonymous release:
`<ANONYMIZED_URL>`.

The package provides the following submodules:

- `pipelines`: Pre-defined experiment and evaluation pipelines for different paradigms.
- `cl_datasets`: Continual learning datasets.
- `mtl_datasets`: Multi-task learning datasets.
- `stl_datasets`: Single-task learning datasets.
- `backbones`: Neural network architectures used as backbones networks.
- `heads`: Output heads.
- `cl_algorithms`: Continual learning algorithms.
- `cul_algorithms`: Continual unlearning algorithms.
- `mtl_algorithms`: Multi-task learning algorithms.
- `stl_algorithms`: Single-task learning algorithms.
- `metrics`: Metrics for evaluation.
- `callbacks`: Extra actions added to the pipelines.
- `utils`: Utilities for the package.
"""

__all__ = [
    "pipelines",
    "cl_datasets",
    "mtl_datasets",
    "stl_datasets",
    "backbones",
    "heads",
    "cl_algorithms",
    "cul_algorithms",
    "mtl_algorithms",
    "stl_algorithms",
    "metrics",
    "callbacks",
    "utils",
]
