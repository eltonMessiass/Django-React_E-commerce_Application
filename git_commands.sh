#!/usr/bin/env bash

git add $1
git commit -m "$2"
git status
git push
git log
