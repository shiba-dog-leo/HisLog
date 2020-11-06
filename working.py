'''
markdownを読み込んでhtmlファイルを作る一連の流れ
'''

# %%
from module import *

# make ntoe obj named thermo
thermo = Note()
thermo.title = "熱力学"
# read md file and write as note's content
thermo.content = mdfile_to_mddoc("./document/.md/test_thermo.md")

with open("./document/.html/thermo.html", mode="w", encoding="utf-8") as f:
    # translate note's contents to html document
    # and make .html file
    f.write(markdown_to_html(thermo.content, title=thermo.title))


# %%
