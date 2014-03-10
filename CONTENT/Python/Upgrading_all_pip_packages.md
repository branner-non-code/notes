## Upgrading all pip packages

Use

    pip install -U `pip list --outdated | awk '{ print $1 }'`

Create alias with 

    alias pipup='pip install -U `pip list --outdated | awk '\''{ print $1 }'\''`'

[end]
