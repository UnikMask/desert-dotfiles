!#/bin/env sh

file=$1
orgmode='tempfile --suffix=.org'

pandoc '$file' -f html -t org -o $orgmode

nvim $orgmode
pandoc $orgmode -f org -t html -o '$file'
