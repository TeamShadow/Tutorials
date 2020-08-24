# -*- coding: utf-8 -*-
"""
    pygments.lexers.shadow
    ~~~~~~~~~~~~~~~~~~~

    Pygments lexer for the Shadow language.

    :copyright: Copyright 2020 by the Shadow team, based on pygments.lexers.jvm by the Pygments team.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
    this, combined, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation
from pygments.util import shebang_matches
from pygments import unistring as uni

__all__ = ['ShadowLexer']

class ShadowLexer(RegexLexer):
    """
    For `Shadow <http://shadow-language.org/>` source code.
    """

    name = 'Shadow'
    aliases = ['shadow']
    filenames = ['*.shadow']
    mimetypes = ['text/x-shadow']

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = {
        'root': [
            (r'[^\S\n]+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            # keywords: go before method names to avoid lexing "throw new XYZ"
            # as a method signature
            (r'(and|assert|break|case|cast|catch|check|continue|copy|create|default|destroy|do|else|finally|for|foreach|freeze|if|in|is|or|recover|return|send|skip|spawn|super|switch|this|throw|try|while|xor)\b',
             Keyword),
            # method names
            (r'((?:[^\W\d]|\$)[\w$]*)'                  # method name
             r'(\s*)(\()',                              # signature start
             bygroups(Name.Function, Text, Punctuation)),
            (r'\[[^\W\d][\w]*(,\s*[^\W\d][\w])*\]', Name.Decorator),
            (r'(abstract|constant|extern|get|immutable|locked|native|nullable|private|protected|public|readonly|set)\b', Keyword.Declaration),
            (r'(boolean|byte|code|double|float|int|long|short|ubyte|uint|ulong|ushort|var)\b',
             Keyword.Type),
            (r'(import)(\s+)', bygroups(Keyword.Namespace, Text), 'import'),
            (r'(false|null|true)\b', Keyword.Constant),
            (r'(class|enum|exception|interface|singleton)(\s+)', bygroups(Keyword.Declaration, Text),
             'class'),
            (r'(var)(\s+)', bygroups(Keyword.Declaration, Text),
             'var'),
            (r'(import)(\s+)', bygroups(Keyword.Namespace, Text),
             'import'),
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'\\.'|'[^\\]'|'\\u[0-9a-fA-F]{4}'", String.Char),
            (r'(\.)((?:[^\W\d]|\$)[\w$]*)', bygroups(Punctuation,
                                                     Name.Attribute)),
            (r'([^\W\d]|\$)[\w$]*', Name),
            (r'([0-9]+\.([0-9]+)?|'
             r'\.[0-9]+)'
             r'([eE][+\-]?[0-9]+)?[fFdD]?|'
             r'[0-9][eE][+\-]?[0-9][0-9]*[fFdD]?|'
             r'[0-9]([eE][+\-]?[0-9][0-9]*)?[fFdD]|'
             r'0[xX]([0-9a-fA-F][0-9a-fA-F]*\.?|'
             r'([0-9a-fA-F][0-9a-fA-F]*)?\.[0-9a-fA-F][0-9a-fA-F_]*)'
             r'[pP][+\-]?[0-9][0-9]*[fFdD]?', Number.Float),
            (r'0[xX][0-9a-fA-F][0-9a-fA-F]*[uU]?[yYsSiIlL]?', Number.Hex),
            (r'0[bB][01][01_]*[uU]?[yYsSiIlL]?', Number.Bin),
            (r'0[cC][0-7_]+[uU]?[yYsSiIlL]?', Number.Oct),
            (r'0|[1-9][0-9]*[uU]?[yYsSiIlL]?', Number.Integer),
            (r'[~^*!%&\[\]<>|+=/?#-]', Operator),
            (r'[{}();:.,@]', Punctuation),
            (r'\n', Text)
        ],
        'class': [
            (r'(([^\W\d][\w:]*)@)?([^\W\d][\w]*)', Name.Class, '#pop')
        ],
        'var': [
            (r'([^\W\d])[\w]*', Name, '#pop')
        ],
        'import': [
            (r'[\w\d:]*[^\W\d][\w\d]*(@[^\W\d][\w]*)?', Name.Namespace, '#pop')
        ],
    }
