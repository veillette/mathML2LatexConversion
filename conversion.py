import lxml.etree as ET
import re

def to_latex(text):

    """ Remove TeX codes in text"""
    text = re.sub(r"(\$\$.*?\$\$)", " ", text) 

    """ Find MathML codes and replace it with its LaTeX representations."""
    mml_codes = re.findall(r"(<math.*?<\/math>)", text)
    for mml_code in mml_codes:
        mml_ns = mml_code.replace('<math>', '<math xmlns="http://www.w3.org/1998/Math/MathML">') #Required.
        mml_dom = ET.fromstring(mml_ns)
        xslt = ET.parse("mmltex.xsl")  ## see http://xsltml.sourceforge.net/
        transform = ET.XSLT(xslt)
        mmldom = transform(mml_dom)
        latex_code = str(mmldom)
        text = text.replace(mml_code, latex_code)
    return text
