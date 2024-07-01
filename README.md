# HumanEval Test Bench / Test Bed

This repository contains tests for evaluating code completions using the HumanEval dataset with 2501. Here's an overview of the key files and directories:

## Results

- random10 : 1.0 pass@1
- large70 : 1.0 pass@1
- full163 : 0.96951 pass@1


## Files

### random10.jsonl

This file contains a set of 10 programming tasks from the HumanEval dataset, selected on an evenly distributed set of tasks selected randomly, including task descriptions and function signatures but without solutions. Each task is identified by a unique `task_id`, and the file is in JSON Lines format, which means each line is a complete JSON object representing a single task.

### random10-completion.jsonl

This is the file containing proposed solutions (completions) for the programming tasks listed in `random10.jsonl`. The completions are generated algorithms or functions written in Python that aim to solve the tasks described in `random10.jsonl`. Each completion is associated with a `task_id` to match the tasks.

### random10-completion.jsonl_results.jsonl

This file holds the results of evaluating the completions in `random10-completion.jsonl`. Each line in this JSON Lines file corresponds to the evaluation of a single completion, including metrics like pass rate, error rate, and execution time. The `task_id` is also included to map the results back to the original tasks and completions.

### full163-completion.jsonl

This file contains a comprehensive set of 163 programming tasks from the HumanEval dataset, including task descriptions and function signatures but without solutions. Each task is identified by a unique `task_id`, and the file is in JSON Lines format.

### full163-completion.jsonl_results.jsonl

This file holds the results of evaluating the completions in `full163-completion.jsonl`. Each line in this JSON Lines file corresponds to the evaluation of a single completion, including metrics like pass rate, error rate, and execution time. The `task_id` is also included to map the results back to the original tasks and completions.

## Folders

### random10_scripts
This folder contains a set of 10 programming tasks from the HumanEval dataset. These tasks provide a comprehensive evaluation of 2501 code generation on an evenly distributed set of tasks selected randomly.

### large70_scripts

This folder holds an even larger set of programming tasks, allowing for extensive testing of code completion capabilities across a wide range of problems.

### full163_scripts

This folder contains the complete set of 163 programming tasks from the HumanEval dataset. It provides the most comprehensive evaluation of code generation capabilities across a wide variety of problems.

## Usage

We use the [OpenAI HumanEval library](https://github.com/openai/human-eval) to evaluate our performances

Ex: 
```evaluate_functional_correctness full163-completion.jsonl --problem_file=HumanEval.jsonl```

## Contact
hello@2501.ai