import Pyro5.api


# Classe nova adicionada: StringUtils
@Pyro5.api.expose
class StringUtils:
    def check_palindrome(self, string: str) -> str:
        if string == string[::-1]:
            return f"A string {string} é um palíndromo."

        return f"A string {string} não é um palíndromo."

    def print_all_substrings(self, string: str) -> list:
        length = len(string)
        seen_substrings = set()

        for start in range(length):
            for end in range(start + 1, length + 1):
                substring = string[start:end]
                if substring not in seen_substrings:
                    seen_substrings.add(substring)

        return list(seen_substrings)


daemon = Pyro5.server.Daemon()  # Cria um Pyro daemon
ns = Pyro5.api.locate_ns()  # Pesquisa do nome do servidor

# Registro das classes como objetos Pyro
uri = daemon.register(StringUtils)

# Registro dos objetos com um nome no servidor
ns.register("example.string", uri)

print("Servidor pronto.")

# inicializa o loop de eventos do servidor e espera uma conexão
daemon.requestLoop()
