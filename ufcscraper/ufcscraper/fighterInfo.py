class UFCdivisions:
    divisionDict = {
        "Men's": {
            "Strawweight": {
                "Division": "Strawweight",
                "Lower_Limit_lbs": None,
                "Upper_Limit_lbs": 115,
                "Lower_Limit_kg": None,
                "Upper_Limit_kg": 52.16
            },
            "Flyweight": {
                "Division": "Flyweight",
                "Lower_Limit_lbs": 116,
                "Upper_Limit_lbs": 125,
                "Lower_Limit_kg": 52.62,
                "Upper_Limit_kg": 56.7
            },
            "Bantamweight": {
                "Division": "Bantamweight",
                "Lower_Limit_lbs": 126,
                "Upper_Limit_lbs": 135,
                "Lower_Limit_kg": 57.15,
                "Upper_Limit_kg": 61.24
            },
            "Featherweight": {
                "Division": "Featherweight",
                "Lower_Limit_lbs": 136,
                "Upper_Limit_lbs": 145,
                "Lower_Limit_kg": 61.69,
                "Upper_Limit_kg": 65.77
            },
            "Lightweight": {
                "Division": "Lightweight",
                "Lower_Limit_lbs": 146,
                "Upper_Limit_lbs": 155,
                "Lower_Limit_kg": 66.22,
                "Upper_Limit_kg": 70.31
            },
            "Welterweight": {
                "Division": "Welterweight",
                "Lower_Limit_lbs": 156,
                "Upper_Limit_lbs": 170,
                "Lower_Limit_kg": 70.76,
                "Upper_Limit_kg": 77.11
            },
            "Middleweight": {
                "Division": "Middleweight",
                "Lower_Limit_lbs": 171,
                "Upper_Limit_lbs": 185,
                "Lower_Limit_kg": 77.56,
                "Upper_Limit_kg": 83.91
            },
            "Light Heavyweight": {
                "Division": "Light Heavyweight",
                "Lower_Limit_lbs": 186,
                "Upper_Limit_lbs": 205,
                "Lower_Limit_kg": 84.37,
                "Upper_Limit_kg": 92.99
            },
            "Heavyweight": {
                "Division": "Heavyweight",
                "Lower_Limit_lbs": 206,
                "Upper_Limit_lbs": 265,
                "Lower_Limit_kg": 93.44,
                "Upper_Limit_kg": 120.20
            }
        },
        "Women's": {
            "Strawweight": {
                "Division": "Strawweight",
                "Lower_Limit_lbs": None,
                "Upper_Limit_lbs": 115,
                "Lower_Limit_kg": None,
                "Upper_Limit_kg": 52.16
            },
            "Flyweight": {
                "Division": "Flyweight",
                "Lower_Limit_lbs": 116,
                "Upper_Limit_lbs": 125,
                "Lower_Limit_kg": 52.62,
                "Upper_Limit_kg": 56.7
            },
            "Bantamweight": {
                "Division": "Bantamweight",
                "Lower_Limit_lbs": 126,
                "Upper_Limit_lbs": 135,
                "Lower_Limit_kg": 57.15,
                "Upper_Limit_kg": 61.24
            },
            "Featherweight": {
                "Division": "Featherweight",
                "Lower_Limit_lbs": 136,
                "Upper_Limit_lbs": 145,
                "Lower_Limit_kg": 61.69,
                "Upper_Limit_kg": 65.77
            }
        }
    }


class WeightClass(UFCdivisions):


    w = "Women\'s"

    def __init__(self, codeStr):

        self.codeStr = codeStr

        if self.w in codeStr:
            self.gender = "Women's"
        else:
            self.gender = "Men's"

        if "Light Heavyweight" in self.codeStr:
            self.divisionName = "Light Heavyweight"
            self.divisionLowerLimitlbs = 186
            self.divisionUpperLimitlbs = 205
            self.divisionLowerLimitkg = 84.37
            self.divisionUpperLimitkg = 92.99
        elif "Catch Weight" in self.codeStr:
            self.divisionName = "Catch Weight"
            self.divisionLowerLimitlbs = None
            self.divisionUpperLimitlbs = None
            self.divisionLowerLimitkg = None
            self.divisionUpperLimitkg = None
        else:
            self.divisionDict = [val for key, val in self.divisionDict[self.gender].items() if key in self.codeStr]
            self.divisionName = self.divisionDict[0]['Division']
            self.divisionLowerLimitlbs = self.divisionDict[0]['Lower_Limit_lbs']
            self.divisionUpperLimitlbs = self.divisionDict[0]['Upper_Limit_lbs']
            self.divisionLowerLimitkg = self.divisionDict[0]['Lower_Limit_kg']
            self.divisionUpperLimitkg = self.divisionDict[0]['Upper_Limit_kg']






