import getopt, sys

# Remove script name from arguments
args = sys.argv[1:]

options = "hu:p:o:j"
long_options = ["help", "url=", "pages=", "output=", "json"]


def args_parse() -> dict:
    outpur_args = {
        "url": None,
        "filename": "output",
        "pages": 1,
        "is_json": False
    }
    
    try:
        arguments, values = getopt.getopt(args, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print("usage: olx_parser [-h] [-u URL] [-p PAGES] [-o OUTPUT] [-j]\n")
                print("options:")
                print("  -h, --help  show this help message and exit")
                print("  -u URL      url to parse")
                print("  -p PAGES    pages to parse (default: 1)")
                print("  -o OUTPUT   output file name (default: \"output\")")
                print("  -j          output in json format")
                exit(0)
                        
            elif currentArgument in ("-u", "--url"):
                outpur_args["url"] = currentValue
                
            elif currentArgument in ("-p", "--pages"):
                outpur_args["pages"] = int(currentValue)
                
            elif currentArgument in ("-o", "--output"):
                outpur_args["filename"] = currentValue
                
            elif currentArgument in ("-j", "--json"):
                outpur_args["is_json"] = True
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        
    return outpur_args