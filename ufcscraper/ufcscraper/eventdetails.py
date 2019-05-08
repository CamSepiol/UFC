class fighterResandAwards:

    perfBonusURL = 'http://1e49bc5171d173577ecd-1323f4090557a33db01577564f60846c.r80.cf1.rackcdn.com/perf.png'
    subBonusURL = 'http://1e49bc5171d173577ecd-1323f4090557a33db01577564f60846c.r80.cf1.rackcdn.com/sub.png'
    koBonusURL = 'http://1e49bc5171d173577ecd-1323f4090557a33db01577564f60846c.r80.cf1.rackcdn.com/ko.png'

    def __init__(self, codestr, resStr):

        self.codestr = codestr
        self.resStr = resStr

        self.Result = "L"
        self.perfBonusBool = False
        self.perfBonusBin = 0

        self.subBonusBool = False
        self.subBonusBin = 0

        self.koBonusBool = False
        self.koBonusBin = 0

        if self.Result not in resStr:
            if resStr == "W":
                self.Result = "W"


                if self.perfBonusURL in self.codestr:
                    self.perfBonusBool = True
                    self.perfBonusBin = 1

                if self.subBonusURL in self.codestr:
                    self.subBonusBool = True
                    self.subBonusBin = 1

                if self.koBonusURL in self.codestr:
                    self.koBonusBool = True
                    self.koBonusBin = 1

            else:
                self.Result = "NC"






class HeaderFlags:

    titleFightURL = 'http://1e49bc5171d173577ecd-1323f4090557a33db01577564f60846c.r80.cf1.rackcdn.com/belt.png'
    fotnBonusURL = 'http://1e49bc5171d173577ecd-1323f4090557a33db01577564f60846c.r80.cf1.rackcdn.com/fight.png'


    def __init__(self, codeStr):

        self.codeStr = codeStr

        self.titleFightBool = False
        self.titleFightBin = 0

        ###Set title fight values to True and 1 if titleFightURL present in codeStr###

        if self.titleFightURL in self.codeStr:
            self.titleFightBool = True
            self.titleFightBin = 1



        self.fotnBonusBool = False
        self.fotnBonusBin = 0

        ###Set fotnBonus to True and 1 if fotnBonusURL present in codeStr###

        if self.fotnBonusURL in self.codeStr:
            self.fotnBonusBool = True
            self.fotnBonusBin = 1











