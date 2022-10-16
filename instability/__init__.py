import logging, sys
from .internal.paths import find_external_package

EXTERNAL_PACKAGES = ['k-diffusion', 'stable-diffusion', 'taming-transformers']

def _init_external_packages():
  for pkg in EXTERNAL_PACKAGES:
    pkgpath = find_external_package(pkg)
    if not pkgpath:
      logging.warning("Instability couldn't find the required package {}. Importing may fail.".format(pkg))
    else:
      sys.path.append(pkgpath)

_init_external_packages()

from .patches.optimization import enable as _init_optimization
_init_optimization()

import ldm.modules.diffusionmodules.model
from torch.nn.functional import silu
ldm.modules.diffusionmodules.model.nonlinearity = silu
