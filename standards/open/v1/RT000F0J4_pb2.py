# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RT000F0J4.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fRT000F0J4.proto\x12\x11standards.open.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto\"\xe3o\n\tRT000F0J4\x12`\n\x13\x64\x61taset_information\x18\x01 \x01(\x0b\x32/.standards.open.v1.RT000F0J4.DatasetInformationR\x12\x64\x61tasetInformation\x12o\n\x18manufacturer_information\x18\x02 \x01(\x0b\x32\x34.standards.open.v1.RT000F0J4.ManufacturerInformationR\x17manufacturerInformation\x12`\n\x17per_product_information\x18\x03 \x03(\x0b\x32(.standards.open.v1.RT000F0J4.ProductDataR\x15perProductInformation\x1a\xa9\x05\n\x12\x44\x61tasetInformation\x12[\n\x0b\x65\x65t_version\x18\x01 \x01(\x0e\x32:.standards.open.v1.RT000F0J4.DatasetInformation.EETVersionR\neetVersion\x12#\n\rproducer_name\x18\x02 \x01(\tR\x0cproducerName\x12!\n\x0cproducer_lei\x18\x03 \x01(\tR\x0bproducerLei\x12%\n\x0eproducer_email\x18\x04 \x01(\tR\rproducerEmail\x12V\n\x19\x66ile_generation_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x17\x66ileGenerationTimestamp\x12L\n#data_reporting_sfdr_pre_contractual\x18\x06 \x01(\x08R\x1f\x64\x61taReportingSfdrPreContractual\x12?\n\x1c\x64\x61ta_reporting_sfdr_periodic\x18\x07 \x01(\x08R\x19\x64\x61taReportingSfdrPeriodic\x12\x46\n data_reporting_sfdr_entity_level\x18\x08 \x01(\x08R\x1c\x64\x61taReportingSfdrEntityLevel\x12\x30\n\x14\x64\x61ta_reporting_mifid\x18\t \x01(\x08R\x12\x64\x61taReportingMifid\x12,\n\x12\x64\x61ta_reporting_idd\x18\n \x01(\x08R\x10\x64\x61taReportingIdd\"8\n\nEETVersion\x12\x1b\n\x17\x45\x45T_VERSION_UNSPECIFIED\x10\x00\x12\r\n\tVERSION_1\x10\x01\x1a\x94\t\n\x17ManufacturerInformation\x12+\n\x11manufacturer_name\x18\x01 \x01(\tR\x10manufacturerName\x12\x7f\n\x16manufacturer_code_type\x18\x02 \x01(\x0e\x32I.standards.open.v1.RT000F0J4.ManufacturerInformation.ManufacturerCodeTypeR\x14manufacturerCodeType\x12+\n\x11manufacturer_code\x18\x03 \x01(\tR\x10manufacturerCode\x12-\n\x12manufacturer_email\x18\x04 \x01(\tR\x11manufacturerEmail\x12G\n\x16general_reference_date\x18\x05 \x01(\x0b\x32\x11.google.type.DateR\x14generalReferenceDate\x12H\n!manufacturer_pri_or_prb_signatory\x18\x06 \x01(\x08R\x1dmanufacturerPriOrPrbSignatory\x12:\n\x19manufacturer_pri_notation\x18\x07 \x01(\tR\x17manufacturerPriNotation\x12<\n\x1amanufacturer_pri_compliant\x18\x08 \x01(\x08R\x18manufacturerPriCompliant\x12\x32\n\x15manufacturer_pri_like\x18\t \x01(\x08R\x13manufacturerPriLike\x12m\n\x11other_commitments\x18\n \x01(\x0e\x32@.standards.open.v1.RT000F0J4.ManufacturerInformation.CommitmentsR\x10otherCommitments\x12~\n\x1astewardship_code_signatory\x18\x0b \x01(\x0e\x32@.standards.open.v1.RT000F0J4.ManufacturerInformation.CommitmentsR\x18stewardshipCodeSignatory\x12{\n;manufacturer_website_information_stewardship_and_engagement\x18\x0c \x01(\tR6manufacturerWebsiteInformationStewardshipAndEngagement\"5\n\x14ManufacturerCodeType\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03LEI\x10\x01\"\x8a\x01\n\x0b\x43ommitments\x12\x1b\n\x17\x43OMMITMENTS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41_TCFD\x10\x01\x12\x11\n\rB_NZAMI_NZAOA\x10\x02\x12\x10\n\x0c\x43_SBT_FOR_FI\x10\x03\x12\x16\n\x12\x44_STEWARDSHIP_CODE\x10\x04\x12\n\n\x06\x45_UNGC\x10\x05\x12\t\n\x05\x46_CDP\x10\x06\x1a\xdd^\n\x0bProductData\x12u\n\x16product_identification\x18\x01 \x01(\x0b\x32>.standards.open.v1.RT000F0J4.ProductData.ProductIdentificationR\x15productIdentification\x12s\n\x16\x65sg_screening_criteria\x18\x02 \x01(\x0b\x32=.standards.open.v1.RT000F0J4.ProductData.ESGScreeningCriteriaR\x14\x65sgScreeningCriteria\x12l\n\x13product_disclosures\x18\x03 \x01(\x0b\x32;.standards.open.v1.RT000F0J4.ProductData.ProductDisclosuresR\x12productDisclosures\x1a\xee\x04\n\x15ProductIdentification\x12#\n\rumbrella_fund\x18\x01 \x01(\tR\x0cumbrellaFund\x12\x1b\n\tfund_name\x18\x02 \x01(\tR\x08\x66undName\x12n\n\rshare_classes\x18\x03 \x03(\x0b\x32I.standards.open.v1.RT000F0J4.ProductData.ProductIdentification.ShareClassR\x0cshareClasses\x1a\xa2\x03\n\nShareClass\x12\x32\n\x15share_class_extension\x18\x01 \x01(\tR\x13shareClassExtension\x12$\n\x0eshare_class_id\x18\x02 \x01(\tR\x0cshareClassId\x12\x92\x01\n\x13share_class_id_type\x18\x03 \x01(\x0e\x32\x63.standards.open.v1.RT000F0J4.ProductData.ProductIdentification.ShareClass.ShareClassIdentifierTypesR\x10shareClassIdType\"\xa4\x01\n\x19ShareClassIdentifierTypes\x12\x1a\n\x16IDENTIFIER_UNSPECIFIED\x10\x00\x12\x08\n\x04ISIN\x10\x01\x12\t\n\x05\x43USIP\x10\x02\x12\t\n\x05SEDOL\x10\x03\x12\x07\n\x03WKN\x10\x04\x12\x0e\n\nBBG_TICKER\x10\x05\x12\t\n\x05\x42\x42GID\x10\x06\x12\x07\n\x03RIC\x10\x07\x12\x08\n\x04\x46IGI\x10\x08\x12\x07\n\x03LEI\x10\t\x12\x0b\n\x07PERM_ID\x10\n\x1a\xe5\x0c\n\x14\x45SGScreeningCriteria\x12y\n\x11sfdr_product_type\x18\x07 \x01(\x0e\x32M.standards.open.v1.RT000F0J4.ProductData.ESGScreeningCriteria.SFDRProductTypeR\x0fsfdrProductType\x12\x65\n\nesg_labels\x18\x08 \x03(\x0e\x32\x46.standards.open.v1.RT000F0J4.ProductData.ESGScreeningCriteria.ESGLabelR\tesgLabels\x12J\n#fund_of_fund_min_exposure_article_8\x18\t \x01(\x01R\x1d\x66undOfFundMinExposureArticle8\x12J\n#fund_of_fund_min_exposure_article_9\x18\n \x01(\x01R\x1d\x66undOfFundMinExposureArticle9\x12r\n\x0emain_esg_focus\x18\x0b \x03(\x0e\x32L.standards.open.v1.RT000F0J4.ProductData.ESGScreeningCriteria.MainFocusAreasR\x0cmainEsgFocus\x12%\n\x0epai_considered\x18\x0c \x01(\x08R\rpaiConsidered\"\xc6\x01\n\x0fSFDRProductType\x12#\n\x1f\x44OES_NOT_FOLLOW_SFDR_GUIDELINES\x10\x00\x12 \n\x1c\x46OLLOWS_ARTICLE_6_GUIDELINES\x10\x01\x12\x12\n\x0e\x41RTICLE_8_LIKE\x10\x02\x12\x12\n\x0e\x41RTICLE_9_LIKE\x10\x03\x12\x16\n\x12NOT_ARTICLE_8_OR_9\x10\x04\x12\x15\n\x11\x41RTICLE_8_PRODUCT\x10\x05\x12\x15\n\x11\x41RTICLE_9_PRODUCT\x10\x06\"\x94\x06\n\x08\x45SGLabel\x12\x19\n\x15\x45SG_LABEL_UNSPECIFIED\x10\x00\x12 \n\x1c\x41_ICMA_GREEN_BOND_PRINCIPLES\x10\x01\x12\x1c\n\x18\x42_EU_GREEN_BOND_STANDARD\x10\x02\x12(\n$C_EU_ECOLABEL_FOR_FINANCIAL_PRODUCTS\x10\x03\x12\x15\n\x11\x44_FNG_SIEGEL_FOND\x10\x04\x12!\n\x1d\x45_CBI_CLIMATE_BONDS_STANDARDS\x10\x05\x12\"\n\x1e\x46_ICMA_SOCIAL_BONDS_PRINCIPLES\x10\x06\x12\x11\n\rG_LUXFLAG_ESG\x10\x07\x12\x1d\n\x19H_LUXFLAG_CLIMATE_FINANCE\x10\x08\x12\x19\n\x15I_LUXFLAG_ENVIRONMENT\x10\t\x12\x30\n,J_KEIN_VERSTOSS_GEGEN_ATOMWAFFENSPERRVERTRAG\x10\n\x12\t\n\x05K_ISR\x10\x0b\x12\x1c\n\x18L_TOWARDS_SUSTAINABILITY\x10\x0c\x12,\n(M_UZ49_DAS_OSTERREICHISCHE_UMWELTZEICHEN\x10\r\x12\x11\n\rN_NORDIC_SWAN\x10\x0e\x12\x14\n\x10O_GREENFIN_LABEL\x10\x0f\x12\x0e\n\nP_FINANSOL\x10\x10\x12,\n(Q_DDV_NACHHALTIGKEITSKODEX_ESG_STRATEGIE\x10\x11\x12)\n%R_DDV_NACHHALTIGKEITSKODEX_ESG_IMPACT\x10\x12\x12\x17\n\x13S_GRUNER_PFANDBRIEF\x10\x13\x12\x19\n\x15T_SOZIALER_PFANDBRIEF\x10\x14\x12\x1a\n\x16U_LUXFLAG_MICROFINANCE\x10\x15\x12,\n(V_LUXFLAG_SUSTAINABLE_INSURANCE_PRODUCTS\x10\x16\x12\x32\n.X_CHARTE_ESG_FRANCAISE_DES_PRODUITS_STRUCTURES\x10\x17\x12\x0b\n\x07Z_OTHER\x10\x63\"X\n\x0eMainFocusAreas\x12\x15\n\x11\x46OCUS_UNSPECIFIED\x10\x00\x12\x11\n\rENVIRONMENTAL\x10\x01\x12\n\n\x06SOCIAL\x10\x02\x12\x10\n\x0cGOVERNMENTAL\x10\x03\x1a\x89\x05\n\x12ProductDisclosures\x12\x1c\n\tlanguages\x18\x01 \x03(\tR\tlanguages\x12\xc5\x01\n7pre_contractual_disclosure_for_financial_products_links\x18\x02 \x03(\x0b\x32Q.standards.open.v1.RT000F0J4.ProductData.ProductDisclosures.ProductDisclosureLinkR1preContractualDisclosureForFinancialProductsLinks\x12\x8d\x01\n\x19periodic_disclosure_links\x18\x03 \x03(\x0b\x32Q.standards.open.v1.RT000F0J4.ProductData.ProductDisclosures.ProductDisclosureLinkR\x17periodicDisclosureLinks\x12w\n0end_of_reporting_period_for_periodic_disclosures\x18\x04 \x01(\x0b\x32\x11.google.type.DateR*endOfReportingPeriodForPeriodicDisclosures\x1a\x83\x01\n\x15ProductDisclosureLink\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12\x12\n\x04link\x18\x02 \x01(\tR\x04link\x12:\n\x0fproduction_date\x18\x03 \x01(\x0b\x32\x11.google.type.DateR\x0eproductionDate\x1a\x8e\x45\n\x1b\x41rticle8Article9Information\x12m\n5does_article_8_fund_invest_in_sustainable_investments\x18\x01 \x01(\x08R.doesArticle8FundInvestInSustainableInvestments\x12{\n<article_8_fund_minimum_proportion_of_sustainable_investments\x18\x02 \x01(\x01R5article8FundMinimumProportionOfSustainableInvestments\x12~\n>does_article_8_min_investments_include_eu_taxonomy_investments\x18\x03 \x01(\x08R6doesArticle8MinInvestmentsIncludeEuTaxonomyInvestments\x12\x85\x01\nBdoes_article_8_min_investments_include_non_eu_taxonomy_investments\x18\x04 \x01(\x08R9doesArticle8MinInvestmentsIncludeNonEuTaxonomyInvestments\x12\x7f\n>does_min_investments_include_investments_with_social_objective\x18\x05 \x01(\x08R7doesMinInvestmentsIncludeInvestmentsWithSocialObjective\x12\x7f\n>article_9_fund_minimum_proportion_of_environmental_investments\x18\x06 \x01(\x01R7article9FundMinimumProportionOfEnvironmentalInvestments\x12~\n>does_article_9_min_investments_include_eu_taxonomy_investments\x18\x07 \x01(\x08R6doesArticle9MinInvestmentsIncludeEuTaxonomyInvestments\x12\x85\x01\nBdoes_article_9_min_investments_include_non_eu_taxonomy_investments\x18\x08 \x01(\x08R9doesArticle9MinInvestmentsIncludeNonEuTaxonomyInvestments\x12q\n7article_9_fund_minimum_proportion_of_social_investments\x18\t \x01(\x01R0article9FundMinimumProportionOfSocialInvestments\x12+\n\x11thematic_approach\x18\n \x01(\x08R\x10thematicApproach\x12\x8b\x01\n\x14\x65nvironmental_themes\x18\x0b \x03(\x0e\x32X.standards.open.v1.RT000F0J4.ProductData.Article8Article9Information.EnvironmentalThemesR\x13\x65nvironmentalThemes\x12v\n\rsocial_themes\x18\x0c \x03(\x0e\x32Q.standards.open.v1.RT000F0J4.ProductData.Article8Article9Information.SocialThemesR\x0csocialThemes\x12\x82\x01\n\x11governance_themes\x18\r \x03(\x0e\x32U.standards.open.v1.RT000F0J4.ProductData.Article8Article9Information.GovernanceThemesR\x10governanceThemes\x12\xb2\x01\n#TargetedSustainableDevelopmentGoals\x18\x0e \x03(\x0e\x32`.standards.open.v1.RT000F0J4.ProductData.Article8Article9Information.SustainableDevelopmentGoalsR#TargetedSustainableDevelopmentGoals\x12\x36\n\x17weight_eligible_issuers\x18\x0f \x01(\x01R\x15weightEligibleIssuers\x12\x36\n\x17number_eligible_issuers\x18\x10 \x01(\x05R\x15numberEligibleIssuers\x12\x34\n\x16weight_covered_issuers\x18\x11 \x01(\x01R\x14weightCoveredIssuers\x12\x34\n\x16number_covered_issuers\x18\x12 \x01(\x05R\x14numberCoveredIssuers\x12\x34\n\x16weight_engaged_issuers\x18\x13 \x01(\x01R\x14weightEngagedIssuers\x12\x34\n\x16number_engaged_issuers\x18\x14 \x01(\x05R\x14numberEngagedIssuers\x12#\n\resg_benchmark\x18\x15 \x01(\x08R\x0c\x65sgBenchmark\x12,\n\x12\x65sg_benchmark_name\x18\x16 \x01(\tR\x10\x65sgBenchmarkName\x12(\n\x10\x65sg_benchmark_id\x18\x17 \x01(\tR\x0e\x65sgBenchmarkId\x12\x90\x01\n\x15\x65sg_benchmark_id_type\x18\x18 \x01(\x0e\x32].standards.open.v1.RT000F0J4.ProductData.Article8Article9Information.BenchmarkIdentifierTypesR\x12\x65sgBenchmarkIdType\x12]\n\"minimum_or_planned_allocation_date\x18\x19 \x01(\x0b\x32\x11.google.type.DateR\x1eminimumOrPlannedAllocationDate\x12\x98\x01\nKminimum_or_planned_investments_with_environmental_or_social_characteristics\x18\x1a \x01(\x01RCminimumOrPlannedInvestmentsWithEnvironmentalOrSocialCharacteristics\x12\xd2\x01\n-sustainable_investment_calculation_approaches\x18\x1b \x03(\x0e\x32o.standards.open.v1.RT000F0J4.ProductData.Article8Article9Information.SustainableInvestmentCalculationApproachesR*sustainableInvestmentCalculationApproaches\x12Z\n*minimum_or_planned_sustainable_investments\x18\x1c \x01(\x01R&minimumOrPlannedSustainableInvestments\x12\xa3\x01\nQminimum_or_planned_other_investments_with_environmental_or_social_characteristics\x18\x1d \x01(\x01RHminimumOrPlannedOtherInvestmentsWithEnvironmentalOrSocialCharacteristics\x12u\n8minimum_or_planned_sustainable_investments_environmental\x18\x1e \x01(\x01R3minimumOrPlannedSustainableInvestmentsEnvironmental\x12z\n;minimum_or_planned_sustainable_investments_taxonomy_aligned\x18\x1f \x01(\x01R5minimumOrPlannedSustainableInvestmentsTaxonomyAligned\x12\x80\x01\n>minimum_or_planned_sustainable_investments_other_environmental\x18  \x01(\x01R8minimumOrPlannedSustainableInvestmentsOtherEnvironmental\x12g\n1minimum_or_planned_sustainable_investments_social\x18! \x01(\x01R,minimumOrPlannedSustainableInvestmentsSocial\x12T\n\x1dlast_reported_allocation_date\x18\" \x01(\x0b\x32\x11.google.type.DateR\x1alastReportedAllocationDate\x12\x9d\x01\nNeu_sfdr_last_reported_investments_with_environmental_or_social_characteristics\x18# \x01(\x01REeuSfdrLastReportedInvestmentsWithEnvironmentalOrSocialCharacteristics\x12q\n7eu_sfdr_last_reported_investments_not_sustainable_other\x18$ \x01(\x01R0euSfdrLastReportedInvestmentsNotSustainableOther\x12_\n-eu_sfdr_last_reported_investments_sustainable\x18% \x01(\x01R(euSfdrLastReportedInvestmentsSustainable\x12\xa8\x01\nTeu_sfdr_last_reported_other_investments_with_environmental_or_social_characteristics\x18& \x01(\x01RJeuSfdrLastReportedOtherInvestmentsWithEnvironmentalOrSocialCharacteristics\x12z\n;eu_sfdr_last_reported_investments_sustainable_environmental\x18\' \x01(\x01R5euSfdrLastReportedInvestmentsSustainableEnvironmental\x12\x7f\n>eu_sfdr_last_reported_investments_sustainable_taxonomy_aligned\x18( \x01(\x01R7euSfdrLastReportedInvestmentsSustainableTaxonomyAligned\x12\x85\x01\nAeu_sfdr_last_reported_investments_sustainable_other_environmental\x18) \x01(\x01R:euSfdrLastReportedInvestmentsSustainableOtherEnvironmental\x12l\n4eu_sfdr_last_reported_investments_sustainable_social\x18* \x01(\x01R.euSfdrLastReportedInvestmentsSustainableSocial\x12T\n\'reduction_in_carbon_emissions_objective\x18+ \x01(\x08R#reductionInCarbonEmissionsObjective\x12?\n\x1c\x61ligned_with_paris_agreement\x18, \x01(\x08R\x19\x61lignedWithParisAgreement\x12\x62\n.consider_end_client_sustainability_preferences\x18- \x01(\x08R*considerEndClientSustainabilityPreferences\x12\x82\x01\n@minimum_percentage_aligned_with_eu_taxonomy_incl_sovereign_bonds\x18. \x01(\x01R8minimumPercentageAlignedWithEuTaxonomyInclSovereignBonds\x12\x82\x01\n@minimum_percentage_aligned_with_eu_taxonomy_excl_sovereign_bonds\x18/ \x01(\x01R8minimumPercentageAlignedWithEuTaxonomyExclSovereignBonds\x12@\n\x1dsubject_to_third_party_review\x18\x30 \x01(\x08R\x19subjectToThirdPartyReview\x12\xe1\x01\n6methodology_used_for_eu_taxonomy_alignment_calculation\x18\x31 \x01(\x0e\x32o.standards.open.v1.RT000F0J4.ProductData.Article8Article9Information.SustainableInvestmentCalculationApproachesR0methodologyUsedForEuTaxonomyAlignmentCalculation\x12Q\n%minimum_share_transitional_activities\x18\x32 \x01(\x01R\"minimumShareTransitionalActivities\x12I\n!minimum_share_enabling_activities\x18\x33 \x01(\x01R\x1eminimumShareEnablingActivities\x12i\n2percentage_taxonomy_aligned_incl_sovereign_revenue\x18\x34 \x01(\x01R-percentageTaxonomyAlignedInclSovereignRevenue\x12\x65\n0percentage_taxonomy_aligned_incl_sovereign_capex\x18\x35 \x01(\x01R+percentageTaxonomyAlignedInclSovereignCapex\x12\x63\n/percentage_taxonomy_aligned_incl_sovereign_opex\x18\x36 \x01(\x01R*percentageTaxonomyAlignedInclSovereignOpex\x12i\n2percentage_taxonomy_aligned_excl_sovereign_revenue\x18\x37 \x01(\x01R-percentageTaxonomyAlignedExclSovereignRevenue\x12\x65\n0percentage_taxonomy_aligned_excl_sovereign_capex\x18\x38 \x01(\x01R+percentageTaxonomyAlignedExclSovereignCapex\x12\x63\n/percentage_taxonomy_aligned_excl_sovereign_opex\x18\x39 \x01(\x01R*percentageTaxonomyAlignedExclSovereignOpex\x12o\n5percentage_taxonomy_aligned_climate_change_mitigation\x18: \x01(\x01R0percentageTaxonomyAlignedClimateChangeMitigation\x12k\n3percentage_taxonomy_aligned_climate_change_adaption\x18; \x01(\x01R.percentageTaxonomyAlignedClimateChangeAdaption\x12\xaf\x01\nXpercentage_taxonomy_aligned_sustainable_use_and_protection_of_water_and_marine_resources\x18< \x01(\x01RMpercentageTaxonomyAlignedSustainableUseAndProtectionOfWaterAndMarineResources\x12^\n,percentage_taxonomy_aligned_circular_economy\x18= \x01(\x01R(percentageTaxonomyAlignedCircularEconomy\x12|\n<percentage_taxonomy_aligned_pollution_prevention_and_control\x18> \x01(\x01R6percentageTaxonomyAlignedPollutionPreventionAndControl\x12\xab\x01\nUpercentage_taxonomy_aligned_protection_and_restoration_of_biodiversity_and_ecosystems\x18? \x01(\x01RLpercentageTaxonomyAlignedProtectionAndRestorationOfBiodiversityAndEcosystems\x12|\n<percentage_taxonomy_aligned_share_of_transitional_activities\x18@ \x01(\x01R6percentageTaxonomyAlignedShareOfTransitionalActivities\x12t\n8percentage_taxonomy_aligned_share_of_enabling_activities\x18\x41 \x01(\x01R2percentageTaxonomyAlignedShareOfEnablingActivities\"\xff\x01\n\x13\x45nvironmentalThemes\x12#\n\x1f\x45NVIRONMENTAL_THEME_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x41_ENERGY\x10\x01\x12\x16\n\x12\x42_RENEWABLE_ENERGY\x10\x02\x12\x13\n\x0f\x43_RAW_MATERIALS\x10\x03\x12\x14\n\x10\x44_WATER_AND_LAND\x10\x04\x12\x0b\n\x07\x45_WASTE\x10\x05\x12\x1e\n\x1a\x46_GREENHOUSE_GAS_EMISSIONS\x10\x06\x12\x12\n\x0eG_BIODIVERSITY\x10\x07\x12\x16\n\x12H_CIRCULAR_ECONOMY\x10\x08\x12\x19\n\x15I_ENVIRONMENTAL_OTHER\x10\t\"\xf8\x01\n\x0cSocialThemes\x12\x1c\n\x18SOCIAL_THEME_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x41_INEQUALITY\x10\x01\x12\x15\n\x11\x42_SOCIAL_COHESION\x10\x02\x12\x18\n\x14\x43_SOCIAL_INTEGRATION\x10\x03\x12\x16\n\x12\x44_LABOUR_RELATIONS\x10\x04\x12!\n\x1d\x45_INVESTMENT_IN_HUMAN_CAPITAL\x10\x05\x12\x38\n4F_ECONOMICALLY_OR_SOCIALLY_DISADVANTAGED_COMMUNITIES\x10\x06\x12\x12\n\x0eG_SOCIAL_OTHER\x10\x07\"\xbb\x01\n\x10GovernanceThemes\x12 \n\x1cGOVERNANCE_THEME_UNSPECIFIED\x10\x00\x12!\n\x1d\x41_SOUND_MANAGEMENT_STRUCTURES\x10\x01\x12\x18\n\x14\x42_EMPLOYEE_RELATIONS\x10\x02\x12\x1b\n\x17\x43_RENUMERATION_OF_STAFF\x10\x03\x12\x14\n\x10\x44_TAX_COMPLIANCE\x10\x04\x12\x15\n\x11\x45_GOVERANCE_OTHER\x10\x05\"\xc6\x04\n\x1bSustainableDevelopmentGoals\x12\x13\n\x0fSDG_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x41_NO_POVERTY\x10\x01\x12\x0f\n\x0b\x42_NO_HUNGER\x10\x02\x12\x1f\n\x1b\x43_GOOD_HEALTH_AND_WELLBEING\x10\x03\x12\x17\n\x13\x44_QUALITY_EDUCATION\x10\x04\x12\x15\n\x11\x45_GENDER_EQUALITY\x10\x05\x12 \n\x1c\x46_CLEAN_WATER_AND_SANITATION\x10\x06\x12!\n\x1dG_AFFORDABLE_AND_CLEAN_ENERGY\x10\x07\x12%\n!H_DECENT_WORK_AND_ECONOMIC_GROWTH\x10\x08\x12,\n(I_INDUSTRY_INNOVATION_AND_INFRASTRUCTURE\x10\t\x12\x18\n\x14J_REDUCED_INEQUALITY\x10\n\x12(\n$K_SUSTAINABLE_CITIES_AND_COMMUNITIES\x10\x0b\x12,\n(L_RESPONSIBLE_CONSUMPTION_AND_PRODUCTION\x10\x0c\x12\x14\n\x10M_CLIMATE_ACTION\x10\r\x12\x16\n\x12N_LIFE_BELOW_WATER\x10\x0e\x12\x12\n\x0eO_LIFE_ON_LAND\x10\x0f\x12+\n\'P_PEACE_AND_JUSTICE_STRONG_INSTITUTIONS\x10\x10\x12#\n\x1fQ_PARTNERSHIPS_TO_ACHIEVE_GOALS\x10\x11\"`\n\x18\x42\x65nchmarkIdentifierTypes\x12\x1a\n\x16IDENTIFIER_UNSPECIFIED\x10\x00\x12\x08\n\x04ISIN\x10\x01\x12\x07\n\x03RIC\x10\x02\x12\x08\n\x04\x46IGI\x10\x03\x12\x0b\n\x07PERM_ID\x10\x04\"t\n*SustainableInvestmentCalculationApproaches\x12$\n CALCULATION_APPROACH_UNSPECIFIED\x10\x00\x12\x0b\n\x07REVENUE\x10\x01\x12\t\n\x05\x43\x41PEX\x10\x02\x12\x08\n\x04OPEX\x10\x03\"K\n\x0fRT000F0J4_batch\x12\x38\n\x08response\x18\x01 \x03(\x0b\x32\x1c.standards.open.v1.RT000F0J4R\x08responseB2Z0go.protobuf.standards.exchange/standards/open/v1b\x06proto3')



