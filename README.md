# Python3.x seed-code
<<<<<<< bobuntu-readme

Starter boilerplate for python3.x projects complete with **git-hooks** that trigger
the linter to format the code before committing changes.

#### Project structure:

```bash
/.
├── <file>.py
├── LICENSE
├── pyproject.toml
└── README.md
└── .pre-commit-config.yaml
└── .pylintrc
└── setup.cfg
```

Starter boilerplate for python3.x projects complete with **git-hooks** that trigger
the linter to format the code before committing changes.

### CHANGELOG:
- [x] Using `pre-commit` git-hooks
- [x] ~Using **Black** is rigid, highly opinionated. Dismissed~
- [x] ~Same relative rigidity for `autopep8`, `flake8`, or any PEP8-compliant linter~
- [x] Linting with `yapf` and `pylint`
- [ ] Customize `.pylintrc` config

> Note: `<file>.py` file is for demo purposes. **It can safely be deleted**.

### Instructions

Clone this repo and rename the root folder to anything you want. Immediately start writing code.

To fully take advantage of what's in here, we recommend installing a few packages, and commit the folder to versioning with Git, as follows:

```bash
pip install -U pre-commit pylint yapf
git init
pre-commit install
git add .
git commit -m "Message"
```

Git hooks are a great way to perform last-minute checks before committing changes. They automatically block the commit process in order to do a few things as pre-determined by you. For starters this boilerplate simply lints all staged python files.

### LICENSE

See `./LICENSE` file.
