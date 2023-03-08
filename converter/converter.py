import re


def find_max_tab(text):
    lst = text.replace("   ", "\t").split("\n")
    max_no = 0
    for element in lst:
        count = element.count("\t")
        if count > max_no:
            max_no = count
    return max_no


def nested_list(text):
    max_no = find_max_tab(text)
    print(max_no)
    for i in range(1, max_no + 1):
        print(rf'((?<=\n\t{{{i}}})<li>[.\s\S]*?(?=\n\t{{0,{i - 1}}}<li>|\n<p>))')
        text = re.sub(rf'((?<=\n\t{{{i}}})<li>[.\s\S]*?(?=\n\t{{0,{i - 1}}}<li>|\n<p>))', r'<ul>\1</ul>', text)
    return text


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

    new_text = re.sub(r'(\u2022[.\s\S]*?(?=\n\t*[a-zA-Z0-9]|$))', r'<ul>\1</ul>', new_text)
    new_text = re.sub(r'((?<=\u2022).*)', r'<li>\1</li>', new_text)
    new_text = new_text.replace("\n", "<br>\n")

    new_text = re.sub(r'([^</p>].*(?=<br>\n<br>)|[^>]+$)', r'<p>\1</p>', new_text)
    new_text = new_text.replace("•", "")

    new_text = nested_list(new_text)
    print(new_text)
    return new_text
