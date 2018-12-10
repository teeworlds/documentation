#!/usr/bin/env python3

# Requires Python 3.5+ and misaka

import misaka as m
import sys
from os.path import normpath
import re
from pathlib import Path
import shutil
from argparse import ArgumentParser
from enum import Enum


def main():
    p = ArgumentParser()
    p.add_argument('-t', '--build-type', type=BuildType,
            choices=tuple(BuildType), default=BuildType.LOCAL.value)
    p.add_argument('source', type=Path)
    p.add_argument('target', type=Path)
    args = p.parse_args()

    target = args.target.with_suffix('.new')
    compile_docs(args.source, target, args.build_type)
    shutil.rmtree(str(args.target), ignore_errors=True)
    target.replace(args.target)


class BuildType(Enum):
    LOCAL = 'local'
    TEEWORLDS_COM = 'teeworlds.com'


def compile_docs(source, target, build_type):
    for input_path in source.glob('**/*.md'):
        output_dir = (target / input_path.relative_to(source)).parent
        output_dir.mkdir(exist_ok=True, parents=True)
        output_path = output_dir / (input_path.with_suffix('.html').name)
        print("Processing {}...".format(input_path), file=sys.stderr)

        def link_patcher(match):
            if build_type == BuildType.TEEWORLDS_COM:
                path = normpath(str(input_path.parent.relative_to(source) / match.group(2)))
                return "[{}]({})".format(match.group(1), '/?page=docs&wiki=' + path)
            elif build_type == BuildType.LOCAL:
                return "[{}]({})".format(match.group(1), match.group(2) + '.html')
            else:
                raise ValueError("Unsupported BuildType")

        with input_path.open() as inp, output_path.open('w') as out:
            data = inp.read()
            data = re.sub(r'\[([^\]]+)]\(\s*([^\)]+)\.md\s*\)', link_patcher, data)
            html = m.html(data, extensions=m.EXT_TABLES | m.EXT_FENCED_CODE,
                    render_flags=m.HTML_USE_XHTML)
            out.write(html)


if __name__ == '__main__':
    main()
