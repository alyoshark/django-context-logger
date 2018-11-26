# django-context-logger (WIP)


## Dev Prep

```bash
conda -p $PWD/pyenv python=3  # Use Conda + Python 3.7
```

The idea of this project is to create a log handler that taps into the stack to log some upper level variables.

The main application of it, as I can imagine,
is to log some variables global to the entire request lifecycle in Django,
thus it is named `django-context-logger` as of now.
But the usage is definitely not only specific to Django.

This is still work in progress,
and I don't even know if I'm heading to anywhere at all,
so any help is welcomed.