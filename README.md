# Creative approaches to problem solving[$^1$](https://qz.com/192071/how-one-college-went-from-10-female-computer-science-majors-to-40/) in neuroscience using Python

## Introduction to (Scientific) Progamming

### featuring Neurons and Maths

by [Christopher Brian Currin](https://chriscurrin.com)

A _functional approach_ to learning code. _Why-based_ in contrast to _fact-based_.

![Cape Town](https://images.unsplash.com/photo-1563656157432-67560011e209?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=900&h=300&q=80)

## Setup

### Install Python

1. Download MambaForge from <https://github.com/conda-forge/miniforge#mambaforge>
2. Create an environment

   ```bash
   conda create -n imbizo python
   ```

3. Install dependencies

   ```bash
   pip install matplotlib seaborn numpy pandas jupyter
   ```

   or

   ```bash
   pip install -r requirements.txt
   ```

### Colab

1. <https://colab.research.google.com/github/ChrisCurrin/imbizo_2024_problem_solving/blob/main/1%20-%20the%20neuron.ipynb>
2. <https://colab.research.google.com/github/ChrisCurrin/imbizo_2024_problem_solving/blob/main/2%20-%20debugging.ipynb>
3. <https://colab.research.google.com/github/ChrisCurrin/imbizo_2024_problem_solving/blob/main/3%20-%20synapses.ipynb>
4. <https://colab.research.google.com/github/ChrisCurrin/imbizo_2024_problem_solving/blob/main/4%20-%20analysis.ipynb>
5. <https://colab.research.google.com/github/ChrisCurrin/imbizo_2024_problem_solving/blob/main/5%20-%20simulator.ipynb>

## General

Coding is *just* problem-solving using a formal language (in this case python) to convert instructions we give into some form of processing.
Most of programming is figuring out which instructions are possible/allowed (aka the **syntax**) and which are appropriate for your problem (aka the **semantics**) - just because something compiles (no syntax errors) does not mean it is correct in solving the problem (or the best way to solve a problem).

> "A compiler or interpreter could complain about syntax errors. Your co-workers will complain about semantics."

- [Test often. Test well](https://en.wikipedia.org/wiki/Test-driven_development).
- Read and contribute to [The role of scientific code: How can we write better code](https://docs.google.com/document/d/11NcnnCllrHD19EpHc2wSjdD_5mimqClDkdmweZkOPrk/edit), i.e. use our laboratory more effectively?
- [The Zen of Python](https://peps.python.org/pep-0020/)
- Use a good file structure (https://drivendata.github.io/cookiecutter-data-science)

## Coding

### Style

#### Docstrings

We recommy Numpy style docstrings. See <https://numpydoc.readthedocs.io/en/latest/format.html> for more details.

```python
def function(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    Raises
    ------
    LinAlgException
        If the matrix is not numerically invertible.

    See Also
    --------
    package.module.submodule.func_a :
        A somewhat long description of the function.

    Notes
    -----
    The FFT is a fast implementation of the discrete Fourier transform:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    Examples
    --------
    np.add(1, 2)
    3

    Comment explaining the second example.

    np.add([1, 2], [3, 4])
    array([4, 6])

    """
    return True
```

> if your docstring is longer than your code, that's a good sign!

For other docstring styles see <https://stackoverflow.com/a/24385103/5209000>

#### Formatting

We use `black` and `isort` for formatting.

#### Linting

We use `flake8` for linting.

#### Testing

We use `pytest` and `coverage` for testing.

#### Continuous Integration

We use [GitHub Actions](https://docs.github.com/en/actions) for continuous integration. The <https://github.com/rochacbruno/python-project-template> repo has a good example of how to set this up. However, most good CI systems require a public repo.

#### Setup Style

> the default python project template has these setup already but you can add them to any project by following the instructions below.

##### [Option 1] Install dependencies with a file

1. copy <https://github.com/rochacbruno/python-project-template/blob/main/requirements-test.txt> to your project

2. install the dependencies

    ```bash
    pip install -r requirements-test.txt
    ```

##### [Option 2] Install dependencies with a script

```bash
pip install pytest coverage flake8 black isort pytest-cov codecov mypy gitchangelog mkdocs
```

## Repository hygiene

Most of the time, you will be working on your own projects. However, sometimes you will need to collaborate with others. This section outlines some best practices for managing your code and projects. These are not hard rules, but they are good guidelines to follow.

### Selective commits

Try commit in blocks of related features.

```bash
git add file1.py file2.py
git commit -m "feat: add logging to file1.py and file2.py"
```

If you have made changes to multiple files, but they are not related, you can commit them separately.

```bash
git add file1.py
git commit -m "feat: add logging"

git add file2.py
git commit -m "fix: remove zero division"
```

#### Line changes (aka hunks)

If you have made changes to multiple lines in a file, but they are not related, you can commit them separately.

```bash
git add file1.py -p
git commit -m "feat: add logging"

git add file1.py -p
git commit -m "feat: add ability to multiply"
```

(`-p` is short for `--patch`)

this will allow you to select which lines to add to the commit

```git
...
(1/11) Stage this hunk [y,n,q,a,d,j,J,g,/,s,e,?]? ?
? - print help
...
```

> !!! The easiest way to do this is with an IDE!

### Commit often

Try to commit often. This makes it easier to roll back changes, and to collaborate with others.

How often is often? That depends on the project. For a small project, you might commit every time you add a new feature. For a large project, you might commit every time you add a new function.

Rule of thumb: if you are about to make a change that you might want to undo later, commit first.

Good default: commit every time you finish a coding session.

Moving between computers: commit before you push. Prefix the commit message with `wip:` (work in progress). This will make it easier to find the commit later.

### Commit messages

Commit messages should be short and descriptive. Use the imperative, present tense (e.g. "add", "change", "fix", "remove") to describe what the commit does, rather than what it did or what it will do.

It is a good idea to use **[conventional commits](https://www.conventionalcommits.org/)**, a concept similar to [semantic versioning](https://semver.org). This allows for automatic changelog generation, and easy release notes, and makes it easier for people to contribute to your projects by allowing them to explore a **more structured commit history**.

```markdown
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

the short example is:

```bash
git commit -m "feat: add logging to function"
```

recommended `type`s are:

- `feat`: a new feature
- `fix`: a bug fix
- `docs`: documentation only changes
- `style`: changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: a code change that neither fixes a bug nor adds a feature
- `perf`: a code change that improves performance
- `test`: adding missing or correcting existing tests
- `build`: changes that affect the build system or external dependencies (example scopes: pip, make, npm)
- `ci`: changes to our CI configuration files and scripts (example scopes: GitHub Actions, Travis, Circle, BrowserStack, SauceLabs)
- `chore`: other changes that don't modify src or test files
- `revert`: revert a previous commit

### Branches

Branches should be named according to their feature. Use dashes to separate words. A preceding `feature/` or `bugfix/` is recommended.

Examples:

- `add-logging`
- `feature/add-logging`
- `bugfix/fix-logging`

```bash
git checkout main
git checkout -b feature-branch
```

For simple projects, the [GitHub Flow](https://guides.github.com/introduction/flow/) branching model is recommended.

For advanced branching, see the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) branching model.

In general, it is okay to branch off `main` for small projects. For larger projects, it is recommended to branch off `develop` and then merge into `develop` and then `main` when ready. See the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) branching model for more details.

Merge branches with a merge commit. This allows for a clean history and easy reverting of changes. Delete the branch after merging for cleaner branches.

```bash
git checkout main
git merge --no-ff feature-branch
git branch -d feature-branch
```

#### Rebase vs merge

[**Advanced**]

Use `merge` for merging branches. This is the default and easiest method. Your commit history is a **record of what actually happened**.

Use `rebase` when you want to move the base of your branch to the latest commit. This is useful for updating your branch with the latest changes from `main`. This is also useful for cleaning up your branch before merging, makes the history cleaner, and putting the onus of merging on the `feature-branch` developer rather than the `main` maintainer. Your commit history is a **story of how your project was made** (not the time-order of what happened).

```bash
git checkout feature-branch
git fetch && git rebase origin/main
```

You may need to `git push --force-with-lease` your `feature-branch` after rebasing.

```bash
git checkout main
git merge --no-ff feature-branch
git branch -d feature-branch
```

**The golden rule of git rebase is to never use it on public branches like `main`**.

> This is a more advanced topic. If you are not sure, use `merge`.

For more, see <https://www.atlassian.com/git/tutorials/merging-vs-rebasing> and <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>.

#### Squash

[**Advanced**]

Use `squash` to combine multiple commits into a single commit. This is useful for cleaning up your branch before merging.

1. if you decide to squash before merging, then all of those individual commits from your feature branch will be combined into a single commit. The main commit history, therefore, will only show a single commit for this integration.
1. if you decide AGAINST squashing, all of your individual commits will be preserved as such.

There are pros and cons to both approaches, so it's mostly a matter of preference and convention.

#### Pull vs fetch

Use `fetch` to update your local copy of the remote repository. This will not change your local files.

Use `pull` to update your local copy of the remote repository and merge the changes into your local branch. This will change your local files.

```bash
git fetch
git pull
```

### Conflict resolution

Secnarion: you’ve made changes on your local copy and the GitHub version. i.e. there are conflicts if you try pull or merge.

Resolve conflicts by deciding whether to keep `HEAD` (current state) or `main` (an example of an incoming state, could be another branch).

    ```
    <<<<<<< HEAD
    what you have
    =======
    what you are pulling
    >>>>>>> main
    ```

If pulling (i.e. not using a branch, but conflicts between HEAD and remote):

1. If you have changes you don't want to commit before starting a merge

   ```bash
    git stash
    git pull
    git stash pop
    ```

2. There are different changes on both the remote and the local branch

    ```bash
     git pull [--rebase]
     ```

    where `--rebase` is optional (see [rebase vs merge](#rebase-vs-merge) above).

> if things have gone wrong, you can always `git merge --abort` to go back to the state before the merge (all files intact).

## Collaborate

### Code review

Code review is an important part of the development process. It allows for discussion and feedback on code changes before they are merged into the main branch.

### Forks

Forks are useful for making changes to a repository that you do not have write access to. Forks can be used to make changes to a repository and then submit a pull request to the original repository.

### Pull requests

Pull requests should be used for all collaborative code changes. This allows for code review and discussion before merging.

Merge pull requests with a merge commit. Squashing is up to your personal preference(s). This allows for a clean history and easy reverting of changes. Delete the branch after merging for cleaner branches.

### Issues

Issues should be used to track bugs, feature requests, and other tasks. Issues can be linked to pull requests and commits to track progress (e.g. `"fixes #13"` in the pull request title or description). See <https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue> for more details.

The `python-project-template` repo has some templates for issues and pull requests already.

Assign issues to yourself when you start working on them. This allows others to see who is working on what.

## Publish

### Citations

Once an article is published, the associated code should be made available online for all to see.

By default (and the easiest route) is to make the repo public by going to the settings of the repo and selecting `Public`. This will make the repo available to everyone.

The alternative (e.g. if you want to keep working on the code in private but release parts or the current version as public) is to create a **new** repo in your lab's GitHub organisation and make it public.

### Releases and versioning

Once a paper is published, the code should be released with a version number. This is done by creating a [release](https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository) in the repo.

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=appveyor)](https://opensource.org/licenses/MIT)

Projects should generally licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Some projects may have their own license, please check the individual project for details.

#### Creating a license

The easiest way to **create** a license is to go to your GitHub repo and click `Add File` > `Create new file`. Then name it LICENSE and select the `Choose a license template` ocne it appears.

The easiest way to **choose** a license is to use the [GitHub license generator](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository). See also <https://choosealicense.com/>.

![creating a license](https://docs.github.com/assets/cb-18542/mw-1440/images/help/repository/license-tool.webp)

#### The MIT license is a simple permissive license that only requires preservation of copyright

A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

- Permissions
  - Commercial use
  - Modification
  - Distribution
  - Private use
- Limitations
  - Liability
  - Warranty
- Conditions
  - License and copyright notice

#### Apache License 2.0 is also a permissive license, but it also includes a patent grant

A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code.

- Permissions
  - Commercial use
  - Modification
  - Distribution
  - Patent use
  - Private use
- Limitations
  - Trademark use
  - Liability
  - Warranty
- Conditions
  - License and copyright notice
  - State changes

#### GNU GPL v3 is a strong copyleft license that requires derived works to be licensed under the same terms

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

- Permissions
  - Commercial use
  - Modification
  - Distribution
  - Patent use
  - Private use
- Limitations
  - Liability
  - Warranty
- Conditions
  - License and copyright notice
  - State changes
  - Disclose source
  - Same license

## Authors

- **[Christopher Brian Currin](https://chriscurrin.com)**
