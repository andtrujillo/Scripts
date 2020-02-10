#!/bin/bash
grep "File:" url.txt | cut -d ' ' -f2- | xargs touch --
