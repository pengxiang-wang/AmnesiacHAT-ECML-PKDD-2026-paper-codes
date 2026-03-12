# Anonymous Reviewer Guide


Thank you for reviewing this paper! This archive contains two directories:

- **continual-learning-anonymous** - the anonymized source package.
- **continual-learning-research** - the experiment workspace, including configuration files, launch scripts, notebooks, and output artifacts.

Place both directories under the same parent directory before running anything.

## Installation

1. Open a terminal and change into the package ‘continual-learning-anonymous’ directory:

```bash
cd <ANONYMIZED_PACKAGE_DIR>/
```

2. Install the package:

```bash
pip install .
```

Python 3.12 or later is required. A dedicated conda environment is recommended because the dependency set is relatively large.

## Running the Anonymous Experiment Bundle

1. Change into the experiment workspace:

```bash
cd ../continual-learning-research/
```

2. Launch the anonymized experiment bundle:

```bash
bash scripts/amnesiachat_paper/full.sh
```

This entry script dispatches the remaining scripts in the `scripts/amnesiachat_paper` directory, including:

1. Main-study scripts, named `main_study_xxx.sh`, where `xxx` denotes the benchmark setting name.
2. The ablation-study script `ablation_study_pmnist_5tasks_til.sh`.
3. The hyperparameter-study script `hyperparameter_study.sh`.

## Running Custom Experiments

- Custom configurations can be added or modified under `continual-learning-research/configs/`.
- Each YAML file under `continual-learning-research/configs/index/` corresponds to one experiment entry.
- Use the anonymized command-line entry point to launch an experiment. For example:

```bash
clarena pipeline=CUL_FULL_EXPR index=<ANONYMIZED_INDEX_PATH>
```

## Results

After an experiment finishes, all generated outputs are written under `continual-learning-research/outputs/`.
