# HumanEval Test Bench / Test Bed

This repository contains tests for evaluating code completions using the HumanEval dataset with 2501. Here's an overview of the key files and directories:

## Files

### random10.jsonl

This file contains a set of 10 programming tasks from the HumanEval dataset, selected on an evenly distributed set of tasks selected randomly, including task descriptions and function signatures but without solutions. Each task is identified by a unique `task_id`, and the file is in JSON Lines format, which means each line is a complete JSON object representing a single task.

### random10-completion.jsonl

This is the file containing proposed solutions (completions) for the programming tasks listed in `random10.jsonl`. The completions are generated algorithms or functions written in Python that aim to solve the tasks described in `random10.jsonl`. Each completion is associated with a `task_id` to match the tasks.

### random10-completion.jsonl_results.jsonl

This file holds the results of evaluating the completions in `random10-completion.jsonl`. Each line in this JSON Lines file corresponds to the evaluation of a single completion, including metrics like pass rate, error rate, and execution time. The `task_id` is also included to map the results back to the original tasks and completions.

## Folders

### random10_scripts
This folder contains a set of 10 programming tasks from the HumanEval dataset. These tasks provide a comprehensive evaluation of 2501 code generation on an evenly distributed set of tasks selected randomly.

### large70_scripts

This folder holds an even larger set of programming tasks, allowing for extensive testing of code completion capabilities across a wide range of problems.

## Usage

To use the test bench and submit your code completions for evaluation, follow these steps:

1. Review the programming tasks in `random10.jsonl` to understand the problems that need to be solved.

2. Generate completions (solutions) for the tasks and save them in `random10-completion.jsonl`. Each completion should be associated with the corresponding `task_id`.

3. Submit your `random10-completion.jsonl` file to the HumanEval evaluation script. The script will execute your completions against the test cases and generate results in `random10-completion.jsonl_results.jsonl`.

4. Analyze the results in `random10-completion.jsonl_results.jsonl` to determine the performance of your code generation model. Key metrics to consider include pass rate, error rate, and execution time.

For a more comprehensive evaluation, you can use the larger sets of programming tasks provided in the `random70_scripts` and `large70_scripts` folders. These datasets offer a greater variety and complexity of problems to test the capabilities of your code generation model.

To submit your completions for the larger datasets, follow the same process as described above, but use the corresponding `.jsonl` files in the respective folders.

The HumanEval evaluation script will run your submitted completions against the predefined test cases and generate detailed results, allowing you to assess the performance and effectiveness of your code generation approach.