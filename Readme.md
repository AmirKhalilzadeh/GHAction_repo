
This is an interim repo that uses Github API to provide an initial analysis of the verbosity of existing notebooks (~1.4k repos) within the school Github account. The test workflow has been implemented in a separate private repository.

### Importance of Communication in Data Pipelines

One of the core principles we emphasize to our learners when building data pipelines is the importance of *communication*. This not only refers to interpersonal skills but also to the ability to communicate technical details clearly and effectively to stakeholders. Learners should be able to articulate their assumptions and decisions for each task and present their findings in a concise, structured manner after completing the task.

For example, we often reject solution notebooks that consist solely of code, with no explanations or context. Code alone doesn't provide sufficient insight into the thought process behind decisions, which is a critical component of effective communication.

### Automating Documentation Checks with GitHub Actions?

To improve this aspect of the learning process, implementation of a GitHub Action that checks if notebooks contain sufficient markdown cells with explanatory content is suggested. If a learner submits a poorly documented notebook, they will receive a warning, encouraging them to add more context and explanations to their work. This system will ensure that learners consistently improve not only their coding skills but also their ability to communicate technical information effectively.

