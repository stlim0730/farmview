#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

from HTMLParser import HTMLParser

try:
    import regex as re
except ImportError:
    import re

from textile import Textile
from textile.regex_strings import cls_re_s, regex_snippets
from textile.tools import sanitizer
from textile.utils import normalize_newlines


class Plaintext(Textile):
    """Given text with Textile markup, strip out the Textile and return
    plaintext."""
    def __init__(self, plaintext=True, **kwargs):
        super(Plaintext, self).__init__(**kwargs)
        self.plaintext = plaintext

    def parse(self, text, rel=None, sanitize=False):
        """Parse the input text as textile and return html output."""
        self.notes = OrderedDict()
        self.unreferencedNotes = OrderedDict()
        self.notelist_cache = OrderedDict()


        if self.restricted and not self.plaintext:
            text = self.encode_html(text, quotes=False)

        text = normalize_newlines(text)
        text = text.replace(self.uid, '')

        if self.block_tags:
            if self.lite:
                self.blocktag_whitelist = ['bq', 'p']
                text = self.block(text)
            else:
                self.blocktag_whitelist = [
                        'bq', 'p', 'bc', 'notextile', 'pre', 'h[1-6]',
                        'fn{0}+'.format(regex_snippets['digit']), '###']
                text = self.block(text)
                text = self.placeNoteLists(text)
        else:
            # Inline markup (em, strong, sup, sub, del etc).
            text = self.span(text)

            # Glyph level substitutions (mainly typographic -- " & ' => curly
            # quotes, -- => em-dash etc.
            text = self.glyphs(text)

        if rel:
            self.rel = ' rel="%s"' % rel

        text = self.getRefs(text)

        if not self.lite:
            text = self.placeNoteLists(text)

        text = self.retrieve(text)
        text = text.replace('{0}:glyph:'.format(self.uid), '')

        if sanitize:
            text = sanitizer.sanitize(text)

        text = self.retrieveURLs(text)

        # if the text contains a break tag (<br> or <br />) not followed by
        # a newline, replace it with a new style break tag and a newline.
        text = re.sub(r'<br( /)?>(?!\n)', '<br />\n', text)

        htmlparser = HTMLParser()
        text = htmlparser.unescape(text)
        return text

    def fBlock(self, tag, atts, ext, cite, content):
        if self.plaintext:
            content = self.graf(content)
            o1 = ''
            c1 = ''
            o2 = ''
            c2 = ''
            return o1, o2, content, c2, c1, False
        return super(Plaintext, self).fBlock(tag, atts, ext, cite, content)

    def graf(self, text):
        if not self.lite:
            text = self.noTextile(text)
            text = self.code(text)

        text = self.getHTMLComments(text)

        text = self.getRefs(text)
        text = self.links(text)

        if not self.noimage:
            text = self.image(text)

        if not self.lite:
            text = self.table(text)
            text = self.redcloth_list(text)
            text = self.lists(text)

        text = self.span(text)
        text = self.footnoteRef(text)
        text = self.noteRef(text)

        if not self.plaintext:
            text = self.glyphs(text)

        return text.rstrip('\n')

    def fLink(self, m):
        in_ = m
        pre, inner, url = m.groups()
        pre = pre or ''

        m = re.search(r'''^
            (?P<atts>{0})                # $atts (if any)
            {1}*                         # any optional spaces
            (?P<text>                    # $text is...
                (!.+!)                   #     an image
            |                            #   else...
                .+?                      #     link text
            )                            # end of $text
            (?:\((?P<title>[^)]+?)\))?   # $title (if any)
            $'''.format(cls_re_s, regex_snippets['space']), inner,
                flags=re.X | regex_snippets['mod'])

        atts = m.group('atts') or ''
        text = m.group('text') or '' or inner
        title = m.group('title') or ''

        if self.plaintext:
            return '{0}"{1}":{2}'.format(pre, text, url)
        return super(Plaintext, self).fLink(in_)

    def fSpan(self, match):
        pre, tag, atts, cite, content, end, tail = match.groups()
        if self.plaintext:
            out = '{0}{1}'.format(content, end)
            return out
        return super(Plaintext, self).fSpan(match)

def plaintext(text):
    return Plaintext().parse(text)
