# barcode é uma lib de qrcode, import a lib, EAN13 é um tipo de padrão
from barcode import EAN13
from barcode.writer import ImageWriter
import qrcode
# gerar código de barras com 13 digitos "12 dig são valores q passamos e o ultimo digito é o verificador gerado automatico"
codigo_barra = EAN13("123123123123", writer=ImageWriter())
codigo_barra.save("codigo_barra")
# dicionarios com lista de produtos e seus codigos
codigos_produtos = {
    "produto_bot1": "147147147147",
    "produto_bot2": "147125147147",
    "produto_bot3": "147147145447",
    "produto_bot4": "147142347147"}

for produto in codigos_produtos:
    # cria o codigo
    codigo = codigos_produtos[produto]
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    # salva o codigo de barra como imagem
    codigo_barra.save(f"codigo_barra_{produto}")

# criando a imagem do qrcode a partir do link
imagem_qrcode = qrcode.make("https://github.com/jaquelinealvess")
# salvar o qdcode
imagem_qrcode.save("qrcode_python.png")
# dicionarios com lista de links que correspondem ao qrcode
links_produtos = {
    "Excel": "https://excelparaestagio.klickpages.com.br/inscricao-basico-cta-att?origemurl=hashtag_yt_org_minibasico2_videoqrcode",
    "VBA": "https://pages.hashtagtreinamentos.com/inscricao-minicurso-formulario?origemurl=hashtag_yt_org_miniform_videoqrcode",
    "Power BI": "https://excelparaestagio.klickpages.com.br/inscricao-minicurso-power-bi?origemurl=hashtag_yt_org_minicursopbi_videoqrcode",
    "Python": "https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoqrcode",
    "SQL": "https://excelparaestagio.klickpages.com.br/inscricao-minicurso-sql?origemurl=hashtag_yt_org_minisql_videoqrcode"
}
# para cada produto no dicionario de links
for produto in links_produtos:
    meu_qrcode = qrcode.make(links_produtos[produto])
    # sempre que tiver variavel dentro do texto coloca o f
    meu_qrcode.save(f"qrcode_{produto}.png")
