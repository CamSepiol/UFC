from scrapy import Spider, Request
from ..items import UFCscraperItem
from ..eventdetails import HeaderFlags, fighterResandAwards
from ..fighterInfo import WeightClass
from ..fightstatsandinfo import FightStats, FightDetails, DescriptiveStats


class UFCspider(Spider):
    name = "UFC"
    start_urls = [
                  "http://www.ufcstats.com/statistics/events/completed?page=1"
    ]


    def parse(self, response):

        result_urls = [
            'http://www.ufcstats.com/statistics/events/completed?page={}'.format(x) for x in range(1, 19)]

        for url in result_urls:
            yield Request(url=url, callback=self.parse_events_page)

    def parse_events_page(self, response):
        event_page_urls = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "b-link_style_black", " " ))]/@href').extract()


        for url in event_page_urls:
            yield Request(url=url, callback=self.parse_event_details_page)

    def parse_event_details_page(self, response):

        fight_detail_urls = response.xpath(
            "//table[@class='b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table']//tbody//tr[@class='b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click']//@data-link").extract()

        for url in fight_detail_urls:
            yield Request(url=url, callback=self.parse_fight_details_page)


    def parse_fight_details_page(self, response):

        item = UFCscraperItem()

        ###EVENT DETAILS###
        eventName = response.xpath('//html/body/section/div/h2/a//text()').extract_first().strip()


        ###FIGHT DETAILS###
        titleHeaderCodeStr = response.xpath('//html/body/section/div/div/div[2]/div[1]/i').get()

        # checks for titlefights and fight bonuses #
        #
        hF = HeaderFlags(titleHeaderCodeStr)

        # assign gender and weightclass #
        fightGenderWeightClassInfo = response.xpath('//html/body/section/div/div/div[2]/div[1]/i').get()
        #
        gW = WeightClass(fightGenderWeightClassInfo)

        fD = FightDetails()

        method = response.xpath(fD.fightDetailsDict["method"]).get().strip()
        roundFinish = int(response.xpath(fD.fightDetailsDict["roundFinish"]).extract_first().strip())
        timeFinish = response.xpath(fD.fightDetailsDict["timeFinish"]).get().strip()
        ttlFightTime = fD.ttl_fight_time(roundFinish, timeFinish)
        numRoundFormat = response.xpath(fD.fightDetailsDict["numRoundFormat"]).get().strip()[0]
        referee = response.xpath(fD.fightDetailsDict["referee"]).get().strip()
        finishDetails = response.xpath(fD.fightDetailsDict["finishDetails"]).extract()[-2].strip()


        if method not in fD.nonDecisionMethods:
            judge1 = response.xpath(fD.decisionDetailsDict["judge1"]).get()
            judge1RedPts = response.xpath(fD.decisionDetailsDict["judge1RedPts"]).get().strip()[0:2]
            judge1BluePts = response.xpath(fD.decisionDetailsDict["judge1BluePts"]).get().strip()[5:7]
            judge2 = response.xpath(fD.decisionDetailsDict["judge2"]).get()
            judge2RedPts = response.xpath(fD.decisionDetailsDict["judge2RedPts"]).get().strip()[0:2]
            judge2BluePts = response.xpath(fD.decisionDetailsDict["judge2BluePts"]).get().strip()[5:7]
            judge3 = response.xpath(fD.decisionDetailsDict["judge3"]).get()
            judge3RedPts = response.xpath(fD.decisionDetailsDict["judge3RedPts"]).get().strip()[0:2]
            judge3BluePts = response.xpath(fD.decisionDetailsDict["judge3BluePts"]).get().strip()[5:7]




        ###RED CORNER FIGHTER DETAILS###
        if response.xpath('//html/body/section/div/div/div[1]/div[1]/div/h3/a//text()').extract_first() is not None:
            rC_Name = response.xpath('//html/body/section/div/div/div[1]/div[1]/div/h3/a//text()').extract_first()
        else:
            rC_Name = response.xpath('/html/body/section/div/div/div[1]/div[1]/div/h3/span/text()').get()

        #
        rRaA = fighterResandAwards(codestr=titleHeaderCodeStr,
                                   resStr=response.xpath(
                                       '//html/body/section/div/div/div[1]/div[1]/i//text()').get().strip())


        ###RED CORNER FIGHT STATS###
        rFS = FightStats()


        ##TOTAL STRIKING STATS##
        rC_knockdowns = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["knockdowns"]).get().strip())
        rC_ttlStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["ttlStrikesLanded"]).get().strip().split(" of ")[0])
        rC_ttlStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["ttlStrikesLanded"]).get().strip().split(" of ")[1])

        ##TOTAL SIGNIFICANT STRIKING STATS##
        rC_ttlSigStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["ttlSigStrikesLanded"]).get().strip().split(" of ")[0])
        rC_ttlSigStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["ttlSigStrikesAttempted"]).get().strip().split(" of ")[1])
    #rC_SigStrikePercentageLanded = (rC_ttlSigStrikesLanded / rC_ttlSigStrikesAttempted)

        # TOTAL SIG STRIKES BY TARGET#
        # head#
        rC_sigHeadStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["head"]["attempted"]).get().strip().split(" of ")[1])
        rC_sigHeadStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["head"]["landed"]).get().strip().split(" of ")[0])
        # body#
        rC_sigBodyStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["body"]["attempted"]).get().strip().split(" of ")[1])
        rC_sigBodyStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["body"]["landed"]).get().strip().split(" of ")[0])
        # leg#
        rC_sigLegStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["leg"]["attempted"]).get().strip().split(" of ")[1])
        rC_sigLegStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["leg"]["landed"]).get().strip().split(" of ")[0])

        # TOTAL SIG STRIKES BY POSITION#
        # distance#
        rC_sigStrikesDistanceAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["distance"]["attempted"]).get().strip().split(" of ")[1])
        rC_sigStrikesDistanceLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["distance"]["landed"]).get().strip().split(" of ")[0])
        # clinch#
        rC_sigStrikesClinchAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["clinch"]["attempted"]).get().strip().split(" of ")[1])
        rC_sigStrikesClinchLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["clinch"]["landed"]).get().strip().split(" of ")[0])
        # ground#
        rC_sigStrikesGroundAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["ground"]["attempted"]).get().strip().split(" of ")[1])
        rC_sigStrikesGroundLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["ground"]["landed"]).get().strip().split(" of ")[0])


        ##TOTAL GRAPPLING STATS##
        rC_takedownsLanded = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["grappling"]["takedownsLanded"]).get().strip().split(" of ")[0])
        rC_takedownsAttempted = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["grappling"]["takedownsAttempted"]).get().strip().split(" of ")[1])
    #rC_takedownPercentage = ((rC_takedownsLanded / rC_takedownsAttempted))
        rC_submissionAttempts = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["grappling"]["submissionAttempts"]).get().strip())
        rC_passes = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["grappling"]["passes"]).get().strip())
        rC_reversals = int(response.xpath(rFS.fightStatsDict["red"]["totals"]["grappling"]["reversals"]).get().strip())

        ###TOTAL STATS BY ROUND###
        ##ROUND 1##

        # STRIKING#
        rC_rd1_knockdowns = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[0].strip())
        rC_rd1_ttlStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_ttlStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[0].strip().split(" of ")[1])

        # SIGNIFICANT STRIKING#
        rC_rd1_ttlSigStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["ttlSigStrikesLanded"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_ttlSigStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["ttlSigStrikesAttempted"]).extract()[0].strip().split(" of ")[1])
    #rC_rd1_SigStrikePercentageLanded = scrapy.Field()

        # Sig Strikes by Target#
        # head#
        rC_rd1_sigHeadStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["head"]["landed"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_sigHeadStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["head"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # body#
        rC_rd1_sigBodyStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["body"]["landed"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_sigBodyStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["body"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # leg#
        rC_rd1_sigLegStrikesLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["leg"]["landed"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_sigLegStrikesAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["leg"]["attempted"]).extract()[0].strip().split(" of ")[1])

        # Sig Strikes by Position#
        # distance#
        rC_rd1_sigStrikesDistanceLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["distance"]["landed"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_sigStrikesDistanceAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["distance"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # clinch#
        rC_rd1_sigStrikesClinchLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["clinch"]["landed"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_sigStrikesClinchAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["clinch"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # ground#
        rC_rd1_sigStrikesGroundLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["ground"]["landed"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_sigStrikesGroundAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["ground"]["attempted"]).extract()[0].strip().split(" of ")[1])

        # GRAPPLING#
        rC_rd1_takedownsLanded = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[0].strip().split(" of ")[0])
        rC_rd1_takedownsAttempted = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[0].strip().split(" of ")[1])
    #rC_rd1_takedownSuccPercentage = scrapy.Field()
        rC_rd1_submissionAttempts = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[0].strip())
        rC_rd1_passes = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[0].strip())
        rC_rd1_reversals = int(response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[0].strip())


        if roundFinish >= 2:
            ##ROUND 2##

            # STRIKING#
            rC_rd2_knockdowns = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[1].strip())
            rC_rd2_ttlStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              1].strip().split(" of ")[0])
            rC_rd2_ttlStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 1].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            rC_rd2_ttlSigStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[1].strip().split(" of ")[0])
            rC_rd2_ttlSigStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[1].strip().split(" of ")[1])
            # rC_rd2_SigStrikePercentageLanded = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            rC_rd2_sigHeadStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[1].strip().split(" of ")[0])
            rC_rd2_sigHeadStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # body#
            rC_rd2_sigBodyStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[1].strip().split(" of ")[0])
            rC_rd2_sigBodyStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # leg#
            rC_rd2_sigLegStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[1].strip().split(" of ")[0])
            rC_rd2_sigLegStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[1].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            rC_rd2_sigStrikesDistanceLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[1].strip().split(" of ")[0])
            rC_rd2_sigStrikesDistanceAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # clinch#
            rC_rd2_sigStrikesClinchLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[1].strip().split(" of ")[0])
            rC_rd2_sigStrikesClinchAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # ground#
            rC_rd2_sigStrikesGroundLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[1].strip().split(" of ")[0])
            rC_rd2_sigStrikesGroundAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[1].strip().split(" of ")[1])

            # GRAPPLING#
            rC_rd2_takedownsLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             1].strip().split(" of ")[0])
            rC_rd2_takedownsAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                1].strip().split(" of ")[1])
            # rC_rd2_takedownSuccPercentage = scrapy.Field()
            rC_rd2_submissionAttempts = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                1].strip())
            rC_rd2_passes = int(
                response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    1].strip())
            rC_rd2_reversals = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[1].strip())

        ##ROUND 3##
        if roundFinish >= 3:
            # STRIKING#
            rC_rd3_knockdowns = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[2].strip())
            rC_rd3_ttlStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              2].strip().split(" of ")[0])
            rC_rd3_ttlStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 2].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            rC_rd3_ttlSigStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[2].strip().split(" of ")[0])
            rC_rd3_ttlSigStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[2].strip().split(" of ")[1])
            # rC_rd3_SigStrikePercentageLanded = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            rC_rd3_sigHeadStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[2].strip().split(" of ")[0])
            rC_rd3_sigHeadStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # body#
            rC_rd3_sigBodyStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[2].strip().split(" of ")[0])
            rC_rd3_sigBodyStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # leg#
            rC_rd3_sigLegStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[2].strip().split(" of ")[0])
            rC_rd3_sigLegStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[2].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            rC_rd3_sigStrikesDistanceLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[2].strip().split(" of ")[0])
            rC_rd3_sigStrikesDistanceAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # clinch#
            rC_rd3_sigStrikesClinchLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[2].strip().split(" of ")[0])
            rC_rd3_sigStrikesClinchAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # ground#
            rC_rd3_sigStrikesGroundLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[2].strip().split(" of ")[0])
            rC_rd3_sigStrikesGroundAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[2].strip().split(" of ")[1])

            # GRAPPLING#
            rC_rd3_takedownsLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             2].strip().split(" of ")[0])
            rC_rd3_takedownsAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                2].strip().split(" of ")[1])
            # rC_rd3_takedownSuccPercentage = scrapy.Field()
            rC_rd3_submissionAttempts = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                2].strip())
            rC_rd3_passes = int(
                response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    2].strip())
            rC_rd3_reversals = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[2].strip())

        ##ROUND 4##
        if roundFinish >= 4:

            # STRIKING#
            rC_rd4_knockdowns = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[3].strip())
            rC_rd4_ttlStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              3].strip().split(" of ")[0])
            rC_rd4_ttlStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 3].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            rC_rd4_ttlSigStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[3].strip().split(" of ")[0])
            rC_rd4_ttlSigStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[3].strip().split(" of ")[1])
            # rC_rd4_SigStrikePercentageLanded = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            rC_rd4_sigHeadStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[3].strip().split(" of ")[0])
            rC_rd4_sigHeadStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # body#
            rC_rd4_sigBodyStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[3].strip().split(" of ")[0])
            rC_rd4_sigBodyStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # leg#
            rC_rd4_sigLegStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[3].strip().split(" of ")[0])
            rC_rd4_sigLegStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[3].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            rC_rd4_sigStrikesDistanceLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[3].strip().split(" of ")[0])
            rC_rd4_sigStrikesDistanceAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # clinch#
            rC_rd4_sigStrikesClinchLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[3].strip().split(" of ")[0])
            rC_rd4_sigStrikesClinchAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # ground#
            rC_rd4_sigStrikesGroundLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[3].strip().split(" of ")[0])
            rC_rd4_sigStrikesGroundAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[3].strip().split(" of ")[1])

            # GRAPPLING#
            rC_rd4_takedownsLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             3].strip().split(" of ")[0])
            rC_rd4_takedownsAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                3].strip().split(" of ")[1])
            # rC_rd4_takedownSuccPercentage = scrapy.Field()
            rC_rd4_submissionAttempts = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                3].strip())
            rC_rd4_passes = int(
                response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    3].strip())
            rC_rd4_reversals = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[3].strip())

        ##ROUND 5##
        if roundFinish >= 5:
            # STRIKING#
            rC_rd5_knockdowns = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[4].strip())
            rC_rd5_ttlStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              4].strip().split(" of ")[0])
            rC_rd5_ttlStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 4].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            rC_rd5_ttlSigStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[4].strip().split(" of ")[0])
            rC_rd5_ttlSigStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[4].strip().split(" of ")[1])
            # rC_rd5_SigStrikePercentageLanded = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            rC_rd5_sigHeadStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[4].strip().split(" of ")[0])
            rC_rd5_sigHeadStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # body#
            rC_rd5_sigBodyStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[4].strip().split(" of ")[0])
            rC_rd5_sigBodyStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # leg#
            rC_rd5_sigLegStrikesLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[4].strip().split(" of ")[0])
            rC_rd5_sigLegStrikesAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[4].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            rC_rd5_sigStrikesDistanceLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[4].strip().split(" of ")[0])
            rC_rd5_sigStrikesDistanceAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # clinch#
            rC_rd5_sigStrikesClinchLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[4].strip().split(" of ")[0])
            rC_rd5_sigStrikesClinchAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # ground#
            rC_rd5_sigStrikesGroundLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[4].strip().split(" of ")[0])
            rC_rd5_sigStrikesGroundAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[4].strip().split(" of ")[1])

            # GRAPPLING#
            rC_rd5_takedownsLanded = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             4].strip().split(" of ")[0])
            rC_rd5_takedownsAttempted = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                4].strip().split(" of ")[1])
            # rC_rd5_takedownSuccPercentage = scrapy.Field()
            rC_rd5_submissionAttempts = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                4].strip())
            rC_rd5_passes = int(
                response.xpath(rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    4].strip())
            rC_rd5_reversals = int(response.xpath(
                rFS.fightStatsDict["red"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[4].strip())




        ################################################################################################################


        ###BLUE CORNER FIGHTER DETAILS###
        if response.xpath('/html/body/section/div/div/div[1]/div[2]/div/h3/a//text()').extract_first() is not None:
            bC_Name = response.xpath('/html/body/section/div/div/div[1]/div[2]/div/h3/a//text()').extract_first()
        else:
            bC_Name = response.xpath('/html/body/section/div/div/div[1]/div[2]/div/h3/span/text()').get()


        bRaA = fighterResandAwards(codestr=titleHeaderCodeStr,
                                   resStr=response.xpath(
                                       '//html/body/section/div/div/div[1]/div[2]/i//text()').get().strip())

        ###BLUE CORNER FIGHT STATS###
        bFS = FightStats()

        ##TOTAL STRIKING STATS##
        bC_knockdowns = int(response.xpath(bFS.fightStatsDict["blue"]["totals"]["striking"]["knockdowns"]).get().strip())
        bC_ttlStrikesLanded = int(
            response.xpath(bFS.fightStatsDict["blue"]["totals"]["striking"]["ttlStrikesLanded"]).get().strip().split(
                " of ")[0])
        bC_ttlStrikesAttempted = int(
            response.xpath(bFS.fightStatsDict["blue"]["totals"]["striking"]["ttlStrikesLanded"]).get().strip().split(
                " of ")[1])

        ##TOTAL SIGNIFICANT STRIKING STATS##
        bC_ttlSigStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"][
                "ttlSigStrikesLanded"]).get().strip().split(" of ")[0])
        bC_ttlSigStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"][
                "ttlSigStrikesAttempted"]).get().strip().split(" of ")[1])
        # bC_SigStrikePercentageLanded = (bC_ttlSigStrikesLanded / bC_ttlSigStrikesAttempted)

        # TOTAL SIG STRIKES BY TARGET#
        # head#
        bC_sigHeadStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["head"][
                "attempted"]).get().strip().split(" of ")[1])
        bC_sigHeadStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["head"][
                "landed"]).get().strip().split(" of ")[0])
        # body#
        bC_sigBodyStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["body"][
                "attempted"]).get().strip().split(" of ")[1])
        bC_sigBodyStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["body"][
                "landed"]).get().strip().split(" of ")[0])
        # leg#
        bC_sigLegStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["leg"][
                "attempted"]).get().strip().split(" of ")[1])
        bC_sigLegStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByTarget"]["leg"][
                "landed"]).get().strip().split(" of ")[0])

        # TOTAL SIG STRIKES BY POSITION#
        # distance#
        bC_sigStrikesDistanceAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["distance"][
                "attempted"]).get().strip().split(" of ")[1])
        bC_sigStrikesDistanceLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["distance"][
                "landed"]).get().strip().split(" of ")[0])
        # clinch#
        bC_sigStrikesClinchAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["clinch"][
                "attempted"]).get().strip().split(" of ")[1])
        bC_sigStrikesClinchLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["clinch"][
                "landed"]).get().strip().split(" of ")[0])
        # ground#
        bC_sigStrikesGroundAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["ground"][
                "attempted"]).get().strip().split(" of ")[1])
        bC_sigStrikesGroundLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["totals"]["striking"]["significantStrikes"]["sigStrikesByPosition"]["ground"][
                "landed"]).get().strip().split(" of ")[0])

        ##TOTAL GRAPPLING STATS##
        bC_takedownsLanded = int(
            response.xpath(bFS.fightStatsDict["blue"]["totals"]["grappling"]["takedownsLanded"]).get().strip().split(
                " of ")[0])
        bC_takedownsAttempted = int(
            response.xpath(bFS.fightStatsDict["blue"]["totals"]["grappling"]["takedownsLanded"]).get().strip().split(
                " of ")[1])
        # bC_takedownPercentage = ((bC_takedownsLanded / bC_takedownsAttempted))
        bC_submissionAttempts = int(
            response.xpath(bFS.fightStatsDict["blue"]["totals"]["grappling"]["submissionAttempts"]).get().strip())
        bC_passes = int(response.xpath(bFS.fightStatsDict["blue"]["totals"]["grappling"]["passes"]).get().strip())
        bC_reversals = int(response.xpath(bFS.fightStatsDict["blue"]["totals"]["grappling"]["reversals"]).get().strip())

        ###TOTAL STATS BY ROUND###
        ##ROUND 1##

        # STRIKING#
        bC_rd1_knockdowns = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[0].strip())
        bC_rd1_ttlStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                          0].strip().split(" of ")[0])
        bC_rd1_ttlStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                             0].strip().split(" of ")[1])

        # SIGNIFICANT STRIKING#
        bC_rd1_ttlSigStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "ttlSigStrikesLanded"]).extract()[0].strip().split(" of ")[0])
        bC_rd1_ttlSigStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "ttlSigStrikesAttempted"]).extract()[0].strip().split(" of ")[1])
        # bC_rd1_SigStrikePercentageLanded = scrapy.Field()

        # Sig Strikes by Target#
        # head#
        bC_rd1_sigHeadStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByTarget"]["head"]["landed"]).extract()[0].strip().split(" of ")[0])
        bC_rd1_sigHeadStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByTarget"]["head"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # body#
        bC_rd1_sigBodyStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByTarget"]["body"]["landed"]).extract()[0].strip().split(" of ")[0])
        bC_rd1_sigBodyStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByTarget"]["body"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # leg#
        bC_rd1_sigLegStrikesLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByTarget"]["leg"]["landed"]).extract()[0].strip().split(" of ")[0])
        bC_rd1_sigLegStrikesAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByTarget"]["leg"]["attempted"]).extract()[0].strip().split(" of ")[1])

        # Sig Strikes by Position#
        # distance#
        bC_rd1_sigStrikesDistanceLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByPosition"]["distance"]["landed"]).extract()[0].strip().split(" of ")[0])
        bC_rd1_sigStrikesDistanceAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByPosition"]["distance"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # clinch#
        bC_rd1_sigStrikesClinchLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByPosition"]["clinch"]["landed"]).extract()[0].strip().split(" of ")[0])
        bC_rd1_sigStrikesClinchAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[0].strip().split(" of ")[1])
        # ground#
        bC_rd1_sigStrikesGroundLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByPosition"]["ground"]["landed"]).extract()[0].strip().split(" of ")[0])
        bC_rd1_sigStrikesGroundAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                "sigStrikesByPosition"]["ground"]["attempted"]).extract()[0].strip().split(" of ")[1])

        # GRAPPLING#
        bC_rd1_takedownsLanded = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                         0].strip().split(" of ")[0])
        bC_rd1_takedownsAttempted = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                            0].strip().split(" of ")[1])
        # bC_rd1_takedownSuccPercentage = scrapy.Field()
        bC_rd1_submissionAttempts = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                            0].strip())
        bC_rd1_passes = int(
            response.xpath(bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                0].strip())
        bC_rd1_reversals = int(response.xpath(
            bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[0].strip())

        if roundFinish >= 2:
            ##ROUND 2##

            # STRIKING#
            bC_rd2_knockdowns = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[
                                        1].strip())
            bC_rd2_ttlStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              1].strip().split(" of ")[0])
            bC_rd2_ttlStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 1].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            bC_rd2_ttlSigStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[1].strip().split(" of ")[0])
            bC_rd2_ttlSigStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[1].strip().split(" of ")[1])
            # bC_rd2_SigStrikePercentageLanded = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            bC_rd2_sigHeadStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[1].strip().split(" of ")[0])
            bC_rd2_sigHeadStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # body#
            bC_rd2_sigBodyStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[1].strip().split(" of ")[0])
            bC_rd2_sigBodyStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # leg#
            bC_rd2_sigLegStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[1].strip().split(" of ")[0])
            bC_rd2_sigLegStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[1].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            bC_rd2_sigStrikesDistanceLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[1].strip().split(" of ")[0])
            bC_rd2_sigStrikesDistanceAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # clinch#
            bC_rd2_sigStrikesClinchLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[1].strip().split(" of ")[0])
            bC_rd2_sigStrikesClinchAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[1].strip().split(" of ")[1])
            # ground#
            bC_rd2_sigStrikesGroundLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[1].strip().split(" of ")[0])
            bC_rd2_sigStrikesGroundAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[1].strip().split(" of ")[1])

            # GRAPPLING#
            bC_rd2_takedownsLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             1].strip().split(" of ")[0])
            bC_rd2_takedownsAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                1].strip().split(" of ")[1])
            # bC_rd2_takedownSuccPercentage = scrapy.Field()
            bC_rd2_submissionAttempts = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                1].strip())
            bC_rd2_passes = int(
                response.xpath(
                    bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    1].strip())
            bC_rd2_reversals = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[
                                       1].strip())

        ##ROUND 3##
        if roundFinish >= 3:
            # STRIKING#
            bC_rd3_knockdowns = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[
                                        2].strip())
            bC_rd3_ttlStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              2].strip().split(" of ")[0])
            bC_rd3_ttlStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 2].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            bC_rd3_ttlSigStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[2].strip().split(" of ")[0])
            bC_rd3_ttlSigStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[2].strip().split(" of ")[1])
            # bC_rd3_SigStrikePercentageLanded = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            bC_rd3_sigHeadStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[2].strip().split(" of ")[0])
            bC_rd3_sigHeadStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # body#
            bC_rd3_sigBodyStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[2].strip().split(" of ")[0])
            bC_rd3_sigBodyStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # leg#
            bC_rd3_sigLegStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[2].strip().split(" of ")[0])
            bC_rd3_sigLegStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[2].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            bC_rd3_sigStrikesDistanceLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[2].strip().split(" of ")[0])
            bC_rd3_sigStrikesDistanceAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # clinch#
            bC_rd3_sigStrikesClinchLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[2].strip().split(" of ")[0])
            bC_rd3_sigStrikesClinchAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[2].strip().split(" of ")[1])
            # ground#
            bC_rd3_sigStrikesGroundLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[2].strip().split(" of ")[0])
            bC_rd3_sigStrikesGroundAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[2].strip().split(" of ")[1])

            # GRAPPLING#
            bC_rd3_takedownsLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             2].strip().split(" of ")[0])
            bC_rd3_takedownsAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                2].strip().split(" of ")[1])
            # bC_rd3_takedownSuccPercentage = scrapy.Field()
            bC_rd3_submissionAttempts = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                2].strip())
            bC_rd3_passes = int(
                response.xpath(
                    bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    2].strip())
            bC_rd3_reversals = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[
                                       2].strip())

        ##ROUND 4##
        if roundFinish >= 4:
            # STRIKING#
            bC_rd4_knockdowns = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[
                                        3].strip())
            bC_rd4_ttlStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              3].strip().split(" of ")[0])
            bC_rd4_ttlStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 3].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            bC_rd4_ttlSigStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[3].strip().split(" of ")[0])
            bC_rd4_ttlSigStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[3].strip().split(" of ")[1])
            # bC_rd4_SigStrike = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            bC_rd4_sigHeadStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[3].strip().split(" of ")[0])
            bC_rd4_sigHeadStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # body#
            bC_rd4_sigBodyStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[3].strip().split(" of ")[0])
            bC_rd4_sigBodyStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # leg#
            bC_rd4_sigLegStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[3].strip().split(" of ")[0])
            bC_rd4_sigLegStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[3].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            bC_rd4_sigStrikesDistanceLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[3].strip().split(" of ")[0])
            bC_rd4_sigStrikesDistanceAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # clinch#
            bC_rd4_sigStrikesClinchLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[3].strip().split(" of ")[0])
            bC_rd4_sigStrikesClinchAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[3].strip().split(" of ")[1])
            # ground#
            bC_rd4_sigStrikesGroundLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[3].strip().split(" of ")[0])
            bC_rd4_sigStrikesGroundAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[3].strip().split(" of ")[1])

            # GRAPPLING#
            bC_rd4_takedownsLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             3].strip().split(" of ")[0])
            bC_rd4_takedownsAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                3].strip().split(" of ")[1])
            # bC_rd4_takedownSuccPercentage = scrapy.Field()
            bC_rd4_submissionAttempts = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                3].strip())
            bC_rd4_passes = int(
                response.xpath(
                    bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    3].strip())
            bC_rd4_reversals = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[
                                       3].strip())

        ##ROUND 5##
        if roundFinish >= 5:
            # STRIKING#
            bC_rd5_knockdowns = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["knockdowns"]).extract()[
                                        4].strip())
            bC_rd5_ttlStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesLanded"]).extract()[
                                              4].strip().split(" of ")[0])
            bC_rd5_ttlStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["ttlStrikesAttempted"]).extract()[
                                                 4].strip().split(" of ")[1])

            # SIGNIFICANT STRIKING#
            bC_rd5_ttlSigStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesLanded"]).extract()[4].strip().split(" of ")[0])
            bC_rd5_ttlSigStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "ttlSigStrikesAttempted"]).extract()[4].strip().split(" of ")[1])
            # bC_rd5_SigStrikePercentageLanded = scrapy.Field()

            # Sig Strikes by Target#
            # head#
            bC_rd5_sigHeadStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["landed"]).extract()[4].strip().split(" of ")[0])
            bC_rd5_sigHeadStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["head"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # body#
            bC_rd5_sigBodyStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["landed"]).extract()[4].strip().split(" of ")[0])
            bC_rd5_sigBodyStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["body"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # leg#
            bC_rd5_sigLegStrikesLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["landed"]).extract()[4].strip().split(" of ")[0])
            bC_rd5_sigLegStrikesAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByTarget"]["leg"]["attempted"]).extract()[4].strip().split(" of ")[1])

            # Sig Strikes by Position#
            # distance#
            bC_rd5_sigStrikesDistanceLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["landed"]).extract()[4].strip().split(" of ")[0])
            bC_rd5_sigStrikesDistanceAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["distance"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # clinch#
            bC_rd5_sigStrikesClinchLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["landed"]).extract()[4].strip().split(" of ")[0])
            bC_rd5_sigStrikesClinchAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["clinch"]["attempted"]).extract()[4].strip().split(" of ")[1])
            # ground#
            bC_rd5_sigStrikesGroundLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["landed"]).extract()[4].strip().split(" of ")[0])
            bC_rd5_sigStrikesGroundAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["striking"]["significantStrikes"][
                    "sigStrikesByPosition"]["ground"]["attempted"]).extract()[4].strip().split(" of ")[1])

            # GRAPPLING#
            bC_rd5_takedownsLanded = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsLanded"]).extract()[
                                             4].strip().split(" of ")[0])
            bC_rd5_takedownsAttempted = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["takedownsAttempted"]).extract()[
                                                4].strip().split(" of ")[1])
            # bC_rd5_takedownSuccPercentage = scrapy.Field()
            bC_rd5_submissionAttempts = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["submissionAttempts"]).extract()[
                                                4].strip())
            bC_rd5_passes = int(
                response.xpath(
                    bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["passes"]).extract()[
                    4].strip())
            bC_rd5_reversals = int(response.xpath(
                bFS.fightStatsDict["blue"]["byRound"]["round1"]["totals"]["grappling"]["reversals"]).extract()[
                                       4].strip())


