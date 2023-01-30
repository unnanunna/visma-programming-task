import re
import sys

class Identifyer:

    path = ''
    parameters = {}

    
    def parse_uri(self, uri: str):
        invalid_path = "Path is invalid."

        try: 
            uri_parsed = re.split('://|\?|&|=', uri)

            # Checks scheme
            if (uri_parsed[0] != 'visma-identity'):
                sys.exit("Scheme is not correct (visma-identity).")

            # Check that 'source' is on the path
            if (uri_parsed[2] != 'source'):
                sys.exit(invalid_path)


            if (uri_parsed[1] == 'login'):

                #Check that source is severa
                if(uri_parsed[3] != 'severa'):
                    sys.exit(invalid_path)

                self.parameters = {'source':'severa'}

            elif (uri_parsed[1] == 'sign'):

                #Check that source is vismasign and documentid is in the path
                if (uri_parsed[3] != 'vismasign' or uri_parsed[4] != 'documentid' or uri_parsed[5] == ''):
                    sys.exit(invalid_path)

                self.parameters = {uri_parsed[2]:uri_parsed[3], uri_parsed[4]:uri_parsed[5]}

            elif (uri_parsed[1] == 'confirm'):

                #Check that source is netvisor and path includes paymentnumber
                if(uri_parsed[3] != 'netvisor' or uri_parsed[4] != 'paymentnumber' or uri_parsed[5] == ''):
                    sys.exit(invalid_path)

                #Check whether paymentnumber is integer or not
                try:
                    print("!")
                    p_number = int(uri_parsed[5])
                except:
                    sys.exit(invalid_path)

                self.parameters = {uri_parsed[2]:uri_parsed[3], uri_parsed[4]:p_number}

            else:
                sys.exit(invalid_path)

            self.path = uri

        except:
            sys.exit(invalid_path)
        


    def return_path(self):
        return self.path

    def return_parameters(self):
        return self.parameters