_RT000F0J4 = DESCRIPTOR.message_types_by_name['RT000F0J4']
_RT000F0J4_DATASETINFORMATION = _RT000F0J4.nested_types_by_name['DatasetInformation']
_RT000F0J4_MANUFACTURERINFORMATION = _RT000F0J4.nested_types_by_name['ManufacturerInformation']
_RT000F0J4_PRODUCTDATA = _RT000F0J4.nested_types_by_name['ProductData']
_RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION = _RT000F0J4_PRODUCTDATA.nested_types_by_name['ProductIdentification']
_RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS = _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION.nested_types_by_name['ShareClass']
_RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA = _RT000F0J4_PRODUCTDATA.nested_types_by_name['ESGScreeningCriteria']
_RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES = _RT000F0J4_PRODUCTDATA.nested_types_by_name['ProductDisclosures']
_RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES_PRODUCTDISCLOSURELINK = _RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES.nested_types_by_name['ProductDisclosureLink']
_RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION = _RT000F0J4_PRODUCTDATA.nested_types_by_name['Article8Article9Information']
_RT000F0J4_BATCH = DESCRIPTOR.message_types_by_name['RT000F0J4_batch']
_RT000F0J4_DATASETINFORMATION_EETVERSION = _RT000F0J4_DATASETINFORMATION.enum_types_by_name['EETVersion']
_RT000F0J4_MANUFACTURERINFORMATION_MANUFACTURERCODETYPE = _RT000F0J4_MANUFACTURERINFORMATION.enum_types_by_name['ManufacturerCodeType']
_RT000F0J4_MANUFACTURERINFORMATION_COMMITMENTS = _RT000F0J4_MANUFACTURERINFORMATION.enum_types_by_name['Commitments']
_RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS_SHARECLASSIDENTIFIERTYPES = _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS.enum_types_by_name['ShareClassIdentifierTypes']
_RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_SFDRPRODUCTTYPE = _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA.enum_types_by_name['SFDRProductType']
_RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_ESGLABEL = _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA.enum_types_by_name['ESGLabel']
_RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_MAINFOCUSAREAS = _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA.enum_types_by_name['MainFocusAreas']
_RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_ENVIRONMENTALTHEMES = _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION.enum_types_by_name['EnvironmentalThemes']
_RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SOCIALTHEMES = _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION.enum_types_by_name['SocialThemes']
_RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_GOVERNANCETHEMES = _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION.enum_types_by_name['GovernanceThemes']
_RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SUSTAINABLEDEVELOPMENTGOALS = _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION.enum_types_by_name['SustainableDevelopmentGoals']
_RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_BENCHMARKIDENTIFIERTYPES = _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION.enum_types_by_name['BenchmarkIdentifierTypes']
_RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SUSTAINABLEINVESTMENTCALCULATIONAPPROACHES = _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION.enum_types_by_name['SustainableInvestmentCalculationApproaches']
RT000F0J4 = _reflection.GeneratedProtocolMessageType('RT000F0J4', (_message.Message,), {

  'DatasetInformation' : _reflection.GeneratedProtocolMessageType('DatasetInformation', (_message.Message,), {
    'DESCRIPTOR' : _RT000F0J4_DATASETINFORMATION,
    '__module__' : 'RT000F0J4_pb2'
    # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.DatasetInformation)
    })
  ,

  'ManufacturerInformation' : _reflection.GeneratedProtocolMessageType('ManufacturerInformation', (_message.Message,), {
    'DESCRIPTOR' : _RT000F0J4_MANUFACTURERINFORMATION,
    '__module__' : 'RT000F0J4_pb2'
    # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ManufacturerInformation)
    })
  ,

  'ProductData' : _reflection.GeneratedProtocolMessageType('ProductData', (_message.Message,), {

    'ProductIdentification' : _reflection.GeneratedProtocolMessageType('ProductIdentification', (_message.Message,), {

      'ShareClass' : _reflection.GeneratedProtocolMessageType('ShareClass', (_message.Message,), {
        'DESCRIPTOR' : _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS,
        '__module__' : 'RT000F0J4_pb2'
        # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ProductData.ProductIdentification.ShareClass)
        })
      ,
      'DESCRIPTOR' : _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION,
      '__module__' : 'RT000F0J4_pb2'
      # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ProductData.ProductIdentification)
      })
    ,

    'ESGScreeningCriteria' : _reflection.GeneratedProtocolMessageType('ESGScreeningCriteria', (_message.Message,), {
      'DESCRIPTOR' : _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA,
      '__module__' : 'RT000F0J4_pb2'
      # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ProductData.ESGScreeningCriteria)
      })
    ,

    'ProductDisclosures' : _reflection.GeneratedProtocolMessageType('ProductDisclosures', (_message.Message,), {

      'ProductDisclosureLink' : _reflection.GeneratedProtocolMessageType('ProductDisclosureLink', (_message.Message,), {
        'DESCRIPTOR' : _RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES_PRODUCTDISCLOSURELINK,
        '__module__' : 'RT000F0J4_pb2'
        # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ProductData.ProductDisclosures.ProductDisclosureLink)
        })
      ,
      'DESCRIPTOR' : _RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES,
      '__module__' : 'RT000F0J4_pb2'
      # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ProductData.ProductDisclosures)
      })
    ,

    'Article8Article9Information' : _reflection.GeneratedProtocolMessageType('Article8Article9Information', (_message.Message,), {
      'DESCRIPTOR' : _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION,
      '__module__' : 'RT000F0J4_pb2'
      # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ProductData.Article8Article9Information)
      })
    ,
    'DESCRIPTOR' : _RT000F0J4_PRODUCTDATA,
    '__module__' : 'RT000F0J4_pb2'
    # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4.ProductData)
    })
  ,
  'DESCRIPTOR' : _RT000F0J4,
  '__module__' : 'RT000F0J4_pb2'
  # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4)
  })
