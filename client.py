import Pyro5.api

string_util_obj = Pyro5.api.Proxy("PYRONAME:example.string")
print(
    "Funções do servidor:\n1- check_palindrome(): Checa se uma dada string é um palíndromo\n"
    "2- print_all_substrings(): Imprime todas as substrings de uma string"
)

while True:
    try:
        function_call = input("Insira o número da função desejada: ")
        if function_call == "exit":
            raise KeyboardInterrupt

        elif function_call == "1":
            string = input("Insira a string: ")
            print(string_util_obj.check_palindrome(string))

        elif function_call == "2":
            string = input("Insira a string: ")
            print(
                f"Substrings de {string}: {string_util_obj.print_all_substrings(string)}"
            )

        else:
            raise ModuleNotFoundError

    except KeyboardInterrupt:
        print("Finalizando programa...")
        break
    except ModuleNotFoundError:
        print(f"Nenhuma função encontrada com código {function_call}")
    except Exception as e:
        print(e)
