#!/usr/bin/env python3
# vim: set tabstop=4 noexpandtab shiftwidth=4:

import misaka as m
import os
import sys
import shutil
import re
import functools

BUILDDIR = "html"

BUILDTYPE = "local"
if len(sys.argv) > 1:
	BUILDTYPE = sys.argv[1]

if os.path.exists(BUILDDIR):
	shutil.rmtree(BUILDDIR)

os.mkdir(BUILDDIR)

@functools.lru_cache()
def mkdir_cached(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)

for root, dirs, files in os.walk("."):
	for fn in files:
		if fn.endswith(".md"):
			input_path = os.path.join(root, fn)
			output_dir = os.path.join(BUILDDIR, root)
			output_path = os.path.join(output_dir, fn[:-3]+".html")
			mkdir_cached(output_dir)
			print("Processing {}...".format(input_path), file=sys.stderr)
			with open(input_path, "r") as inp, open(output_path, "w") as out:
				data = inp.read()
				def link_patcher(match):
					if BUILDTYPE == "teeworlds.com":
						path = os.path.normpath(os.path.join(root, match.group(2)))
						return "[{}]({})".format(match.group(1), "/?page=docs&wiki="+path)
					else:
						return "[{}]({})".format(match.group(1), match.group(2)+".html")
				data = re.sub(r"\[([^\]]+)]\(\s*([^\)]+)\.md\s*\)", link_patcher, data)
				html = m.html(data, extensions=m.EXT_TABLES | m.EXT_FENCED_CODE, render_flags=m.HTML_USE_XHTML)
				out.write(html)
