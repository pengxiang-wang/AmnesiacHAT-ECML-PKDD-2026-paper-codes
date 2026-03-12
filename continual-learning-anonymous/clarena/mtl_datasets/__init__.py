r"""

# Multi-Task Learning Datasets

This submodule provides the **multi-task learning datasets** that can be used in the package.

Here are the base classes for multi-task learning datasets, which inherit from Lightning `LightningDataModule`:

- `MTLDataset`: The base class for all multi-task learning datasets.
    - `MTLCombinedDataset`: The base class for combined multi-task learning datasets. A child class of `MTLDataset`.
    - `MTLDatasetFromCL`: The base class for constructing multi-task learning datasets from continual learning datasets. A child class of `MTLDataset`.

Please note that this is API documentation. External documentation links are omitted in the anonymous release:
`<ANONYMIZED_URL>`.



"""

from .base import MTLDataset, MTLCombinedDataset, MTLDatasetFromCL

from .combined import Combined


__all__ = ["MTLDataset", "MTLCombinedDataset", "MTLDatasetFromCL", "combined"]
