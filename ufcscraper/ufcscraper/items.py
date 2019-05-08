# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UFCscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ####EVENT DETAIL ITEMS####
    eventName = scrapy.Field()


    ####FIGHT DETAIL ITEMS####
    titleFightBool = scrapy.Field()
    titleFightBin = scrapy.Field()
    fightGender = scrapy.Field()
    Division = scrapy.Field()
    Lower_Limit_lbs = scrapy.Field()
    Upper_Limit_lbs = scrapy.Field()
    Lower_Limit_kg = scrapy.Field()
    Upper_Limit_kg = scrapy.Field()
    fotnBonusBool = scrapy.Field()
    fotnBonusBin = scrapy.Field()
    method = scrapy.Field()
    roundFinish = scrapy.Field()
    timeFinish = scrapy.Field()
    ttlFightTime = scrapy.Field()
    numRoundFormat = scrapy.Field()
    referee = scrapy.Field()
    finishDetails = scrapy.Field()
    judge1 = scrapy.Field()
    judge1RedPts = scrapy.Field()
    judge1BluePts = scrapy.Field()
    judge2 = scrapy.Field()
    judge2RedPts = scrapy.Field()
    judge2BluePts = scrapy.Field()
    judge3 = scrapy.Field()
    judge3RedPts = scrapy.Field()
    judge3BluePts = scrapy.Field()

    ####RED CORNER FIGHTER DETAILS ITEMS####
    rC_Name = scrapy.Field()
    rC_Result = scrapy.Field()
    rC_perfBonusBool = scrapy.Field()
    rC_perfBonusBin = scrapy.Field()
    rC_subBonusBool = scrapy.Field()
    rC_subBonusBin = scrapy.Field()
    rC_koBonusBool = scrapy.Field()
    rC_koBonusBin = scrapy.Field()

    ####RED CORNER FIGHT STATS ITEMS####

    ###RED CORNER DESCRIPTIVE STATS###
    rC_SLpM = scrapy.Field()
    rC_StrAcc = scrapy.Field()
    rC_SApM = scrapy.Field()
    rC_StrDef = scrapy.Field()
    rC_TDAcc = scrapy.Field()
    rC_TDDef = scrapy.Field()
    rC_SigStrDif = scrapy.Field()

    ###TOTAL FIGHT STATS###

    ##TOTAL STRIKING STATS##
    rC_knockdowns = scrapy.Field()
    rC_ttlStrikesLanded = scrapy.Field()
    rC_ttlStrikesAttempted = scrapy.Field()

    ##TOTAL SIGNIFICANT STRIKING STATS##
    rC_ttlSigStrikesLanded = scrapy.Field()
    rC_ttlSigStrikesAttempted = scrapy.Field()


    #TOTAL SIG STRIKES BY TARGET#
    #head#
    rC_sigHeadStrikesAttempted = scrapy.Field()
    rC_sigHeadStrikesLanded = scrapy.Field()
    #body#
    rC_sigBodyStrikesAttempted = scrapy.Field()
    rC_sigBodyStrikesLanded = scrapy.Field()
    #leg#
    rC_sigLegStrikesAttempted = scrapy.Field()
    rC_sigLegStrikesLanded = scrapy.Field()

    #TOTAL SIG STRIKES BY POSITION#
    #distance#
    rC_sigStrikesDistanceAttempted = scrapy.Field()
    rC_sigStrikesDistanceLanded = scrapy.Field()
    #clinch#
    rC_sigStrikesClinchAttempted = scrapy.Field()
    rC_sigStrikesClinchLanded = scrapy.Field()
    #ground#
    rC_sigStrikesGroundAttempted = scrapy.Field()
    rC_sigStrikesGroundLanded = scrapy.Field()


    ##TOTAL GRAPPLING STATS##
    rC_takedownsLanded = scrapy.Field()
    rC_takedownsAttempted = scrapy.Field()
    rC_takedownPercentage = scrapy.Field()
    rC_submissionAttempts = scrapy.Field()
    rC_passes = scrapy.Field()
    rC_reversals = scrapy.Field()

    ###TOTAL STATS BY ROUND###
    ##ROUND 1##

    #STRIKING#
    rC_rd1_knockdowns = scrapy.Field()
    rC_rd1_ttlStrikesLanded = scrapy.Field()
    rC_rd1_ttlStrikesAttempted = scrapy.Field()

    #SIGNIFICANT STRIKING#
    rC_rd1_ttlSigStrikesLanded = scrapy.Field()
    rC_rd1_ttlSigStrikesAttempted = scrapy.Field()


    #Sig Strikes by Target#
    #head#
    rC_rd1_sigHeadStrikesAttempted = scrapy.Field()
    rC_rd1_sigHeadStrikesLanded = scrapy.Field()
    #body#
    rC_rd1_sigBodyStrikesAttempted = scrapy.Field()
    rC_rd1_sigBodyStrikesLanded = scrapy.Field()
    #leg#
    rC_rd1_sigLegStrikesLanded = scrapy.Field()
    rC_rd1_sigLegStrikesAttempted = scrapy.Field()

    #Sig Strikes by Position#
    #distance#
    rC_rd1_sigStrikesDistanceLanded = scrapy.Field()
    rC_rd1_sigStrikesDistanceAttempted = scrapy.Field()
    #clinch#
    rC_rd1_sigStrikesClinchLanded = scrapy.Field()
    rC_rd1_sigStrikesClinchAttempted = scrapy.Field()
    #ground#
    rC_rd1_sigStrikesGroundLanded = scrapy.Field()
    rC_rd1_sigStrikesGroundAttempted = scrapy.Field()

    #GRAPPLING#
    rC_rd1_takedownsLanded = scrapy.Field()
    rC_rd1_takedownsAttempted = scrapy.Field()
    rC_rd1_takedownSuccPercentage = scrapy.Field()
    rC_rd1_submissionAttempts = scrapy.Field()
    rC_rd1_passes = scrapy.Field()
    rC_rd1_reversals = scrapy.Field()

    ##ROUND 2##

    # STRIKING#
    rC_rd2_knockdowns = scrapy.Field()
    rC_rd2_ttlStrikesLanded = scrapy.Field()
    rC_rd2_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    rC_rd2_ttlSigStrikesLanded = scrapy.Field()
    rC_rd2_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    rC_rd2_sigHeadStrikesAttempted = scrapy.Field()
    rC_rd2_sigHeadStrikesLanded = scrapy.Field()
    # body#
    rC_rd2_sigBodyStrikesAttempted = scrapy.Field()
    rC_rd2_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    rC_rd2_sigLegStrikesLanded = scrapy.Field()
    rC_rd2_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    rC_rd2_sigStrikesDistanceLanded = scrapy.Field()
    rC_rd2_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    rC_rd2_sigStrikesClinchLanded = scrapy.Field()
    rC_rd2_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    rC_rd2_sigStrikesGroundLanded = scrapy.Field()
    rC_rd2_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    rC_rd2_takedownsLanded = scrapy.Field()
    rC_rd2_takedownsAttempted = scrapy.Field()
    rC_rd2_takedownSuccPercentage = scrapy.Field()
    rC_rd2_submissionAttempts = scrapy.Field()
    rC_rd2_passes = scrapy.Field()
    rC_rd2_reversals = scrapy.Field()

    ##ROUND 3##

    # STRIKING#
    rC_rd3_knockdowns = scrapy.Field()
    rC_rd3_ttlStrikesLanded = scrapy.Field()
    rC_rd3_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    rC_rd3_ttlSigStrikesLanded = scrapy.Field()
    rC_rd3_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    rC_rd3_sigHeadStrikesAttempted = scrapy.Field()
    rC_rd3_sigHeadStrikesLanded = scrapy.Field()
    # body#
    rC_rd3_sigBodyStrikesAttempted = scrapy.Field()
    rC_rd3_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    rC_rd3_sigLegStrikesLanded = scrapy.Field()
    rC_rd3_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    rC_rd3_sigStrikesDistanceLanded = scrapy.Field()
    rC_rd3_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    rC_rd3_sigStrikesClinchLanded = scrapy.Field()
    rC_rd3_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    rC_rd3_sigStrikesGroundLanded = scrapy.Field()
    rC_rd3_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    rC_rd3_takedownsLanded = scrapy.Field()
    rC_rd3_takedownsAttempted = scrapy.Field()
    rC_rd3_takedownSuccPercentage = scrapy.Field()
    rC_rd3_submissionAttempts = scrapy.Field()
    rC_rd3_passes = scrapy.Field()
    rC_rd3_reversals = scrapy.Field()

    ##ROUND 4##

    # STRIKING#
    rC_rd4_knockdowns = scrapy.Field()
    rC_rd4_ttlStrikesLanded = scrapy.Field()
    rC_rd4_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    rC_rd4_ttlSigStrikesLanded = scrapy.Field()
    rC_rd4_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    rC_rd4_sigHeadStrikesAttempted = scrapy.Field()
    rC_rd4_sigHeadStrikesLanded = scrapy.Field()
    # body#
    rC_rd4_sigBodyStrikesAttempted = scrapy.Field()
    rC_rd4_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    rC_rd4_sigLegStrikesLanded = scrapy.Field()
    rC_rd4_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    rC_rd4_sigStrikesDistanceLanded = scrapy.Field()
    rC_rd4_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    rC_rd4_sigStrikesClinchLanded = scrapy.Field()
    rC_rd4_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    rC_rd4_sigStrikesGroundLanded = scrapy.Field()
    rC_rd4_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    rC_rd4_takedownsLanded = scrapy.Field()
    rC_rd4_takedownsAttempted = scrapy.Field()
    rC_rd4_takedownSuccPercentage = scrapy.Field()
    rC_rd4_submissionAttempts = scrapy.Field()
    rC_rd4_passes = scrapy.Field()
    rC_rd4_reversals = scrapy.Field()

    ##ROUND 5##

    # STRIKING#
    rC_rd5_knockdowns = scrapy.Field()
    rC_rd5_ttlStrikesLanded = scrapy.Field()
    rC_rd5_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    rC_rd5_ttlSigStrikesLanded = scrapy.Field()
    rC_rd5_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    rC_rd5_sigHeadStrikesAttempted = scrapy.Field()
    rC_rd5_sigHeadStrikesLanded = scrapy.Field()
    # body#
    rC_rd5_sigBodyStrikesAttempted = scrapy.Field()
    rC_rd5_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    rC_rd5_sigLegStrikesLanded = scrapy.Field()
    rC_rd5_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    rC_rd5_sigStrikesDistanceLanded = scrapy.Field()
    rC_rd5_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    rC_rd5_sigStrikesClinchLanded = scrapy.Field()
    rC_rd5_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    rC_rd5_sigStrikesGroundLanded = scrapy.Field()
    rC_rd5_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    rC_rd5_takedownsLanded = scrapy.Field()
    rC_rd5_takedownsAttempted = scrapy.Field()
    rC_rd5_takedownSuccPercentage = scrapy.Field()
    rC_rd5_submissionAttempts = scrapy.Field()
    rC_rd5_passes = scrapy.Field()
    rC_rd5_reversals = scrapy.Field()

