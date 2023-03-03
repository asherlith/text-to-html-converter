import re


def convert(text):
    conversions = {"&": "&amp;",
                   "<": "&lt;",
                   ">": "&gt;",
                   "\"": "&quot;",
                   "\'": "&apos;",
                   "¢": "&cent;",
                   "£": "&pound;",
                   "¥": "&yen;",
                   "€": "&euro;",
                   "©": "&copy;",
                   "®": "&reg;",
                   }
    new_text = text.translate(str.maketrans(conversions))
    new_text = new_text.replace("\n", "<br>\n")
    new_text = re.sub(r'(.*<br>\n<br>|[^\n].*$)', r'<p>\1</p>', new_text)
    return new_text