_sym_db.RegisterMessage(RT000F0J4)
_sym_db.RegisterMessage(RT000F0J4.DatasetInformation)
_sym_db.RegisterMessage(RT000F0J4.ManufacturerInformation)
_sym_db.RegisterMessage(RT000F0J4.ProductData)
_sym_db.RegisterMessage(RT000F0J4.ProductData.ProductIdentification)
_sym_db.RegisterMessage(RT000F0J4.ProductData.ProductIdentification.ShareClass)
_sym_db.RegisterMessage(RT000F0J4.ProductData.ESGScreeningCriteria)
_sym_db.RegisterMessage(RT000F0J4.ProductData.ProductDisclosures)
_sym_db.RegisterMessage(RT000F0J4.ProductData.ProductDisclosures.ProductDisclosureLink)
_sym_db.RegisterMessage(RT000F0J4.ProductData.Article8Article9Information)

RT000F0J4_batch = _reflection.GeneratedProtocolMessageType('RT000F0J4_batch', (_message.Message,), {
  'DESCRIPTOR' : _RT000F0J4_BATCH,
  '__module__' : 'RT000F0J4_pb2'
  # @@protoc_insertion_point(class_scope:standards.open.v1.RT000F0J4_batch)
  })
_sym_db.RegisterMessage(RT000F0J4_batch)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0go.protobuf.standards.exchange/standards/open/v1'
  _RT000F0J4._serialized_start=274
  _RT000F0J4._serialized_end=14581
  _RT000F0J4_DATASETINFORMATION._serialized_start=597
  _RT000F0J4_DATASETINFORMATION._serialized_end=1278
  _RT000F0J4_DATASETINFORMATION_EETVERSION._serialized_start=1222
  _RT000F0J4_DATASETINFORMATION_EETVERSION._serialized_end=1278
  _RT000F0J4_MANUFACTURERINFORMATION._serialized_start=1281
  _RT000F0J4_MANUFACTURERINFORMATION._serialized_end=2453
  _RT000F0J4_MANUFACTURERINFORMATION_MANUFACTURERCODETYPE._serialized_start=2259
  _RT000F0J4_MANUFACTURERINFORMATION_MANUFACTURERCODETYPE._serialized_end=2312
  _RT000F0J4_MANUFACTURERINFORMATION_COMMITMENTS._serialized_start=2315
  _RT000F0J4_MANUFACTURERINFORMATION_COMMITMENTS._serialized_end=2453
  _RT000F0J4_PRODUCTDATA._serialized_start=2456
  _RT000F0J4_PRODUCTDATA._serialized_end=14581
  _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION._serialized_start=2818
  _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION._serialized_end=3440
  _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS._serialized_start=3022
  _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS._serialized_end=3440
  _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS_SHARECLASSIDENTIFIERTYPES._serialized_start=3276
  _RT000F0J4_PRODUCTDATA_PRODUCTIDENTIFICATION_SHARECLASS_SHARECLASSIDENTIFIERTYPES._serialized_end=3440
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA._serialized_start=3443
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA._serialized_end=5080
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_SFDRPRODUCTTYPE._serialized_start=4001
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_SFDRPRODUCTTYPE._serialized_end=4199
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_ESGLABEL._serialized_start=4202
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_ESGLABEL._serialized_end=4990
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_MAINFOCUSAREAS._serialized_start=4992
  _RT000F0J4_PRODUCTDATA_ESGSCREENINGCRITERIA_MAINFOCUSAREAS._serialized_end=5080
  _RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES._serialized_start=5083
  _RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES._serialized_end=5732
  _RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES_PRODUCTDISCLOSURELINK._serialized_start=5601
  _RT000F0J4_PRODUCTDATA_PRODUCTDISCLOSURES_PRODUCTDISCLOSURELINK._serialized_end=5732
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION._serialized_start=5735
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION._serialized_end=14581
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_ENVIRONMENTALTHEMES._serialized_start=13084
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_ENVIRONMENTALTHEMES._serialized_end=13339
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SOCIALTHEMES._serialized_start=13342
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SOCIALTHEMES._serialized_end=13590
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_GOVERNANCETHEMES._serialized_start=13593
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_GOVERNANCETHEMES._serialized_end=13780
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SUSTAINABLEDEVELOPMENTGOALS._serialized_start=13783
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SUSTAINABLEDEVELOPMENTGOALS._serialized_end=14365
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_BENCHMARKIDENTIFIERTYPES._serialized_start=14367
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_BENCHMARKIDENTIFIERTYPES._serialized_end=14463
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SUSTAINABLEINVESTMENTCALCULATIONAPPROACHES._serialized_start=14465
  _RT000F0J4_PRODUCTDATA_ARTICLE8ARTICLE9INFORMATION_SUSTAINABLEINVESTMENTCALCULATIONAPPROACHES._serialized_end=14581
  _RT000F0J4_BATCH._serialized_start=14583
  _RT000F0J4_BATCH._serialized_end=14658
# @@protoc_insertion_point(module_scope)
