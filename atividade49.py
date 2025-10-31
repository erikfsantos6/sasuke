from dataclasses import dataclass

@dataclass
class Autor:
    nome: str
    biografia: str


@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor  # Relacionamento com a classe Autor

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")


# Criando o autor
autor_kaiju = Autor(
    nome="Naoya Matsumoto",
    biografia="Mangaká japonês conhecido por criar o mangá Kaiju No. 8, publicado pela Shueisha em 2020."
)


manga_kaiju = Livro(
    titulo="Kaiju No. 8",
    ano=2020,
    autor=autor_kaiju
)

# Exibindo os detalhes
manga_kaiju.exibir_detalhes()