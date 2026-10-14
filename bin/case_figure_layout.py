"""Group authored case figures for the website's responsive two-column layout."""
import re


def figure_grid(cards):
    figures = [f'<figure class="rsh-case-figure" markdown="1">\n\n{card.strip()}\n\n</figure>' for card in cards]
    return '<div class="rsh-case-figures" markdown="1">\n\n' + '\n\n'.join(figures) + '\n\n</div>\n\n'


def align_case_figure_headers(content):
    """Give paired figures a shared header row without changing image sizes."""
    def wrap(match):
        opening, body, closing = match.groups()
        if 'class="rsh-case-figure-content"' in body:
            return match.group(0)
        body = body.strip()
        heading = re.match(r'^(### [^\n]+)\s*\n', body)
        title = heading.group(1) + '\n\n' if heading else ''
        if heading:
            body = body[heading.end():].strip()
        return (opening + '\n\n' + title +
                '<div class="rsh-case-figure-content" markdown="1">\n\n' + body +
                '\n\n</div>\n\n' + closing)
    return re.sub(r'(<figure class="rsh-case-figure"[^>]*>)(.*?)(</figure>)', wrap, content, flags=re.DOTALL)


def format_case_figures(content):
    """Preserve Markdown text, captions, and links while grouping each image."""
    if 'class="rsh-case-figures"' in content:
        return align_case_figure_headers(content)
    before, separator, rest = content.partition('## Problem set')
    image = re.search(r'^!\[', before, re.MULTILINE)
    if image:
        before = before[:image.start()] + figure_grid([before[image.start():]])
    content = before + separator + rest
    before, separator, results = content.partition('## Results\n')
    if not separator:
        return align_case_figure_headers(content)
    results, footer_mark, footer = results.partition('\n---\n')
    rendered, cards = [], []
    for section in re.split(r'(?=^### )', results, flags=re.MULTILINE):
        chunks = re.split(r'(?=^!\[)', section, flags=re.MULTILINE)
        if len(chunks) > 1:
            cards.append(chunks[0] + chunks[1])
            cards.extend(chunks[2:])
        elif section.strip():
            if cards:
                rendered.append(figure_grid(cards))
                cards = []
            rendered.append(section.strip() + '\n\n')
    if cards:
        rendered.append(figure_grid(cards))
    return align_case_figure_headers(before + separator + '\n' + ''.join(rendered) + footer_mark + footer)
