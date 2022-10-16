import os, sys

VENDOR_DIR = 'external'
MODULE_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
PROJECT_ROOT = os.path.realpath(os.path.join(MODULE_ROOT, '..'))

def find_external_package(name):
  attempts = [
    (MODULE_ROOT, VENDOR_DIR, name),
    (PROJECT_ROOT, VENDOR_DIR, name)
  ]
  for a in attempts:
    pkgpath = os.path.join(*a)
    if os.path.exists(pkgpath): return pkgpath
  return None

