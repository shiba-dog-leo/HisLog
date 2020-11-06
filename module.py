import datetime
import markdown as md


class Note ():
    def __init__(self,title="no title", content="no content"):
        self.date = datetime.datetime.now()
        self.title = title #str
        self.content = content #expected markdown doc 

def markdown_to_html(md_doc, title="no title"):
    #requires markdown document
    #returns html document

    pre = '''<!DOCTYPE html>
        <html lang="ja">
        <head>
        <meta charset="UTF-8">
        <title>'''
    mid = '''</title>
        <script type="text/javascript" src="../../MathJax/MathJax.js?config=TeX-AMS_CHTML">
        MathJax.Hub.Config({
            TeX: { equationNumbers: { autoNumber: "AMS" }},
            tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            processEscapes: true
            },
            "HTML-CSS": { matchFontHeight: false },
            displayAlign: "left",
            displayIndent: "2em"
        });
        </script>
        </head>
        <body>
        '''
    post = '''
        </body>
        </html>'''

    txt_html = pre + title + mid + md.markdown(md_doc) + post
    
    return txt_html


def mdfile_to_mddoc(filename):
    #returns Note class object
    #requires .md file
    
    with open(filename, mode="r", encoding="utf-8") as f:
        md_doc = f.read()
    
    return md_doc

#とりあえず．
#あとで構文解析してtitleとかは分離する

