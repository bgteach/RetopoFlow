'''
Copyright (C) 2023 CG Cookie
http://cgcookie.com
hello@cgcookie.com

Created by Jonathan Denning

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import annotations
from typing import Any, Iterable
from contextlib import contextmanager
from ..ext import termcolor

def colored(
    text: str,
    color: str | None = None,
    *,
    highlight: str | None = None,
    attributes: Iterable[str] | None = None,
    no_color: bool | None = None,
    force_color: bool | None = None,
) -> str:
    return termcolor.colored(
        text,
        color=color,
        on_color=f'on_{highlight}' if highlight else None,
        attrs=attributes,
        no_color=no_color,
        force_color=force_color,
    )

def cprint(
    text: str,
    *,
    color: str | None = None,
    highlight: str | None = None,
    attributes: Iterable[str] | None = None,
    no_color: bool | None = None,
    force_color: bool | None = None,
    **kwargs: Any,
) -> None:
    print(
        colored(
            text,
            color=color,
            highlight=highlight,
            attributes=attributes,
            no_color=no_color,
            force_color=force_color,
        ),
        **kwargs,
    )

def boxed(*lines, title=None, prefix='', margin='', pad=' ', sides='single', color=None, highlight=None, attributes=None, wrap=120, indent=4):
    lines = [line for lines_ in lines for line in lines_.splitlines()]
    # https://www.w3.org/TR/xml-entity-names/025.html
    tl,tm,tr,lm,rm,bl,bm,br,lt,rt = {
        'single': '┌─┐││└─┘┤├',
        'double': '╔═╗║║╚═╝╡╞',
    }[sides]
    if title:
        title = f'{tm}{lt} {title} {rt}{tm}'
        title_width = len(title)
    else:
        title_width = 0
    pad_width = len(pad) * 2
    width = max(max(len(line) for line in lines), title_width)
    if wrap and width > wrap:
        width = wrap
        wrapped_lines = []
        for line in lines:
            first = True
            while True:
                if not first: line = ' '*indent + line
                first = False
                wrapped_lines.append(line[:wrap])
                line = line[wrap:]
                if not line: break
        lines = wrapped_lines
    if prefix: print(prefix, end='')
    if title:
        cprint(f'{margin}{tl}{title}{tm*(width+pad_width-len(title))}{tr}{margin}', color=color, highlight=highlight, attributes=attributes)
    else:
        cprint(f'{margin}{tl}{tm*(width+pad_width)}{tr}{margin}', color=color, highlight=highlight, attributes=attributes)
    for line in lines:
        if prefix: print(prefix, end='')
        cprint(f'{margin}{lm}{pad}{line}{" "*(width - len(line))}{pad}{rm}{margin}', color=color, highlight=highlight, attributes=attributes)
    if prefix: print(prefix, end='')
    cprint(f'{margin}{bl}{bm*(width+pad_width)}{br}{margin}', color=color, highlight=highlight, attributes=attributes)