#########################################################################

    ####BLUE CORNER FIGHTER DETAILS ITEMS####
    bC_Name = scrapy.Field()
    bC_Result = scrapy.Field()
    bC_perfBonusBool = scrapy.Field()
    bC_perfBonusBin = scrapy.Field()
    bC_subBonusBool = scrapy.Field()
    bC_subBonusBin = scrapy.Field()
    bC_koBonusBool = scrapy.Field()
    bC_koBonusBin = scrapy.Field()

    ####BLUE CORNER FIGHT STATS ITEMS####
    ###BLUE CORNER DESCRIPTIVE STATS###
    bC_SLpM = scrapy.Field()
    bC_StrAcc = scrapy.Field()
    bC_SApM = scrapy.Field()
    bC_StrDef = scrapy.Field()
    bC_TDAcc = scrapy.Field()
    bC_TDDef = scrapy.Field()
    bC_SigStrDif = scrapy.Field()


    ###TOTAL FIGHT STATS###

    ##TOTAL STRIKING STATS##
    bC_knockdowns = scrapy.Field()
    bC_ttlStrikesLanded = scrapy.Field()
    bC_ttlStrikesAttempted = scrapy.Field()

    ##TOTAL SIGNIFICANT STRIKING STATS##
    bC_ttlSigStrikesLanded = scrapy.Field()
    bC_ttlSigStrikesAttempted = scrapy.Field()


    # TOTAL SIG STRIKES BY TARGET#
    # head#
    bC_sigHeadStrikesAttempted = scrapy.Field()
    bC_sigHeadStrikesLanded = scrapy.Field()
    # body#
    bC_sigBodyStrikesAttempted = scrapy.Field()
    bC_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    bC_sigLegStrikesAttempted = scrapy.Field()
    bC_sigLegStrikesLanded = scrapy.Field()

    # TOTAL SIG STRIKES BY POSITION#
    # distance#
    bC_sigStrikesDistanceAttempted = scrapy.Field()
    bC_sigStrikesDistanceLanded = scrapy.Field()
    # clinch#
    bC_sigStrikesClinchAttempted = scrapy.Field()
    bC_sigStrikesClinchLanded = scrapy.Field()
    # ground#
    bC_sigStrikesGroundAttempted = scrapy.Field()
    bC_sigStrikesGroundLanded = scrapy.Field()

    ##TOTAL GRAPPLING STATS##
    bC_takedownsLanded = scrapy.Field()
    bC_takedownsAttempted = scrapy.Field()
    bC_takedownPercentage = scrapy.Field()
    bC_submissionAttempts = scrapy.Field()
    bC_passes = scrapy.Field()
    bC_reversals = scrapy.Field()

    ###TOTAL STATS BY ROUND###
    ##ROUND 1##

    # STRIKING#
    bC_rd1_knockdowns = scrapy.Field()
    bC_rd1_ttlStrikesLanded = scrapy.Field()
    bC_rd1_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    bC_rd1_ttlSigStrikesLanded = scrapy.Field()
    bC_rd1_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    bC_rd1_sigHeadStrikesAttempted = scrapy.Field()
    bC_rd1_sigHeadStrikesLanded = scrapy.Field()
    # body#
    bC_rd1_sigBodyStrikesAttempted = scrapy.Field()
    bC_rd1_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    bC_rd1_sigLegStrikesLanded = scrapy.Field()
    bC_rd1_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    bC_rd1_sigStrikesDistanceLanded = scrapy.Field()
    bC_rd1_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    bC_rd1_sigStrikesClinchLanded = scrapy.Field()
    bC_rd1_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    bC_rd1_sigStrikesGroundLanded = scrapy.Field()
    bC_rd1_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    bC_rd1_takedownsLanded = scrapy.Field()
    bC_rd1_takedownsAttempted = scrapy.Field()
    bC_rd1_takedownSuccPercentage = scrapy.Field()
    bC_rd1_submissionAttempts = scrapy.Field()
    bC_rd1_passes = scrapy.Field()
    bC_rd1_reversals = scrapy.Field()

    ##ROUND 2##

    # STRIKING#
    bC_rd2_knockdowns = scrapy.Field()
    bC_rd2_ttlStrikesLanded = scrapy.Field()
    bC_rd2_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    bC_rd2_ttlSigStrikesLanded = scrapy.Field()
    bC_rd2_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    bC_rd2_sigHeadStrikesAttempted = scrapy.Field()
    bC_rd2_sigHeadStrikesLanded = scrapy.Field()
    # body#
    bC_rd2_sigBodyStrikesAttempted = scrapy.Field()
    bC_rd2_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    bC_rd2_sigLegStrikesLanded = scrapy.Field()
    bC_rd2_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    bC_rd2_sigStrikesDistanceLanded = scrapy.Field()
    bC_rd2_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    bC_rd2_sigStrikesClinchLanded = scrapy.Field()
    bC_rd2_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    bC_rd2_sigStrikesGroundLanded = scrapy.Field()
    bC_rd2_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    bC_rd2_takedownsLanded = scrapy.Field()
    bC_rd2_takedownsAttempted = scrapy.Field()
    bC_rd2_takedownSuccPercentage = scrapy.Field()
    bC_rd2_submissionAttempts = scrapy.Field()
    bC_rd2_passes = scrapy.Field()
    bC_rd2_reversals = scrapy.Field()

    ##ROUND 3##

    # STRIKING#
    bC_rd3_knockdowns = scrapy.Field()
    bC_rd3_ttlStrikesLanded = scrapy.Field()
    bC_rd3_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    bC_rd3_ttlSigStrikesLanded = scrapy.Field()
    bC_rd3_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    bC_rd3_sigHeadStrikesAttempted = scrapy.Field()
    bC_rd3_sigHeadStrikesLanded = scrapy.Field()
    # body#
    bC_rd3_sigBodyStrikesAttempted = scrapy.Field()
    bC_rd3_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    bC_rd3_sigLegStrikesLanded = scrapy.Field()
    bC_rd3_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    bC_rd3_sigStrikesDistanceLanded = scrapy.Field()
    bC_rd3_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    bC_rd3_sigStrikesClinchLanded = scrapy.Field()
    bC_rd3_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    bC_rd3_sigStrikesGroundLanded = scrapy.Field()
    bC_rd3_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    bC_rd3_takedownsLanded = scrapy.Field()
    bC_rd3_takedownsAttempted = scrapy.Field()
    bC_rd3_takedownSuccPercentage = scrapy.Field()
    bC_rd3_submissionAttempts = scrapy.Field()
    bC_rd3_passes = scrapy.Field()
    bC_rd3_reversals = scrapy.Field()

    ##ROUND 4##

    # STRIKING#
    bC_rd4_knockdowns = scrapy.Field()
    bC_rd4_ttlStrikesLanded = scrapy.Field()
    bC_rd4_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    bC_rd4_ttlSigStrikesLanded = scrapy.Field()
    bC_rd4_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    bC_rd4_sigHeadStrikesAttempted = scrapy.Field()
    bC_rd4_sigHeadStrikesLanded = scrapy.Field()
    # body#
    bC_rd4_sigBodyStrikesAttempted = scrapy.Field()
    bC_rd4_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    bC_rd4_sigLegStrikesLanded = scrapy.Field()
    bC_rd4_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    bC_rd4_sigStrikesDistanceLanded = scrapy.Field()
    bC_rd4_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    bC_rd4_sigStrikesClinchLanded = scrapy.Field()
    bC_rd4_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    bC_rd4_sigStrikesGroundLanded = scrapy.Field()
    bC_rd4_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    bC_rd4_takedownsLanded = scrapy.Field()
    bC_rd4_takedownsAttempted = scrapy.Field()
    bC_rd4_takedownSuccPercentage = scrapy.Field()
    bC_rd4_submissionAttempts = scrapy.Field()
    bC_rd4_passes = scrapy.Field()
    bC_rd4_reversals = scrapy.Field()

    ##ROUND 5##

    # STRIKING#
    bC_rd5_knockdowns = scrapy.Field()
    bC_rd5_ttlStrikesLanded = scrapy.Field()
    bC_rd5_ttlStrikesAttempted = scrapy.Field()

    # SIGNIFICANT STRIKING#
    bC_rd5_ttlSigStrikesLanded = scrapy.Field()
    bC_rd5_ttlSigStrikesAttempted = scrapy.Field()


    # Sig Strikes by Target#
    # head#
    bC_rd5_sigHeadStrikesAttempted = scrapy.Field()
    bC_rd5_sigHeadStrikesLanded = scrapy.Field()
    # body#
    bC_rd5_sigBodyStrikesAttempted = scrapy.Field()
    bC_rd5_sigBodyStrikesLanded = scrapy.Field()
    # leg#
    bC_rd5_sigLegStrikesLanded = scrapy.Field()
    bC_rd5_sigLegStrikesAttempted = scrapy.Field()

    # Sig Strikes by Position#
    # distance#
    bC_rd5_sigStrikesDistanceLanded = scrapy.Field()
    bC_rd5_sigStrikesDistanceAttempted = scrapy.Field()
    # clinch#
    bC_rd5_sigStrikesClinchLanded = scrapy.Field()
    bC_rd5_sigStrikesClinchAttempted = scrapy.Field()
    # ground#
    bC_rd5_sigStrikesGroundLanded = scrapy.Field()
    bC_rd5_sigStrikesGroundAttempted = scrapy.Field()

    # GRAPPLING#
    bC_rd5_takedownsLanded = scrapy.Field()
    bC_rd5_takedownsAttempted = scrapy.Field()
    bC_rd5_takedownSuccPercentage = scrapy.Field()
    bC_rd5_submissionAttempts = scrapy.Field()
    bC_rd5_passes = scrapy.Field()
    bC_rd5_reversals = scrapy.Field()
