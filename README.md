# A pre-commit hook for Angular-Cli test

This is the Angular-Cli test ([ng test](https://angular.io/cli/test)) hook for [pre-commit](https://pre-commit.com). This hook will prevent git commits if ng test does not pass.

## Usage

- Install pre-commit (see links below).
- Create a pre-commit config file (`.pre-commit-config.yaml`).
- Run `pre-commit install` from the root of your project.

Finally add this to your `.pre-commit-config.yaml`:

```yaml
    -   repo: git://github.com/dwightgunning/pre-commit-ngtest/
        sha: ''  # Use the sha or tag (e.g. 'stable') you want to point at
        hooks:
        -   id: ngtest
```

When making a commit, the hook will run `ng test` on the staged files and if errors or warnings are raised, the commit will be blocked.

## Caveats

If `args` are provided in the pre-commit configuration, the final element must be '--' in order to distinguish between `ng test` options and the filenames to be tested.

By default, pre-commit-ngtest makes use of the "--files" argument on `ng test` so that only files staged for commit are passed through `ng test`. This keeps the tester runtime to a minimum.

Unfortunately, the combination of Angular-cli's support for multiple 'projects' (e.g. 'src' and 'e2e') and the "--files" argument on `ng test` can cause errors indicating that a particular file is not part of a given project. This can be worked-around by being more explicit in setting the 'excludes' property on the 'test' project configuration (`angular.json`). This can be tedious but keeps the commit times to a minimum.

## Links
- For pre-commit: see https://github.com/pre-commit/pre-commit
- For ng test: https://angular.io/cli/test

## Copyright and License Information

Copyright (c) 2019 Dwight Gunning, and individual contributors. All rights reserved.

See the file "LICENSE" for information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.
