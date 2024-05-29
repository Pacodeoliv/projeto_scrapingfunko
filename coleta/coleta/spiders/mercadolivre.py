import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/brinquedos-hobbies/bonecos-bonecas/bonecos-figuras-acao/funko-pop_NoIndex_True#D[A:funko%20pop,on]"]

    def parse(self, response):
        pass
