# UV Demo

This repo was set up for a live-demo to accompany a talk using these slides. Here are the rough steps to go through to follow along with or recreate the demo.

## Prerequisites

Ensure that `uv` is installed on your computer (check with `which uv` and `which uvx` should both return valid paths). Ideally install with `curl -LsSf https://astral.sh/uv/install.sh | sh`. Otherwise use `brew install uv` or `pipx install uv`.

## 1. Repo Initialization

1. `uv init --lib --python=3.12 demo-project`
    * This creates `demo-project` folder with `src/demo_project`, `pyproject.toml`, `.python-version`, and `README.md` files with standards-compliant setup.
2. `cd demo-project`, then `uv sync` to create virtual environment (`.venv`) and `uv.lock`

Variant to try out:

* `uv init --app demo-project`
    * Creates `main.py` instead of `src` directory and no build setup in `pyproject.toml`

## 2. Start developing in a notebook

1. `cd demo-project`, add `notebooks` folder and create `01_start.ipynb` notebook
2. Note that `ipykernel` is required to run the notebook with the `.venv` environment. Install with `uv add --group dev ipykernel`, not the `Install` button on the popup if using VSCode.
    * Adds `ipykernel` to a `dev` dependency group in `pyproject.toml`
    * Updates `uv.lock`
    * Installs `ipykernel` to `.venv` using version in `uv.lock`
3. `uv add plotly[express] httpx pandas`
    * Adds those dependencies to required dependencies in `pyproject.toml`
    * Updates `uv.lock`
    * Installs `plotly`, `httpx`, and `polars` using version from `uv.lock`
4. Restart and run notebook. Note that `nbformat` is required, so run `uv add --group dev nbformat`

## 3. Move functions to library

1. Make `src/demo_project/data.py` and `src/demo_project/plots.py`
2. Copy functions into them
3. Add `02_use_lib.ipynb` file to `notebooks` and use functions from library to generate plot

## 4. Add Streamlit app

1. Add `app.py` with streamlit code to the library and `app.py` to root directory using that code
3. Run `uv add streamlit --optional streamlit`
4. Run `uv run streamlit run app.py`

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
