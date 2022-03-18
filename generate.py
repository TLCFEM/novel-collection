import os


def list_folders():
    novels = os.listdir('.')
    return [novel for novel in novels if
            os.path.isdir(novel) and
            not novel.startswith('.') and
            not novel.startswith('fonts') and
            not novel.startswith('venv')]


def header(file_name):
    return r"""%!TeXprogram=xelatex
\documentclass[UTF8,fontset=ubuntu]{ctexbook}
\usepackage{fontspec}
\ctexset{punct=kaiming}
\usepackage[colorlinks]{hyperref}
\usepackage[paperwidth=7in, paperheight=10in,tmargin=1.4in,bmargin=1in,lmargin=1in,rmargin=1in]{geometry}
\raggedbottom""" + f"\n\\title{{{file_name.replace('-', ' ').title()}}}\n" + r"""\author{}\date{\today}
\begin{document}
\maketitle
\tableofcontents"""


if __name__ == '__main__':
    folders = list_folders()
    for folder in folders:
        os.chdir(folder)
        print(folder)
        with open(folder + '.tex', 'w') as f:
            f.write(header(folder))
            for ch in range(len(os.listdir('CH'))):
                f.write(f"\n\\input{{CH/C{ch:03}.tex}}")
            f.write('\n\\end{document}')

        os.system(f'latexmk -xelatex {folder}.tex')
        os.system(f'cp {folder}.pdf ../')
        os.chdir('..')
