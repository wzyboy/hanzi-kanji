#!/usr/bin/env python

import base64
import random
from pathlib import Path

import jinja2


jenv = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./templates/')
)


def main():
    src_dirs = [Path(p) for p in 'cns cnt tw jp'.split()]

    ref_groups = []
    pic_groups = []
    for i in range(1, 61):
        pic_paths = [p / f'{i:02}.jpg' for p in src_dirs]
        random.shuffle(pic_paths)

        # Save the shuffled order as a reference
        ref_group = [p.parent.name for p in pic_paths]
        ref_groups.append(ref_group)

        # Encoded shuffled pics
        pic_group = [
            base64.b64encode(open(p, 'rb').read()).decode()
            for p in pic_paths
        ]
        pic_groups.append(pic_group)

    template = jenv.get_template('index.html')
    html = template.render(
        ref_groups=ref_groups,
        pic_groups=pic_groups,
    )
    with open('index.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()
