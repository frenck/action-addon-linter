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
    name: ✅ Add-on configuration
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

The JSON Schema is generated from the `src/config.schema.ts` file. If you make
changes to that file, you can update it using the following commands:

```bash
npx typescript-json-schema \
  --refs \
  --noExtraProps \
  --required \
  --uniqueNames \
  --defaultNumberType integer \
  ./src/config.schema.ts Config \
    > ./src/config.schema.json
```

And make the resulting file pretty:

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

Copyright (c) 2021 Franck Nijhof

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
[maintenance-shield]: https://img.shields.io/maintenance/yes/2021.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[releases-shield]: https://img.shields.io/github/release/frenck/action-addon-linter.svg
[releases]: https://github.com/frenck/action-addon-linter/releases
[semver]: http://semver.org/spec/v2.0.0.html
