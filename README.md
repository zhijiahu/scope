<a href="https://travis-ci.org/zhijiahu/scope"><img src="https://travis-ci.org/zhijiahu/scope.svg?branch=master" alt="Build status" /></a>

# Scope
An easy way to run monitoring against APIs

------------------

## Getting started: 30 seconds to Scope

```sh
python scope/main.py -s ../examples
```
------------------

## Configuring the APIs to monitor

For example in this YAML file, Scope will monitor [Google](https://www.google.com/imghp) defined in `backends` using resources defined in `scenarios`

```
backends:
  google: https://www.google.com

scenarios:
  - name: Image Search
    backend: google
    url: /imghp
    method: get

```