#######################################################################################################


        ###RED CORNER DESCRIPTIVE STATS###
        rDS_List = [rC_ttlSigStrikesLanded, rC_ttlSigStrikesAttempted, bC_ttlSigStrikesLanded,
                    bC_ttlSigStrikesAttempted, rC_takedownsLanded, rC_takedownsAttempted,
                    bC_takedownsLanded, bC_takedownsAttempted, ttlFightTime]

        rDS = DescriptiveStats(rDS_List)
        rC_SLpM = rDS.SLpM
        rC_StrAcc = rDS.StrAcc
        rC_SApM = rDS.SApM
        rC_StrDef = rDS.StrDef
        rC_TDAcc = rDS.TDAcc
        rC_TDDef = rDS.TDdef
        rC_SigStrDif = rDS.SigStrDif

        ###BLUE CORNER DESCRIPTIVE STATS###
        bDS_List = [bC_ttlSigStrikesLanded, bC_ttlSigStrikesAttempted, rC_ttlSigStrikesLanded,
                    rC_ttlSigStrikesAttempted, bC_takedownsLanded, bC_takedownsAttempted,
                    rC_takedownsLanded, rC_takedownsAttempted, ttlFightTime]


        bDS = DescriptiveStats(bDS_List)
        bC_SLpM = bDS.SLpM
        bC_StrAcc = bDS.StrAcc
        bC_SApM = bDS.SApM
        bC_StrDef = bDS.StrDef
        bC_TDAcc = bDS.TDAcc
        bC_TDDef = bDS.TDdef
        bC_SigStrDif = bDS.SigStrDif

