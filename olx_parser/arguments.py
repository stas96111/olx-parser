import getopt, sys

# Remove script name from arguments
args = sys.argv[1:]

options = "hu:p:j"
long_options = ["help", "url=", "output=", "json"]


def args_parse() -> dict:
    outpur_args = {
        "url": None,
        "pages": 1,
        "is_json": False
    }
    
    try:
        arguments, values = getopt.getopt(args, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print ("usage: olx_parser [-h] [-u URL] [-p PAGES]")
                
            elif currentArgument in ("-u", "--url"):
                outpur_args["url"] = currentValue
                
            elif currentArgument in ("-p", "--pages"):
                outpur_args["pages"] = currentValue
                
            elif currentArgument in ("-j", "--json"):
                outpur_args["is_json"] = True
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        
    return outpur_args