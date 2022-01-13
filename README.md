# 🚀 Frenck's Github Action: Home Assistant Add-on Linter

[![GitHub Release][releases-shield]][releases]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)

[![Sponsor Frenck via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

🚀 Frenck's GitHub Action for linting Home Assistant Add-ons.

## About

This GitHub Action is able to validate/lint Home Assistant Add-on configuration
files.

Besides checking for validity of add-on configuration files, it will
also warn for default configurations that can be removed and cleaned up.

## Usage

```yaml
name: Lint
on: [push, pull_request]
jobs:
  build:
    name: Add-on configuration
    runs-on: ubuntu-latest
    steps:
      - name: ⤵️ Check out code from GitHub
        uses: actions/checkout@v2
      - name: 🚀 Run Home Assistant Add-on Lint
        uses: frenck/action-addon-linter@v1
        with:
          path: "./addon"
```

## Arguments

|    Input    |                             Description                             |    Usage     |
| :---------: | :-----------------------------------------------------------------: | :----------: |
|   `path`    |     Path to the folder containing the add-on config.json file.      | **Required** |
| `community` | Enable Home Assistant Community Add-ons mode, with specific checks. |  _Optional_  |

## Updating the JSON Schema

For the larger part, JSON Schemas are used to validate the configuration files.
The schema files for both the add-on `config.json` and `build.json` can be found
in the `src/` folder.

- `src/config.schema.json` is used to validate `config.json`
- `src/build.schema.json` is used to validate `build.json`

If you adjust the schema, please make sure they are pretty:

```bash
npx prettier --write ./src/config.schema.json
```

## Changelog & Releases

This repository keeps a change log using [GitHub's releases][releases]
functionality.

Releases are based on [Semantic Versioning][semver], and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## Versions & Updating

You can specify which version of this GitHub Action your workflow should use.
And even allowing for using the latest major or minor version.

For example; this will use release `v1.1.1` of a GitHub Action:

```yaml
- name: 🚀 Run Home Assistant Add-on Lint
  uses: frenck/action-addon-linter@v1.1.1
```

While the following example, will use the `v1.1.x` minor release, for example
if `v1.1.2` is the latest releases (starting with `v1.1`), this will run
`v1.1.2`:

```yaml
- name: 🚀 Run Home Assistant Add-on Lint
  uses: frenck/action-addon-linter@v1.1
```

As in the examples throughout the documentation, the following example is
locked on major version, meaning any `v1.x.x` latest version will be used,
as long as it is version 1.

```yaml
- name: 🚀 Run Home Assistant Add-on Lint
  uses: frenck/action-addon-linter@v1
```

### Automatically update using Dependabot

The advantage of locking against a more specific version, is that it prevents
surprises if an issue or breaking changes were introduced in a newer release.

The disadvantage of being more specific, is that it requires you to keep things
up to date. Fortunately, GitHub has a tool for that, called: Dependabot.

Dependabot can automatically open a pull request on your repository to update
this Action for you. You can instantly see if the new version works (as the
pull request shows the success or failure status) and you can decide to
merge it in by hitting the merge button. Quick, easy and always up2date.

To enable Dependabot, create a file called `.github/dependabot.yaml`:

```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: daily
```

Your all set! Dependabot will now check (and update) your GitHub actions
every day. 🤩

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Authors & contributors

The original setup of this repository is by [Franck Nijhof][frenck].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## License

MIT License

Copyright (c) 2021-2022 Franck Nijhof

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[contributors]: https://github.com/frenck/action-addon-linter/graphs/contributors
[frenck]: https://github.com/frenck
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[license-shield]: https://img.shields.io/github/license/frenck/action-addon-linter.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2022.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[releases-shield]: https://img.shields.io/github/release/frenck/action-addon-linter.svg
[releases]: https://github.com/frenck/action-addon-linter/releases
[semver]: http://semver.org/spec/v2.0.0.html
