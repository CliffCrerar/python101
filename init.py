# Create initial layout

from browser import html
from browser import document

header = html.HEADER(Class="text-center")
main = html.MAIN()
footer = html.FOOTER()

headingOne = html.H1('Python101')
subtitleOne = html.SMALL('Learning how to use python')

header.append(headingOne)
header.append(subtitleOne)

main.append(html.H2('Main Section',Class="text-center"))
footer.append(html.H3('Footer Section',Class="text-center"))

document.body.append(header)
document.body.append(main)
document.body.append(footer)
