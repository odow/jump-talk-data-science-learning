## Installation instructions

1. Download and install Julia from https://julialang.org/downloads/
2. Move the contents of this folder somewhere memorable, e.g., `~/Documents/julia-data-science`
3. Open Julia (e.g., from application folder, program menu etc.), then run
    ```
    cd("~/Documents/julia-data-science")
    import Pkg
    Pkg.activate(".")
    Pkg.instantiate()
    ```
4. Now open IJulia:
    ```
    julia> using IJulia
    julia> IJulia.notebook(dir=".")
    ```
5. A browser window will open, and away you go.

Note: the first time you use Julia, it can take a long time to load because it has to
download and install a lot of packages. Same goes for when you use a new package for the
first time.
