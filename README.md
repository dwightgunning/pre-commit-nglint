# A pre-commit hook for Angular-Cli Lint

This is the Angular-Cli lint ([ng lint](https://angular.io/cli/lint)) hook for [pre-commit](https://pre-commit.com). This hook will prevent git commits if ng lint does not pass.

## Usage

- To use this you first need to install pre-commit(see links below).
- Then create a pre-commit config file.
- Run `pre-commit install` from the root of your project.

Finally add this to your `.pre-commit-config.yaml`:

```yaml
    -   repo: git://github.com/dwightgunning/pre-commit-nglint/
        sha: ''  # Use the sha or tag (e.g. 'stable') you want to point at
        hooks:
        -   id: nglint
```

When making a commit, the hook will run `ng lint` on the project and block the commit.

## Links
- For pre-commit: see https://github.com/pre-commit/pre-commit
- For ng lint: https://angular.io/cli/lint

## Copyright and License Information

Copyright (c) 2019 Dwight Gunning, and individual contributors. All rights reserved.

See the file "LICENSE" for information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.
