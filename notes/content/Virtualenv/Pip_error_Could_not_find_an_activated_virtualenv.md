## Pip error: "Could not find an activated virtualenv (required)".

[Hacker Codex](http://hackercodex.com/guide/python-development-environment-on-mac-osx/#restricting-pip-to-virtual-environments) advises:

Add

```bash
syspip(){
   PIP_REQUIRE_VIRTUALENV="" pip "$@"
}
```

to turn off `PIP_REQUIRE_VIRTUALENV=true` in `~/.bash_profile`. Then if global pip installations need to be made (such as `virtualenv` after OS re-install), use

```bash
syspip install --upgrade --no-use-wheel pip setuptools virtualenv
```

[end]