#######################################################################################################################


        ####YIELD ITEMS####

        ##event detail items##
        item["eventName"] = eventName

        ##fight detail items##
        item["titleFightBool"] = hF.titleFightBool
        item["titleFightBin"] = hF.titleFightBin
        item["fotnBonusBool"] = hF.fotnBonusBool
        item["fotnBonusBin"] = hF.fotnBonusBin
        item["fightGender"] = gW.gender
        item["Division"] = gW.divisionName
        item["Lower_Limit_lbs"] = gW.divisionLowerLimitlbs
        item["Upper_Limit_lbs"] = gW.divisionUpperLimitlbs
        item["Lower_Limit_kg"] = gW.divisionLowerLimitkg
        item["Upper_Limit_kg"] = gW.divisionUpperLimitkg
        item["method"] = method
        item["roundFinish"] = roundFinish
        item["timeFinish"] = timeFinish
        item["ttlFightTime"] = ttlFightTime
        item["numRoundFormat"] = numRoundFormat
        item["referee"] = referee
        item["finishDetails"] = finishDetails

        if method not in fD.nonDecisionMethods:
            item["judge1"] = judge1
            item["judge1RedPts"] = judge1RedPts
            item["judge1BluePts"] = judge1BluePts
            item["judge2"] = judge2
            item["judge2RedPts"] = judge2RedPts
            item["judge2BluePts"] = judge2BluePts
            item["judge3"] = judge3
            item["judge3RedPts"] = judge3RedPts
            item["judge3BluePts"] = judge3BluePts



        ##red corner fighter details items##
        item["rC_Name"] = rC_Name
        item["rC_Result"] = rRaA.Result
        item["rC_perfBonusBool"] = rRaA.perfBonusBool
        item["rC_perfBonusBin"] = rRaA.perfBonusBin
        item["rC_subBonusBool"] = rRaA.subBonusBool
        item["rC_subBonusBin"] = rRaA.subBonusBin
        item["rC_koBonusBool"] = rRaA.koBonusBool
        item["rC_koBonusBin"] = rRaA.koBonusBin

        ##red corner fight stats items##
        item["rC_knockdowns"] = rC_knockdowns
        item["rC_ttlStrikesLanded"] = rC_ttlStrikesLanded
        item["rC_ttlStrikesAttempted"] = rC_ttlStrikesAttempted

        item["rC_ttlSigStrikesLanded"] = rC_ttlSigStrikesLanded
        item["rC_ttlSigStrikesAttempted"] = rC_ttlSigStrikesAttempted

        item["rC_sigHeadStrikesLanded"] = rC_sigHeadStrikesLanded
        item["rC_sigHeadStrikesAttempted"] = rC_sigHeadStrikesAttempted

        item["rC_sigBodyStrikesLanded"] = rC_sigBodyStrikesLanded
        item["rC_sigBodyStrikesAttempted"] = rC_sigBodyStrikesAttempted

        item["rC_sigLegStrikesLanded"] = rC_sigLegStrikesLanded
        item["rC_sigLegStrikesAttempted"] = rC_sigLegStrikesAttempted

        item["rC_sigStrikesDistanceAttempted"] = rC_sigStrikesDistanceAttempted
        item["rC_sigStrikesDistanceLanded"] = rC_sigStrikesDistanceLanded

        item["rC_sigStrikesClinchLanded"] = rC_sigStrikesClinchLanded
        item["rC_sigStrikesClinchAttempted"] = rC_sigStrikesClinchAttempted

        item["rC_sigStrikesGroundLanded"] = rC_sigStrikesGroundLanded
        item["rC_sigStrikesGroundAttempted"] = rC_sigStrikesGroundAttempted

        item["rC_takedownsLanded"] = rC_takedownsLanded
        item["rC_takedownsAttempted"] = rC_takedownsAttempted
        #item["rC_takedownPercentage"] = rC_takedownPercentage
        item["rC_submissionAttempts"] = rC_submissionAttempts
        item["rC_passes"] = rC_passes
        item["rC_reversals"] = rC_reversals

        ##rd 1##
        item["rC_rd1_knockdowns"] = rC_rd1_knockdowns
        item["rC_rd1_ttlStrikesLanded"] = rC_rd1_ttlStrikesLanded
        item["rC_rd1_ttlStrikesAttempted"] = rC_rd1_ttlStrikesAttempted

        item["rC_rd1_ttlSigStrikesLanded"] = rC_rd1_ttlSigStrikesLanded
        item["rC_rd1_ttlSigStrikesAttempted"] = rC_rd1_ttlSigStrikesAttempted

        item["rC_rd1_sigHeadStrikesLanded"] = rC_rd1_sigHeadStrikesLanded
        item["rC_rd1_sigHeadStrikesAttempted"] = rC_rd1_sigHeadStrikesAttempted

        item["rC_rd1_sigBodyStrikesLanded"] = rC_rd1_sigBodyStrikesLanded
        item["rC_rd1_sigBodyStrikesAttempted"] = rC_rd1_sigBodyStrikesAttempted

        item["rC_rd1_sigLegStrikesLanded"] = rC_rd1_sigLegStrikesLanded
        item["rC_rd1_sigLegStrikesAttempted"] = rC_rd1_sigLegStrikesAttempted

        item["rC_rd1_sigStrikesDistanceAttempted"] = rC_rd1_sigStrikesDistanceAttempted
        item["rC_rd1_sigStrikesDistanceLanded"] = rC_rd1_sigStrikesDistanceLanded

        item["rC_rd1_sigStrikesClinchLanded"] = rC_rd1_sigStrikesClinchLanded
        item["rC_rd1_sigStrikesClinchAttempted"] = rC_rd1_sigStrikesClinchAttempted

        item["rC_rd1_sigStrikesGroundLanded"] = rC_rd1_sigStrikesGroundLanded
        item["rC_rd1_sigStrikesGroundAttempted"] = rC_rd1_sigStrikesGroundAttempted

        item["rC_rd1_takedownsLanded"] = rC_rd1_takedownsLanded
        item["rC_rd1_takedownsAttempted"] = rC_rd1_takedownsAttempted
        # item["rC_rd1_takedownPercentage"] = rC_rd1_takedownPercentage
        item["rC_rd1_submissionAttempts"] = rC_rd1_submissionAttempts
        item["rC_rd1_passes"] = rC_rd1_passes
        item["rC_rd1_reversals"] = rC_rd1_reversals

        ##rd 2##
        if roundFinish >= 2:
            item["rC_rd2_knockdowns"] = rC_rd2_knockdowns
            item["rC_rd2_ttlStrikesLanded"] = rC_rd2_ttlStrikesLanded
            item["rC_rd2_ttlStrikesAttempted"] = rC_rd2_ttlStrikesAttempted

            item["rC_rd2_ttlSigStrikesLanded"] = rC_rd2_ttlSigStrikesLanded
            item["rC_rd2_ttlSigStrikesAttempted"] = rC_rd2_ttlSigStrikesAttempted

            item["rC_rd2_sigHeadStrikesLanded"] = rC_rd2_sigHeadStrikesLanded
            item["rC_rd2_sigHeadStrikesAttempted"] = rC_rd2_sigHeadStrikesAttempted

            item["rC_rd2_sigBodyStrikesLanded"] = rC_rd2_sigBodyStrikesLanded
            item["rC_rd2_sigBodyStrikesAttempted"] = rC_rd2_sigBodyStrikesAttempted

            item["rC_rd2_sigLegStrikesLanded"] = rC_rd2_sigLegStrikesLanded
            item["rC_rd2_sigLegStrikesAttempted"] = rC_rd2_sigLegStrikesAttempted

            item["rC_rd2_sigStrikesDistanceAttempted"] = rC_rd2_sigStrikesDistanceAttempted
            item["rC_rd2_sigStrikesDistanceLanded"] = rC_rd2_sigStrikesDistanceLanded

            item["rC_rd2_sigStrikesClinchLanded"] = rC_rd2_sigStrikesClinchLanded
            item["rC_rd2_sigStrikesClinchAttempted"] = rC_rd2_sigStrikesClinchAttempted

            item["rC_rd2_sigStrikesGroundLanded"] = rC_rd2_sigStrikesGroundLanded
            item["rC_rd2_sigStrikesGroundAttempted"] = rC_rd2_sigStrikesGroundAttempted

            item["rC_rd2_takedownsLanded"] = rC_rd2_takedownsLanded
            item["rC_rd2_takedownsAttempted"] = rC_rd2_takedownsAttempted
            # item["rC_rd2_takedownPercentage"] = rC_rd2_takedownPercentage
            item["rC_rd2_submissionAttempts"] = rC_rd2_submissionAttempts
            item["rC_rd2_passes"] = rC_rd2_passes
            item["rC_rd2_reversals"] = rC_rd2_reversals

        ##rd 3##
        if roundFinish >= 3:
            item["rC_rd3_knockdowns"] = rC_rd3_knockdowns
            item["rC_rd3_ttlStrikesLanded"] = rC_rd3_ttlStrikesLanded
            item["rC_rd3_ttlStrikesAttempted"] = rC_rd3_ttlStrikesAttempted

            item["rC_rd3_ttlSigStrikesLanded"] = rC_rd3_ttlSigStrikesLanded
            item["rC_rd3_ttlSigStrikesAttempted"] = rC_rd3_ttlSigStrikesAttempted

            item["rC_rd3_sigHeadStrikesLanded"] = rC_rd3_sigHeadStrikesLanded
            item["rC_rd3_sigHeadStrikesAttempted"] = rC_rd3_sigHeadStrikesAttempted

            item["rC_rd3_sigBodyStrikesLanded"] = rC_rd3_sigBodyStrikesLanded
            item["rC_rd3_sigBodyStrikesAttempted"] = rC_rd3_sigBodyStrikesAttempted

            item["rC_rd3_sigLegStrikesLanded"] = rC_rd3_sigLegStrikesLanded
            item["rC_rd3_sigLegStrikesAttempted"] = rC_rd3_sigLegStrikesAttempted

            item["rC_rd3_sigStrikesDistanceAttempted"] = rC_rd3_sigStrikesDistanceAttempted
            item["rC_rd3_sigStrikesDistanceLanded"] = rC_rd3_sigStrikesDistanceLanded

            item["rC_rd3_sigStrikesClinchLanded"] = rC_rd3_sigStrikesClinchLanded
            item["rC_rd3_sigStrikesClinchAttempted"] = rC_rd3_sigStrikesClinchAttempted

            item["rC_rd3_sigStrikesGroundLanded"] = rC_rd3_sigStrikesGroundLanded
            item["rC_rd3_sigStrikesGroundAttempted"] = rC_rd3_sigStrikesGroundAttempted

            item["rC_rd3_takedownsLanded"] = rC_rd3_takedownsLanded
            item["rC_rd3_takedownsAttempted"] = rC_rd3_takedownsAttempted
            # item["rC_rd3_takedownPercentage"] = rC_rd3_takedownPercentage
            item["rC_rd3_submissionAttempts"] = rC_rd3_submissionAttempts
            item["rC_rd3_passes"] = rC_rd3_passes
            item["rC_rd3_reversals"] = rC_rd3_reversals

        ##rd 4##
        if roundFinish >= 4:
            item["rC_rd4_knockdowns"] = rC_rd4_knockdowns
            item["rC_rd4_ttlStrikesLanded"] = rC_rd4_ttlStrikesLanded
            item["rC_rd4_ttlStrikesAttempted"] = rC_rd4_ttlStrikesAttempted

            item["rC_rd4_ttlSigStrikesLanded"] = rC_rd4_ttlSigStrikesLanded
            item["rC_rd4_ttlSigStrikesAttempted"] = rC_rd4_ttlSigStrikesAttempted

            item["rC_rd4_sigHeadStrikesLanded"] = rC_rd4_sigHeadStrikesLanded
            item["rC_rd4_sigHeadStrikesAttempted"] = rC_rd4_sigHeadStrikesAttempted

            item["rC_rd4_sigBodyStrikesLanded"] = rC_rd4_sigBodyStrikesLanded
            item["rC_rd4_sigBodyStrikesAttempted"] = rC_rd4_sigBodyStrikesAttempted

            item["rC_rd4_sigLegStrikesLanded"] = rC_rd4_sigLegStrikesLanded
            item["rC_rd4_sigLegStrikesAttempted"] = rC_rd4_sigLegStrikesAttempted

            item["rC_rd4_sigStrikesDistanceAttempted"] = rC_rd4_sigStrikesDistanceAttempted
            item["rC_rd4_sigStrikesDistanceLanded"] = rC_rd4_sigStrikesDistanceLanded

            item["rC_rd4_sigStrikesClinchLanded"] = rC_rd4_sigStrikesClinchLanded
            item["rC_rd4_sigStrikesClinchAttempted"] = rC_rd4_sigStrikesClinchAttempted

            item["rC_rd4_sigStrikesGroundLanded"] = rC_rd4_sigStrikesGroundLanded
            item["rC_rd4_sigStrikesGroundAttempted"] = rC_rd4_sigStrikesGroundAttempted

            item["rC_rd4_takedownsLanded"] = rC_rd4_takedownsLanded
            item["rC_rd4_takedownsAttempted"] = rC_rd4_takedownsAttempted
            # item["rC_rd4_takedownPercentage"] = rC_rd4_takedownPercentage
            item["rC_rd4_submissionAttempts"] = rC_rd4_submissionAttempts
            item["rC_rd4_passes"] = rC_rd4_passes
            item["rC_rd4_reversals"] = rC_rd4_reversals

        ##rd 5##
        if roundFinish >= 5:
            item["rC_rd5_knockdowns"] = rC_rd5_knockdowns
            item["rC_rd5_ttlStrikesLanded"] = rC_rd5_ttlStrikesLanded
            item["rC_rd5_ttlStrikesAttempted"] = rC_rd5_ttlStrikesAttempted

            item["rC_rd5_ttlSigStrikesLanded"] = rC_rd5_ttlSigStrikesLanded
            item["rC_rd5_ttlSigStrikesAttempted"] = rC_rd5_ttlSigStrikesAttempted

            item["rC_rd5_sigHeadStrikesLanded"] = rC_rd5_sigHeadStrikesLanded
            item["rC_rd5_sigHeadStrikesAttempted"] = rC_rd5_sigHeadStrikesAttempted

            item["rC_rd5_sigBodyStrikesLanded"] = rC_rd5_sigBodyStrikesLanded
            item["rC_rd5_sigBodyStrikesAttempted"] = rC_rd5_sigBodyStrikesAttempted

            item["rC_rd5_sigLegStrikesLanded"] = rC_rd5_sigLegStrikesLanded
            item["rC_rd5_sigLegStrikesAttempted"] = rC_rd5_sigLegStrikesAttempted

            item["rC_rd5_sigStrikesDistanceAttempted"] = rC_rd5_sigStrikesDistanceAttempted
            item["rC_rd5_sigStrikesDistanceLanded"] = rC_rd5_sigStrikesDistanceLanded

            item["rC_rd5_sigStrikesClinchLanded"] = rC_rd5_sigStrikesClinchLanded
            item["rC_rd5_sigStrikesClinchAttempted"] = rC_rd5_sigStrikesClinchAttempted

            item["rC_rd5_sigStrikesGroundLanded"] = rC_rd5_sigStrikesGroundLanded
            item["rC_rd5_sigStrikesGroundAttempted"] = rC_rd5_sigStrikesGroundAttempted

            item["rC_rd5_takedownsLanded"] = rC_rd5_takedownsLanded
            item["rC_rd5_takedownsAttempted"] = rC_rd5_takedownsAttempted
            # item["rC_rd5_takedownPercentage"] = rC_rd5_takedownPercentage
            item["rC_rd5_submissionAttempts"] = rC_rd5_submissionAttempts
            item["rC_rd5_passes"] = rC_rd5_passes
            item["rC_rd5_reversals"] = rC_rd5_reversals


        ##blue corner fighter details items##
        item["bC_Name"] = bC_Name
        item["bC_Result"] = bRaA.Result
        item["bC_perfBonusBool"] = bRaA.perfBonusBool
        item["bC_perfBonusBin"] = bRaA.perfBonusBin
        item["bC_subBonusBool"] = bRaA.subBonusBool
        item["bC_subBonusBin"] = bRaA.subBonusBin
        item["bC_koBonusBool"] = bRaA.koBonusBool
        item["bC_koBonusBin"] = bRaA.koBonusBin

        ##blue corner fight stats items##
        item["bC_knockdowns"] = bC_knockdowns
        item["bC_ttlStrikesLanded"] = bC_ttlStrikesLanded
        item["bC_ttlStrikesAttempted"] = bC_ttlStrikesAttempted

        item["bC_ttlSigStrikesLanded"] = bC_ttlSigStrikesLanded
        item["bC_ttlSigStrikesAttempted"] = bC_ttlSigStrikesAttempted

        item["bC_sigHeadStrikesLanded"] = bC_sigHeadStrikesLanded
        item["bC_sigHeadStrikesAttempted"] = bC_sigHeadStrikesAttempted

        item["bC_sigBodyStrikesLanded"] = bC_sigBodyStrikesLanded
        item["bC_sigBodyStrikesAttempted"] = bC_sigBodyStrikesAttempted

        item["bC_sigLegStrikesLanded"] = bC_sigLegStrikesLanded
        item["bC_sigLegStrikesAttempted"] = bC_sigLegStrikesAttempted

        item["bC_sigStrikesDistanceAttempted"] = bC_sigStrikesDistanceAttempted
        item["bC_sigStrikesDistanceLanded"] = bC_sigStrikesDistanceLanded

        item["bC_sigStrikesClinchLanded"] = bC_sigStrikesClinchLanded
        item["bC_sigStrikesClinchAttempted"] = bC_sigStrikesClinchAttempted

        item["bC_sigStrikesGroundLanded"] = bC_sigStrikesGroundLanded
        item["bC_sigStrikesGroundAttempted"] = bC_sigStrikesGroundAttempted

        item["bC_takedownsLanded"] = bC_takedownsLanded
        item["bC_takedownsAttempted"] = bC_takedownsAttempted
        # item["bC_takedownPercentage"] = bC_takedownPercentage
        item["bC_submissionAttempts"] = bC_submissionAttempts
        item["bC_passes"] = bC_passes
        item["bC_reversals"] = bC_reversals

        ##rd 1##
        item["bC_rd1_knockdowns"] = bC_rd1_knockdowns
        item["bC_rd1_ttlStrikesLanded"] = bC_rd1_ttlStrikesLanded
        item["bC_rd1_ttlStrikesAttempted"] = bC_rd1_ttlStrikesAttempted

        item["bC_rd1_ttlSigStrikesLanded"] = bC_rd1_ttlSigStrikesLanded
        item["bC_rd1_ttlSigStrikesAttempted"] = bC_rd1_ttlSigStrikesAttempted

        item["bC_rd1_sigHeadStrikesLanded"] = bC_rd1_sigHeadStrikesLanded
        item["bC_rd1_sigHeadStrikesAttempted"] = bC_rd1_sigHeadStrikesAttempted

        item["bC_rd1_sigBodyStrikesLanded"] = bC_rd1_sigBodyStrikesLanded
        item["bC_rd1_sigBodyStrikesAttempted"] = bC_rd1_sigBodyStrikesAttempted

        item["bC_rd1_sigLegStrikesLanded"] = bC_rd1_sigLegStrikesLanded
        item["bC_rd1_sigLegStrikesAttempted"] = bC_rd1_sigLegStrikesAttempted

        item["bC_rd1_sigStrikesDistanceAttempted"] = bC_rd1_sigStrikesDistanceAttempted
        item["bC_rd1_sigStrikesDistanceLanded"] = bC_rd1_sigStrikesDistanceLanded

        item["bC_rd1_sigStrikesClinchLanded"] = bC_rd1_sigStrikesClinchLanded
        item["bC_rd1_sigStrikesClinchAttempted"] = bC_rd1_sigStrikesClinchAttempted

        item["bC_rd1_sigStrikesGroundLanded"] = bC_rd1_sigStrikesGroundLanded
        item["bC_rd1_sigStrikesGroundAttempted"] = bC_rd1_sigStrikesGroundAttempted

        item["bC_rd1_takedownsLanded"] = bC_rd1_takedownsLanded
        item["bC_rd1_takedownsAttempted"] = bC_rd1_takedownsAttempted
        # item["bC_rd1_takedownPercentage"] = bC_rd1_takedownPercentage
        item["bC_rd1_submissionAttempts"] = bC_rd1_submissionAttempts
        item["bC_rd1_passes"] = bC_rd1_passes
        item["bC_rd1_reversals"] = bC_rd1_reversals

        ##rd 2##
        if roundFinish >= 2:
            item["bC_rd2_knockdowns"] = bC_rd2_knockdowns
            item["bC_rd2_ttlStrikesLanded"] = bC_rd2_ttlStrikesLanded
            item["bC_rd2_ttlStrikesAttempted"] = bC_rd2_ttlStrikesAttempted

            item["bC_rd2_ttlSigStrikesLanded"] = bC_rd2_ttlSigStrikesLanded
            item["bC_rd2_ttlSigStrikesAttempted"] = bC_rd2_ttlSigStrikesAttempted

            item["bC_rd2_sigHeadStrikesLanded"] = bC_rd2_sigHeadStrikesLanded
            item["bC_rd2_sigHeadStrikesAttempted"] = bC_rd2_sigHeadStrikesAttempted

            item["bC_rd2_sigBodyStrikesLanded"] = bC_rd2_sigBodyStrikesLanded
            item["bC_rd2_sigBodyStrikesAttempted"] = bC_rd2_sigBodyStrikesAttempted

            item["bC_rd2_sigLegStrikesLanded"] = bC_rd2_sigLegStrikesLanded
            item["bC_rd2_sigLegStrikesAttempted"] = bC_rd2_sigLegStrikesAttempted

            item["bC_rd2_sigStrikesDistanceAttempted"] = bC_rd2_sigStrikesDistanceAttempted
            item["bC_rd2_sigStrikesDistanceLanded"] = bC_rd2_sigStrikesDistanceLanded

            item["bC_rd2_sigStrikesClinchLanded"] = bC_rd2_sigStrikesClinchLanded
            item["bC_rd2_sigStrikesClinchAttempted"] = bC_rd2_sigStrikesClinchAttempted

            item["bC_rd2_sigStrikesGroundLanded"] = bC_rd2_sigStrikesGroundLanded
            item["bC_rd2_sigStrikesGroundAttempted"] = bC_rd2_sigStrikesGroundAttempted

            item["bC_rd2_takedownsLanded"] = bC_rd2_takedownsLanded
            item["bC_rd2_takedownsAttempted"] = bC_rd2_takedownsAttempted
            # item["bC_rd2_takedownPercentage"] = bC_rd2_takedownPercentage
            item["bC_rd2_submissionAttempts"] = bC_rd2_submissionAttempts
            item["bC_rd2_passes"] = bC_rd2_passes
            item["bC_rd2_reversals"] = bC_rd2_reversals

        ##rd 3##
        if roundFinish >= 3:
            item["bC_rd3_knockdowns"] = bC_rd3_knockdowns
            item["bC_rd3_ttlStrikesLanded"] = bC_rd3_ttlStrikesLanded
            item["bC_rd3_ttlStrikesAttempted"] = bC_rd3_ttlStrikesAttempted

            item["bC_rd3_ttlSigStrikesLanded"] = bC_rd3_ttlSigStrikesLanded
            item["bC_rd3_ttlSigStrikesAttempted"] = bC_rd3_ttlSigStrikesAttempted

            item["bC_rd3_sigHeadStrikesLanded"] = bC_rd3_sigHeadStrikesLanded
            item["bC_rd3_sigHeadStrikesAttempted"] = bC_rd3_sigHeadStrikesAttempted

            item["bC_rd3_sigBodyStrikesLanded"] = bC_rd3_sigBodyStrikesLanded
            item["bC_rd3_sigBodyStrikesAttempted"] = bC_rd3_sigBodyStrikesAttempted

            item["bC_rd3_sigLegStrikesLanded"] = bC_rd3_sigLegStrikesLanded
            item["bC_rd3_sigLegStrikesAttempted"] = bC_rd3_sigLegStrikesAttempted

            item["bC_rd3_sigStrikesDistanceAttempted"] = bC_rd3_sigStrikesDistanceAttempted
            item["bC_rd3_sigStrikesDistanceLanded"] = bC_rd3_sigStrikesDistanceLanded

            item["bC_rd3_sigStrikesClinchLanded"] = bC_rd3_sigStrikesClinchLanded
            item["bC_rd3_sigStrikesClinchAttempted"] = bC_rd3_sigStrikesClinchAttempted

            item["bC_rd3_sigStrikesGroundLanded"] = bC_rd3_sigStrikesGroundLanded
            item["bC_rd3_sigStrikesGroundAttempted"] = bC_rd3_sigStrikesGroundAttempted

            item["bC_rd3_takedownsLanded"] = bC_rd3_takedownsLanded
            item["bC_rd3_takedownsAttempted"] = bC_rd3_takedownsAttempted
            # item["bC_rd3_takedownPercentage"] = bC_rd3_takedownPercentage
            item["bC_rd3_submissionAttempts"] = bC_rd3_submissionAttempts
            item["bC_rd3_passes"] = bC_rd3_passes
            item["bC_rd3_reversals"] = bC_rd3_reversals

        ##rd 4##
        if roundFinish >= 4:
            item["bC_rd4_knockdowns"] = bC_rd4_knockdowns
            item["bC_rd4_ttlStrikesLanded"] = bC_rd4_ttlStrikesLanded
            item["bC_rd4_ttlStrikesAttempted"] = bC_rd4_ttlStrikesAttempted

            item["bC_rd4_ttlSigStrikesLanded"] = bC_rd4_ttlSigStrikesLanded
            item["bC_rd4_ttlSigStrikesAttempted"] = bC_rd4_ttlSigStrikesAttempted

            item["bC_rd4_sigHeadStrikesLanded"] = bC_rd4_sigHeadStrikesLanded
            item["bC_rd4_sigHeadStrikesAttempted"] = bC_rd4_sigHeadStrikesAttempted

            item["bC_rd4_sigBodyStrikesLanded"] = bC_rd4_sigBodyStrikesLanded
            item["bC_rd4_sigBodyStrikesAttempted"] = bC_rd4_sigBodyStrikesAttempted

            item["bC_rd4_sigLegStrikesLanded"] = bC_rd4_sigLegStrikesLanded
            item["bC_rd4_sigLegStrikesAttempted"] = bC_rd4_sigLegStrikesAttempted

            item["bC_rd4_sigStrikesDistanceAttempted"] = bC_rd4_sigStrikesDistanceAttempted
            item["bC_rd4_sigStrikesDistanceLanded"] = bC_rd4_sigStrikesDistanceLanded

            item["bC_rd4_sigStrikesClinchLanded"] = bC_rd4_sigStrikesClinchLanded
            item["bC_rd4_sigStrikesClinchAttempted"] = bC_rd4_sigStrikesClinchAttempted

            item["bC_rd4_sigStrikesGroundLanded"] = bC_rd4_sigStrikesGroundLanded
            item["bC_rd4_sigStrikesGroundAttempted"] = bC_rd4_sigStrikesGroundAttempted

            item["bC_rd4_takedownsLanded"] = bC_rd4_takedownsLanded
            item["bC_rd4_takedownsAttempted"] = bC_rd4_takedownsAttempted
            # item["bC_rd4_takedownPercentage"] = bC_rd4_takedownPercentage
            item["bC_rd4_submissionAttempts"] = bC_rd4_submissionAttempts
            item["bC_rd4_passes"] = bC_rd4_passes
            item["bC_rd4_reversals"] = bC_rd4_reversals

        ##rd 5##
        if roundFinish >= 5:
            item["bC_rd5_knockdowns"] = bC_rd5_knockdowns
            item["bC_rd5_ttlStrikesLanded"] = bC_rd5_ttlStrikesLanded
            item["bC_rd5_ttlStrikesAttempted"] = bC_rd5_ttlStrikesAttempted

            item["bC_rd5_ttlSigStrikesLanded"] = bC_rd5_ttlSigStrikesLanded
            item["bC_rd5_ttlSigStrikesAttempted"] = bC_rd5_ttlSigStrikesAttempted

            item["bC_rd5_sigHeadStrikesLanded"] = bC_rd5_sigHeadStrikesLanded
            item["bC_rd5_sigHeadStrikesAttempted"] = bC_rd5_sigHeadStrikesAttempted

            item["bC_rd5_sigBodyStrikesLanded"] = bC_rd5_sigBodyStrikesLanded
            item["bC_rd5_sigBodyStrikesAttempted"] = bC_rd5_sigBodyStrikesAttempted

            item["bC_rd5_sigLegStrikesLanded"] = bC_rd5_sigLegStrikesLanded
            item["bC_rd5_sigLegStrikesAttempted"] = bC_rd5_sigLegStrikesAttempted

            item["bC_rd5_sigStrikesDistanceAttempted"] = bC_rd5_sigStrikesDistanceAttempted
            item["bC_rd5_sigStrikesDistanceLanded"] = bC_rd5_sigStrikesDistanceLanded

            item["bC_rd5_sigStrikesClinchLanded"] = bC_rd5_sigStrikesClinchLanded
            item["bC_rd5_sigStrikesClinchAttempted"] = bC_rd5_sigStrikesClinchAttempted

            item["bC_rd5_sigStrikesGroundLanded"] = bC_rd5_sigStrikesGroundLanded
            item["bC_rd5_sigStrikesGroundAttempted"] = bC_rd5_sigStrikesGroundAttempted

            item["bC_rd5_takedownsLanded"] = bC_rd5_takedownsLanded
            item["bC_rd5_takedownsAttempted"] = bC_rd5_takedownsAttempted
            # item["bC_rd5_takedownPercentage"] = bC_rd5_takedownPercentage
            item["bC_rd5_submissionAttempts"] = bC_rd5_submissionAttempts
            item["bC_rd5_passes"] = bC_rd5_passes
            item["bC_rd5_reversals"] = bC_rd5_reversals


        item["rC_SLpM"] = rC_SLpM
        item["rC_StrAcc"] = rC_StrAcc
        item["rC_SApM"] = rC_SApM
        item["rC_StrDef"] = rC_StrDef
        item["rC_TDAcc"] = rC_TDAcc
        item["rC_TDDef"] = rC_TDDef
        item["rC_SigStrDif"] = rC_SigStrDif

        item["bC_SLpM"] = bC_SLpM
        item["bC_StrAcc"] = bC_StrAcc
        item["bC_SApM"] = bC_SApM
        item["bC_StrDef"] = bC_StrDef
        item["bC_TDAcc"] = bC_TDAcc
        item["bC_TDDef"] = bC_TDDef
        item["bC_SigStrDif"] = bC_SigStrDif

        yield item

