# UV Demo

This repo was set up for a live-demo to accompany a talk using these slides. Here are the rough steps to go through to follow along with or recreate the demo.

## Prerequisites

Ensure that `uv` is installed on your computer (check with `which uv` and `which uvx` should both return valid paths). Ideally install with `curl -LsSf https://astral.sh/uv/install.sh | sh`. Otherwise use `brew install uv` or `pipx install uv`.

## 1. Repo Initialization

1. `uv init --lib --python=3.12`
    * This creates a `src/uv_demo` directory and `pyproject.toml`, `.python-version`, and `README.md` files with standards-compliant setup.
2. `uv sync` to create virtual environment (`.venv`) and `uv.lock`

Variant to try out:

* Outside of the `uv-demo` directory: `uv init --app demo-project`
    * Passing `demo-project` creates a new directory with that name to house the project files
    * Creates `main.py` instead of `src` directory and no build setup in `pyproject.toml`
* Managed scripts:
  * `uv init --script some_script.py`
  * `uv add --script some_script.py polars`
  * Copy content into script
  * Run with `uv run --no-project some_script.py`
  * Can also lock dependencies with `uv lock --script some_script.py`

## 2. Start developing in a notebook

1. Add `notebooks` folder and create `01_start.ipynb` notebook
2. Note that `ipykernel` is required to run the notebook with the `.venv` environment. Install with `uv add --group dev ipykernel`, not the `Install` button on the popup if using VSCode.
    * Adds `ipykernel` to a `dev` dependency group in `pyproject.toml`
    * Updates `uv.lock`
    * Installs `ipykernel` to `.venv` using version in `uv.lock`
3. `uv add 'plotly[express]' httpx pandas`
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

## 5. Build and Publish

Won't demo here but `uv build` and `uv publish` replace `poetry build` and `poetry publish`

## 6. Additional Capabilities

### Replacing `pipx` with `uvx` and `uv tool`

- `uv tool install textual-demo` is similar to `pipx install textual-demo`. Installs to `~/.local/bin/textual-demo`
- `uvx textual-demo` downloads (or uses cache) and runs textual-demo without installing executable in `~/.local/bin`
  - same as `uv tool install textual-demo`

- Variant to try:
  - `uvx --with textual-demo textual-demo`

### Replacing venv and pip

- `uv venv`
- Then `uv pip install`
  - Once there's a `.venv` directory, no need to activate it

- Variant to try:
  - `uv venv --python=3.11`

### Replacing pip-compile

- If just wanting to use pip-compile, use `uv pip compile` as a drop-in replacement that's way faster
  - `uv pip compile pyproject.toml -o requirements.txt`
- Then `uv pip sync requirements.txt`

- Variant to try:
  - If using a project with dependencies specified in `requirements.in` instead of `pyproject.toml`:
  - `uv pip compile requirements.in -o requirements.txt`  
