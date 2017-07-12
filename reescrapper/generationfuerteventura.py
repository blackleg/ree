from .core import GenerationScrapper


class GenerationFuerteventura(GenerationScrapper):

    def __init__(self, driver=None):
        super().__init__(driver)
        self.url = "https://demanda.ree.es/movil/canarias/fuerteve/tablas/2"

    def get(self):
        return self._get(self.url)