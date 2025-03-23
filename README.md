# UV Demo

## Sales Pitch

- Replaces a bunch of dev tooling
  - venv/virtualenv
  - pip
  - pipx
  - pip-compile/pip-sync
  - poetry
- Manages installation of python itself
- Lightning fast
- Workflow similar to poetry but better in almost every way

## Replacing poetry

### Managing Dependencies

- uv init
  - uv init --python=3.10
  - uv init --app uv-demo-init-app
  - uv init --lib uv-demo-init-lib
    - Makes src/ directory for library content
  - uv init --script my_script.py
    - uv add polars --script my_script.py
      - adds dependencies to commented config at top of script
    - uv lock --script my_script.py
      - creates my_script.py.lock file
- uv run
  - cd uv-demo-add-remove
  - uv run main.py
    - Installs project automatically before running the file, which
      - Installs compliant python version if necessary
      - Updates uv.lock if necessary
      - Creates ./.venv if necessary
      - Installs packages if necessary
- uv add/remove
  - Uncomment streamlit stuff in main.py
  - `uv run main.py` fails because streamlit isn't added as dependency
  - Run `uv add streamlit`. This adds streamlit to pyproject.toml, updates uv.lock, and installs new packages into `.venv`
  - Now `uv run main.py` works

### Building and Publishing Packages

- uv build / uv publish

### Managing Dev Env

- uv sync
- uv run

## Replacing pipx

- `uv tool install textual-demo` is similar to `pipx install textual-demo`. Installs to `~/.local/bin/textual-demo`
- `uvx textual-demo` downloads (or uses cache) and runs textual-demo without installing executable in `~/.local/bin`
  - same as `uv tool install textual-demo
  - uvx --with textual-demo textual-demo

## Replacing venv and pip

- uv venv
  - uv venv --python=3.11
- Then uv pip install
  - Once there's a .venv directory, no need to activate it

## Replacing pip-compile

- If just wanting to use pip-compile, use `uv pip compile` as a drop-in replacement that's way faster
- uv pip compile requirements.in -o requirements.txt  
- uv pip sync requirements.txt
