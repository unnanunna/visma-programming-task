import identifier


class Client():

    def __init__(self, uri: str):
 
        identifyer = identifier.Identifyer()
        identifyer.parse_uri(uri)

        path = identifyer.return_path()
        parameters = identifyer.return_parameters()

        print("Path is ", path)
        print("Parameters are ", parameters)



if __name__ ==  '__main__':
    uri = input("Give uri: ")

    client = Client(uri)
