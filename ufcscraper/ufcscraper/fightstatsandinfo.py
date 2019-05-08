import scrapy

class FightStats:

    fightStatsDict = {
        "red": {
            "totals": {
                "striking": {
                    "knockdowns": '//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[1]/text()',
                    "ttlStrikesLanded": '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[1]/text()',
                    "ttlStrikesAttempted": '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[1]/text()',
                    "significantStrikes": {
                        "ttlSigStrikesLanded": '//html/body/section/div/div/table/tbody/tr/td[2]/p[1]/text()',
                        "ttlSigStrikesAttempted": '//html/body/section/div/div/table/tbody/tr/td[2]/p[1]/text()',
                        "sigStrikePercentageLanded": '//html/body/section/div/div/table/tbody/tr/td[3]/p[1]/text()',
                        "sigStrikesByTarget": {
                            "head": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[4]/p[1]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[4]/p[1]/text()'
                            },
                            "body": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[5]/p[1]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[5]/p[1]/text()'
                            },
                            "leg": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[6]/p[1]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[6]/p[1]/text()'
                            }
                        },
                        "sigStrikesByPosition": {
                            "distance": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[7]/p[1]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[7]/p[1]/text()'
                            },
                            "clinch": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[8]/p[1]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[8]/p[1]/text()'
                            },
                            "ground": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[9]/p[1]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[9]/p[1]/text()'
                            }
                        }
                    }

                },
                "grappling": {
                    "takedownsLanded": '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[1]/text()',
                    "takedownsAttempted": '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[1]/text()',
                    "takedownSuccPercentage": '//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[1]/text()',
                    "submissionAttempts": '//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[1]/text()',
                    "passes": '//html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[1]/text()',
                    "reversals": '//html/body/section/div/div/section[2]/table/tbody/tr/td[10]/p[1]/text()'
                }
            },
            "byRound": {
                "round1": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//html/body/section/div/div/section[3]/table/tbody/tr/td[2]/p[1]/text()',
                            "ttlStrikesLanded": '//html/body/section/div/div/section[3]/table/tbody/tr/td[5]/p[1]/text()',
                            "ttlStrikesAttempted": '//html/body/section/div/div/section[3]/table/tbody/tr/td[5]/p[1]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//html/body/section/div/div/section[5]/table/tbody/tr/td[2]/p[1]/text()',
                                "ttlSigStrikesAttempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[2]/p[1]/text()',
                                "sigStrikePercentageLanded": '//html/body/section/div/div/section[5]/table/tbody/tr/td[3]/p[1]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[4]/p[1]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[4]/p[1]/text()'
                                    },
                                    "body": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[5]/p[1]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[5]/p[1]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[6]/p[1]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[6]/p[1]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[7]/p[1]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[7]/p[1]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[8]/p[1]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[8]/p[1]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[9]/p[1]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[9]/p[1]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//html/body/section/div/div/section[3]/table/tbody/tr/td[6]/p[1]/text()',
                            "takedownsAttempted": '//html/body/section/div/div/section[3]/table/tbody/tr/td[6]/p[1]/text()',
                            "takedownSuccPercentage": '//html/body/section/div/div/section[3]/table/tbody/tr/td[7]/p[1]/text()',
                            "submissionAttempts": '//html/body/section/div/div/section[3]/table/tbody/tr/td[8]/p[1]/text()',
                            "passes": '//html/body/section/div/div/section[3]/table/tbody/tr/td[9]/p[1]/text()',
                            "reversals": '//html/body/section/div/div/section[3]/table/tbody/tr/td[10]/p[1]/text()'
                        }
                    }
                },
                "round2": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][2]/td[2]/p[1]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[1]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[1]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][2]/td[2]/p[1]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][2]/td[2]/p[1]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][2]/td[3]/p[1]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[4]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[4]/p[1]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[1]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[1]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[7]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[7]/p[1]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[8]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[8]/p[1]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[9]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[9]/p[1]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[1]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[1]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][2]/td[7]/p[1]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][2]/td[8]/p[1]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][2]/td[9]/p[1]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][2]/td[10]/p[1]/text()'
                        }
                    }
                },
                "round3": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][3]/td[2]/p[1]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[1]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[1]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][3]/td[2]/p[1]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][3]/td[2]/p[1]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][3]/td[3]/p[1]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[4]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[4]/p[1]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[1]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[1]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[7]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[7]/p[1]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[8]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[8]/p[1]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[9]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[9]/p[1]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[1]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[1]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][3]/td[7]/p[1]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][3]/td[8]/p[1]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][3]/td[9]/p[1]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][3]/td[10]/p[1]/text()'
                        }
                    }
                },
                "round4": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][4]/td[2]/p[1]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[1]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[1]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][4]/td[2]/p[1]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][4]/td[2]/p[1]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][4]/td[3]/p[1]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[4]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[4]/p[1]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[1]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[1]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[7]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[7]/p[1]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[8]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[8]/p[1]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[9]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[9]/p[1]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[1]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[1]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][4]/td[7]/p[1]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][4]/td[8]/p[1]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][4]/td[9]/p[1]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][4]/td[10]/p[1]/text()'
                        }
                    }
                },
                "round5": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][5]/td[2]/p[1]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[1]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[1]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][5]/td[2]/p[1]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][5]/td[2]/p[1]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][5]/td[3]/p[1]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[4]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[4]/p[1]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[1]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[1]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[7]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[7]/p[1]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[8]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[8]/p[1]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[9]/p[1]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[9]/p[1]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[1]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[1]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][5]/td[7]/p[1]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][5]/td[8]/p[1]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][5]/td[9]/p[1]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][5]/td[10]/p[1]/text()'
                        }
                    }
                }
            }
        },
        "blue": {
            "totals": {
                "striking": {
                    "knockdowns": '//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[2]/text()',
                    "ttlStrikesLanded": '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[2]/text()',
                    "ttlStrikesAttempted": '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[2]/text()',
                    "significantStrikes": {
                        "ttlSigStrikesLanded": '//html/body/section/div/div/table/tbody/tr/td[2]/p[2]/text()',
                        "ttlSigStrikesAttempted": '//html/body/section/div/div/table/tbody/tr/td[2]/p[2]/text()',
                        "sigStrikePercentageLanded": '//html/body/section/div/div/table/tbody/tr/td[3]/p[2]/text()',
                        "sigStrikesByTarget": {
                            "head": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[4]/p[2]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[4]/p[2]/text()'
                            },
                            "body": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[5]/p[2]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[5]/p[2]/text()'
                            },
                            "leg": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[6]/p[2]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[6]/p[2]/text()'
                            }
                        },
                        "sigStrikesByPosition": {
                            "distance": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[7]/p[2]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[7]/p[2]/text()'
                            },
                            "clinch": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[8]/p[2]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[8]/p[2]/text()'
                            },
                            "ground": {
                                "attempted": '//html/body/section/div/div/table/tbody/tr/td[9]/p[2]/text()',
                                "landed": '//html/body/section/div/div/table/tbody/tr/td[9]/p[2]/text()'
                            }
                        }
                    }

                },
                "grappling": {
                    "takedownsLanded": '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[2]/text()',
                    "takedownsAttempted": '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[2]/text()',
                    "takedownSuccPercentage": '//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[2]/text()',
                    "submissionAttempts": '//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[2]/text()',
                    "passes": '//html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[2]/text()',
                    "reversals": '//html/body/section/div/div/section[2]/table/tbody/tr/td[10]/p[2]/text()'
                }
            },
            "byRound": {
                "round1": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//html/body/section/div/div/section[3]/table/tbody/tr/td[2]/p[2]/text()',
                            "ttlStrikesLanded": '//html/body/section/div/div/section[3]/table/tbody/tr/td[5]/p[2]/text()',
                            "ttlStrikesAttempted": '//html/body/section/div/div/section[3]/table/tbody/tr/td[5]/p[2]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//html/body/section/div/div/section[5]/table/tbody/tr/td[2]/p[2]/text()',
                                "ttlSigStrikesAttempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[2]/p[2]/text()',
                                "sigStrikePercentageLanded": '//html/body/section/div/div/section[5]/table/tbody/tr/td[3]/p[2]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[4]/p[2]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[4]/p[2]/text()'
                                    },
                                    "body": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[5]/p[2]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[5]/p[2]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[6]/p[2]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[6]/p[2]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[7]/p[2]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[7]/p[2]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[8]/p[2]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[8]/p[2]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//html/body/section/div/div/section[5]/table/tbody/tr/td[9]/p[2]/text()',
                                        "landed": '//html/body/section/div/div/section[5]/table/tbody/tr/td[9]/p[2]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//html/body/section/div/div/section[3]/table/tbody/tr/td[6]/p[2]/text()',
                            "takedownsAttempted": '//html/body/section/div/div/section[3]/table/tbody/tr/td[6]/p[2]/text()',
                            "takedownSuccPercentage": '//html/body/section/div/div/section[3]/table/tbody/tr/td[7]/p[2]/text()',
                            "submissionAttempts": '//html/body/section/div/div/section[3]/table/tbody/tr/td[8]/p[2]/text()',
                            "passes": '//html/body/section/div/div/section[3]/table/tbody/tr/td[9]/p[2]/text()',
                            "reversals": '//html/body/section/div/div/section[3]/table/tbody/tr/td[10]/p[2]/text()'
                        }
                    }
                },
                "round2": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][2]/td[2]/p[2]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[2]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[2]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][2]/td[2]/p[2]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][2]/td[2]/p[2]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][2]/td[3]/p[2]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[4]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[4]/p[2]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[5]/p[2]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[2]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[7]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[7]/p[2]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[8]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[8]/p[2]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][2]/td[9]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][2]/td[9]/p[2]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[2]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][2]/td[6]/p[2]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][2]/td[7]/p[2]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][2]/td[8]/p[2]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][2]/td[9]/p[2]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][2]/td[10]/p[2]/text()'
                        }
                    }
                },
                "round3": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][3]/td[2]/p[2]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[2]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[2]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][3]/td[2]/p[2]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][3]/td[2]/p[2]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][3]/td[3]/p[2]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[4]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[4]/p[2]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[5]/p[2]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[2]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[7]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[7]/p[2]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[8]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[8]/p[2]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][3]/td[9]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][3]/td[9]/p[2]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[2]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][3]/td[6]/p[2]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][3]/td[7]/p[2]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][3]/td[8]/p[2]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][3]/td[9]/p[2]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][3]/td[10]/p[2]/text()'
                        }
                    }
                },
                "round4": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][4]/td[2]/p[2]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[2]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[2]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][4]/td[2]/p[2]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][4]/td[2]/p[2]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][4]/td[3]/p[2]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[4]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[4]/p[2]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[5]/p[2]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[2]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[7]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[7]/p[2]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[8]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[8]/p[2]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][4]/td[9]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][4]/td[9]/p[2]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[2]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][4]/td[6]/p[2]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][4]/td[7]/p[2]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][4]/td[8]/p[2]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][4]/td[9]/p[2]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][4]/td[10]/p[2]/text()'
                        }
                    }
                },
                "round5": {
                    "totals": {
                        "striking": {
                            "knockdowns": '//tr[@class="b-fight-details__table-row"][5]/td[2]/p[2]/text()',
                            "ttlStrikesLanded": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[2]/text()',
                            "ttlStrikesAttempted": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[2]/text()',
                            "significantStrikes": {
                                "ttlSigStrikesLanded": '//tr[@class="b-fight-details__table-row"][5]/td[2]/p[2]/text()',
                                "ttlSigStrikesAttempted": '//tr[@class="b-fight-details__table-row"][5]/td[2]/p[2]/text()',
                                "sigStrikePercentageLanded": '//tr[@class="b-fight-details__table-row"][5]/td[3]/p[2]/text()',
                                "sigStrikesByTarget": {
                                    "head": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[4]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[4]/p[2]/text()'
                                    },
                                    "body": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[5]/p[2]/text()'
                                    },
                                    "leg": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[2]/text()'
                                    }
                                },
                                "sigStrikesByPosition": {
                                    "distance": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[7]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[7]/p[2]/text()'
                                    },
                                    "clinch": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[8]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[8]/p[2]/text()'
                                    },
                                    "ground": {
                                        "attempted": '//tr[@class="b-fight-details__table-row"][5]/td[9]/p[2]/text()',
                                        "landed": '//tr[@class="b-fight-details__table-row"][5]/td[9]/p[2]/text()'
                                    }
                                }
                            }
                        },
                        "grappling": {
                            "takedownsLanded": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[2]/text()',
                            "takedownsAttempted": '//tr[@class="b-fight-details__table-row"][5]/td[6]/p[2]/text()',
                            "takedownSuccPercentage": '//tr[@class="b-fight-details__table-row"][5]/td[7]/p[2]/text()',
                            "submissionAttempts": '//tr[@class="b-fight-details__table-row"][5]/td[8]/p[2]/text()',
                            "passes": '//tr[@class="b-fight-details__table-row"][5]/td[9]/p[2]/text()',
                            "reversals": '//tr[@class="b-fight-details__table-row"][5]/td[10]/p[2]/text()'
                        }
                    }
                }
            }
        }
    }


