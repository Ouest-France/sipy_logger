# sipy_logger
Programmatically creates python loggers with different handlers (console, file, graylog)

# Install

Install from the github repository:

* with [pipenv](https://pipenv.readthedocs.io/en/latest/):

```sh
pipenv install git+https://github.com/Ouest-France/sipy_logger.git#egg=sipy_logger
```

* with `pip`:

```sh
pip3 install git+https://github.com/Ouest-France/sipy_logger.git
```

# Usage

* fully declare the logger in the root script (_eg._ `server.py`):

```python
from os import getenv
LOG_DIR = getenv('LOG_DIR')

from sipy_logger import getLogger
logger = getLogger('myapplogger', fileDir=LOG_DIR, filename=datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%m-myapp.log'))

from ./routehandler import routehandler

# ...
logger.info('starting server, logging in %s', LOG_DIR)
```

* re-use it in sub-scripts (_eg._ `routehandler.py`) that are imported by the root script:

```python
from sipy_logger import getLogger
logger = getLogger('myapplogger') # no need to re-specify the logger parameters, they would be ignored anyway

logger.info('handling route %s', aRoute)
```

# Licence

Unless stated otherwise all works are:

* Copyright © Ouest-France/SIPA Tech 
* licensed under the [MIT license](http://spdx.org/licenses/MIT.html), a copy of which is included [here](LICENSE)

# Contributions

* [Thomas Girault](https://github.com/thomasgirault)
* [Luc Sorel-Giffo](https://github.com/lucsorel)

Pull-requests are welcome and will be processed on a best-effort basis.
