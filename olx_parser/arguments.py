import getopt, sys

# Remove script name from arguments
args = sys.argv[1:]

options = "hu:p:"
long_options = ["help", "url=", "output="]


def parse() -> dict:
    outpur_args = {
        "url": None,
        "pages": 1
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
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        
    return outpur_args