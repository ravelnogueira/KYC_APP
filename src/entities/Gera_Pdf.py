# from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.utils import ImageReader
# from reportlab.lib.pagesizes import A4,letter

# Timbrado = ImageReader('src/asset/timbrado.png')
# Foto_Frontal = ImageReader('src/asset/15103414716/ImagemFrontal.png')
# Foto_Planta = ImageReader('src/asset/15103414716/ImagePlanta.png')
# Portal_Transparencia = ImageReader('src/asset/15103414716/PortalTransparencia.png')
# Consulta_Situacao = ImageReader('src/asset/15103414716/ConsultaCPF.png')
# JusBrasil = ImageReader('src/asset/15103414716/ConsultaJusBrasil.png')
# Midias = ImageReader('src/asset/15103414716/ConsultaKeyWordsfraude.png')

# class Gerar_Pdf:
#     def __init__(self):
#         self.canvas = Canvas('src/asset/Relatorio.pdf', pagesize=A4)

#     def Run(self):
#         self.Primeira_Pagina()
#         self.Segunda_pagina()

#     def Primeira_Pagina(self):
#         self.canvas.drawImage(Timbrado,self.mm_to_px(0),self.mm_to_px(0),self.mm_to_px(210),self.mm_to_px(297),mask=None)
#         self.canvas.setFont('Helvetica', 12)

#         try: 
#             self.canvas.drawString(self.mm_to_px(5), self.mm_to_px(265), "Coleta de endereço Maps:")
#             self.canvas.drawImage(Foto_Planta, self.mm_to_px(5),self.mm_to_px(115),self.mm_to_px(140),self.mm_to_px(70))
#             self.canvas.drawImage(Foto_Frontal, self.mm_to_px(5),self.mm_to_px(190),self.mm_to_px(140),self.mm_to_px(70))
#         except:
#             pass
        
#         try:
#             self.canvas.drawString(self.mm_to_px(5), self.mm_to_px(105), "Portal da Transparência:")
#             self.canvas.drawImage(Portal_Transparencia, self.mm_to_px(5),self.mm_to_px(30),self.mm_to_px(140),self.mm_to_px(70))
#             self.canvas.showPage()
#         except:
#             pass

#     def Segunda_pagina(self):
#         self.canvas.drawImage(Timbrado,self.mm_to_px(0),self.mm_to_px(0),self.mm_to_px(210),self.mm_to_px(297),mask=None)
#         try:
#             self.canvas.drawString(self.mm_to_px(5), self.mm_to_px(265), "Consulta Situação Cadastral")
#             self.canvas.drawImage(Consulta_Situacao, self.mm_to_px(5),self.mm_to_px(190),self.mm_to_px(140),self.mm_to_px(70))
#         except:
#             pass
        
#         try:
#             self.canvas.drawString(self.mm_to_px(5), self.mm_to_px(185), "Consultar JusBrasil")
#             self.canvas.drawImage(JusBrasil, self.mm_to_px(5),self.mm_to_px(110),self.mm_to_px(140),self.mm_to_px(70))
#         except:
#             pass
#         try:
#             self.canvas.drawString(self.mm_to_px(5), self.mm_to_px(105), "Consultar Midias Negativas")
#             self.canvas.drawImage(Midias, self.mm_to_px(5),self.mm_to_px(30),self.mm_to_px(140),self.mm_to_px(70))
#         except:
#             pass
        
#         self.canvas.showPage()
#         self.canvas.save()
 
#     def mm_to_px(self, mm):
#         return mm / 0.352777