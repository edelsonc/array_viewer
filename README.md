# pyctarr
A simple solution to visualizing `numpy` arrays while scripting. `pyctarr` uses `matplotlib` to create simple heatmaps of 2D `numpy` arrays.

## Installation
Currently `pyctarr` is not on PyPI, so the quickest way to install it is to fork this repository and install locally. This is done by navigating to the repository locally on your computer and typing

```
$ pip install .
```

That's it! Enjoy you visuals!

## Usage
`pyctarr` has to main ways of visualizing your arrays: the `view` function and the `Viewer` class. 

### `view`
The view function create a heatmap of the array and displays it. The script will pause while the display is open, and resume when it is closed.

Ex:

```
#!/Users/edelsonc/miniconda3/bin/python
import numpy.random as nprnd
from pyctarr import view

N = 50 # Dimension of array
rand_array = nprnd.random((N, N))
view(rand_array)
```

### `Viewer`
`Viewer` is a class that stored an array and an associated image and can be updated while scripting. This makes it useful for visualizing updating graphs

Ex:

```
#!/Users/edelsonc/miniconda3/bin/python
import numpy.random as nprnd
from pyctarr import Viewer

N = 50 # Dimension of array
plot_time = 0.1  # show plot for 0.1 seconds
rand_array = nprnd.random((N, N))

viewer = Viewer(rand_array, disp_time=plot_time)
viewer.view()
for _ in range(10):
    new_array = nprnd.random((N, N))
    viewer.update(new_array)
```

The above will create a heatmap that displays for 0.1 seconds and then get updated 10 times.

## Contributions
A big thanks is owed to amniskin for the name suggestion

## To Do
* Add testing
