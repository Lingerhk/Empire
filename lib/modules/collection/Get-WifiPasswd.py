from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        # metadata info about the module, not modified during runtime
        self.info = {
            'Name': 'Get-WifiPasswd',

            'Author': ['@s0nnet'],

            'Description': ('description line 1'),

            'Background' : False,

            'OutputExtension' : None,

            'NeedsAdmin' : True,

            'OpsecSafe' : True,
            
            'MinPSVersion' : '2',

            'Comments': [
                'http://www.s0nnet.com/'
            ]
        }

        # any options needed by the module, settable during runtime
        self.options = {
            'Agent' : {
                'Description'   :   'Agent to grab a screenshot from.',
                'Required'      :   True,
                'Value'         :   ''
            }
        }

        self.mainMenu = mainMenu

        if params:
            for param in params:
                # parameter format is [Name, Value]
                option, value = param
                if option in self.options:
                    self.options[option]['Value'] = value


    def generate(self):
        
		# read in the common module source code
        moduleSource = self.mainMenu.installPath + "/data/module_source/collection/Get-WifiPasswd.ps1"

        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode


        # add any arguments to the end execution of the script
        for option,values in self.options.iteritems():
            if option.lower() != "agent":
                if values['Value'] and values['Value'] != '':
                    if values['Value'].lower() == "true":
                        # if we're just adding a switch
                        script += " -" + str(option)
                    else:
                        script += " -" + str(option) + " " + str(values['Value'])

        return script