class DescriptiveStats:

    def __init__(self, DSlist):
        self.SLpM = (DSlist[0] / DSlist[8])
        if DSlist[1] is not 0:
            self.StrAcc = (DSlist[0] / DSlist[1])
        else:
            self.StrAcc = None
        if DSlist[8] is not 0:
            self.SApM = (DSlist[2] / DSlist[8])
        else:
            self.SApM = None
        if DSlist[3] is not 0:
            self.StrDef = (DSlist[2] / DSlist[3])
        else:
            self.StrDef is None
        if DSlist[5] is not 0:
            self.TDAcc = (DSlist[4] / DSlist[5])
        else:
            self.TDAcc = None
        if DSlist[7] is not 0:
            self.TDdef = (DSlist[6] / DSlist[7])
        else:
            self.TDdef = None
        self.SigStrDif = (DSlist[0] - DSlist[2])


class FightDetails:

    fightDetailsDict = {
        "method": '//html/body/section/div/div/div[2]/div[2]/p[1]/i[1]/i[2]//text()',
        "roundFinish": '//html/body/section/div/div/div[2]/div[2]/p[1]/i[2]//text()[2]',
        "timeFinish": '//html/body/section/div/div/div[2]/div[2]/p[1]/i[3]//text()[2]',
        "numRoundFormat": '//html/body/section/div/div/div[2]/div[2]/p[1]/i[4]//text()[2]',
        "referee": '//html/body/section/div/div/div[2]/div[2]/p[1]/i[5]/span//text()',
        "finishDetails": '//p[@class="b-fight-details__text"]/text()'
    }

    nonDecisionMethods = ["KO/TKO", "Submission", "Overturned", "DQ", "TKO - Doctor's Stoppage", "Could Not Continue"]

    decisionDetailsDict = {
        "judge1": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[2]/span//text()',
        "judge1RedPts": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[2]//text()[2]',
        "judge1BluePts": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[2]//text()[2]',
        "judge2": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[3]/span//text()',
        "judge2RedPts": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[3]//text()[2]',
        "judge2BluePts": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[3]//text()[2]',
        "judge3": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[4]/span//text()',
        "judge3RedPts": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[3]//text()[2]',
        "judge3BluePts": '//html/body/section/div/div/div[2]/div[2]/p[2]/i[3]//text()[2]',
    }

    def ttl_fight_time(self, roundFinish, timeFinish):
        fullRounds = int(roundFinish) - 1
        finishRoundMinute = int(timeFinish[0])
        finishRoundSeconds = int(timeFinish[2:4])
        fightTime = (fullRounds * 5) + (finishRoundMinute) + (finishRoundSeconds / 60)
        return fightTime

#"numRoundFormat":response.xpath('//html/body/section/div/div/div[2]/div[2]/p[1]/i[4]//text()[2]').get().replace("\n","").strip()[0]

#"finishDetails": response.xpath('//p[@class="b-fight-details__text"]/text()').extract()[-2].strip()