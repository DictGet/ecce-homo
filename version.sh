#!/bin/bash -eu

if test $# -ne 1; then
    echo "Missing version number"
    exit 1
fi

VERSION=$1

echo "Running tests"
git commit -am "Bumps version $VERSION"
git tag $VERSION -am "Version $VERSION"
