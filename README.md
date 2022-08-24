[![PyPI version](https://badge.fury.io/py/sphinxcontrib-django-urls.svg)](https://badge.fury.io/py/sphinxcontrib-django-urls)
# sphinxcontrib-django-urls

This project is inspired by [sphinxcontrib-django](https://github.com/edoburu/sphinxcontrib-django), it adds the view's URLs to the view documentation.

![resul_image](img.png)

## Installation

1. `pip install sphinxcontrib-django-urls`
1. add to `extensions` in `conf.py`
   ```python
   extensions = [
   '....' 
   'sphinxcontrib_django_urls',
   '....'
    ]
   ```