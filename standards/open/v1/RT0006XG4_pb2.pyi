"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.type.date_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RT0006XG4(google.protobuf.message.Message):
    """Share Class Unit Price"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EFFECTIVE_DATE_FIELD_NUMBER: builtins.int
    UMBRELLA_FUND_FIELD_NUMBER: builtins.int
    INTERNAL_UMBRELLA_ID_FIELD_NUMBER: builtins.int
    FUND_FIELD_NUMBER: builtins.int
    INTERNAL_FUND_ID_FIELD_NUMBER: builtins.int
    FUND_CURRENCY_FIELD_NUMBER: builtins.int
    SHARE_CLASS_EXTENSION_FIELD_NUMBER: builtins.int
    INTERNAL_SHARE_CLASS_ID_FIELD_NUMBER: builtins.int
    EXTERNAL_SHARE_CLASS_ID_ISIN_FIELD_NUMBER: builtins.int
    EXTERNAL_SHARE_CLASS_ID_CUSIP_FIELD_NUMBER: builtins.int
    EXTERNAL_SHARE_CLASS_ID_SEDOL_FIELD_NUMBER: builtins.int
    EXTERNAL_SHARE_CLASS_ID_FIGI_FIELD_NUMBER: builtins.int
    EXTERNAL_SHARE_CLASS_ID_PERMID_FIELD_NUMBER: builtins.int
    EXTERNAL_EXCHANGE_ID_MIC_FIELD_NUMBER: builtins.int
    EXTERNAL_EXCHANGE_ID_BB_EXCHANGE_CODE_FIELD_NUMBER: builtins.int
    NAV_PER_SHARE_FIELD_NUMBER: builtins.int
    PRIOR_NAV_PER_SHARE_FIELD_NUMBER: builtins.int
    TOTAL_NET_ASSETS_FIELD_NUMBER: builtins.int
    SHARES_OUTSTANDING_FIELD_NUMBER: builtins.int
    @property
    def effective_date(self) -> google.type.date_pb2.Date:
        """The effective date of the holding.
        The holdings are as of market close on the effective date
        """
    umbrella_fund: builtins.str
    """The legal identifier of the umbrella
    Should conform to: https://openfunds.org/OFST005010 (Umbrella)
    See: https://openfunds.org/knowledge/whitepapers/fundnames/ for more information
    """
    internal_umbrella_id: builtins.str
    """The internal umbrella ID used by the system producing the data"""
    fund: builtins.str
    """Name of the relevant sub-fund
    Should conform to: https://openfunds.org/OFST010110 (Legal Fund Name Only)
    Refers to the Sub-Fund in the case of an umbrella structure
    or Fund in the case of a standalone structure
    See: https://openfunds.org/knowledge/whitepapers/fundnames/ for more information
    """
    internal_fund_id: builtins.str
    """The internal fund ID used by the system producing the data"""
    fund_currency: builtins.str
    """The ISO compliant three character code for the base currency of the fund"""
    share_class_extension: builtins.str
    """Extension that identifies the share class.
    Should conform to: https://openfunds.org/OFST020050 (Share Class Extension)
    """
    internal_share_class_id: builtins.str
    """The internal share class ID used by the system producing the data"""
    external_share_class_id_isin: builtins.str
    """ISO 6166 code of ISIN when available. If an ISIN is used, it is recommended that the MIC or Bloomberg Exchange Code should additionally be populated. This combination allows for a fund holding to be uniquely identified."""
    external_share_class_id_cusip: builtins.str
    """CUSIP - The Committee on Uniform Securities Identification Procedures number assigned by the CUSIP Service Bureau for U.S. and Canadian companies when available. If a CUSIP is used, it is recommended that the MIC or Bloomberg Exchange Code should additionally be populated. This combination allows for a fund holding to be uniquely identified."""
    external_share_class_id_sedol: builtins.str
    """SEDOL - Stock Exchange Daily Official List for the London Stock Exchange (when available). If a SEDOL is used, it is recommended that the MIC or Bloomberg Exchange Code should additionally be populated. This combination allows for a fund holding to be uniquely identified."""
    external_share_class_id_figi: builtins.str
    """FIGI - Financial_Instrument Global Identifier (when available)"""
    external_share_class_id_permid: builtins.str
    """PermID - Refinitiv Permanent Identifiers (when available)"""
    external_exchange_id_mic: builtins.str
    """MIC - Market identifier code as defined by ISO 10383 (available at https://www.iso20022.org/market-identifier-codes) (when available)"""
    external_exchange_id_bb_exchange_code: builtins.str
    """Bloomberg Exchange Code - Two digit market identifier code as defined by Bloomberg (when available)"""
    nav_per_share: builtins.float
    """The NAV per share on the effective date"""
    prior_nav_per_share: builtins.float
    """The NAV per share on the prior effective date"""
    total_net_assets: builtins.float
    """The total net assets attributed to the share class"""
    shares_outstanding: builtins.float
    """The total shares outstanding per class"""
    def __init__(
        self,
        *,
        effective_date: google.type.date_pb2.Date | None = ...,
        umbrella_fund: builtins.str = ...,
        internal_umbrella_id: builtins.str = ...,
        fund: builtins.str = ...,
        internal_fund_id: builtins.str = ...,
        fund_currency: builtins.str = ...,
        share_class_extension: builtins.str = ...,
        internal_share_class_id: builtins.str = ...,
        external_share_class_id_isin: builtins.str = ...,
        external_share_class_id_cusip: builtins.str = ...,
        external_share_class_id_sedol: builtins.str = ...,
        external_share_class_id_figi: builtins.str = ...,
        external_share_class_id_permid: builtins.str = ...,
        external_exchange_id_mic: builtins.str = ...,
        external_exchange_id_bb_exchange_code: builtins.str = ...,
        nav_per_share: builtins.float = ...,
        prior_nav_per_share: builtins.float = ...,
        total_net_assets: builtins.float = ...,
        shares_outstanding: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["effective_date", b"effective_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["effective_date", b"effective_date", "external_exchange_id_bb_exchange_code", b"external_exchange_id_bb_exchange_code", "external_exchange_id_mic", b"external_exchange_id_mic", "external_share_class_id_cusip", b"external_share_class_id_cusip", "external_share_class_id_figi", b"external_share_class_id_figi", "external_share_class_id_isin", b"external_share_class_id_isin", "external_share_class_id_permid", b"external_share_class_id_permid", "external_share_class_id_sedol", b"external_share_class_id_sedol", "fund", b"fund", "fund_currency", b"fund_currency", "internal_fund_id", b"internal_fund_id", "internal_share_class_id", b"internal_share_class_id", "internal_umbrella_id", b"internal_umbrella_id", "nav_per_share", b"nav_per_share", "prior_nav_per_share", b"prior_nav_per_share", "share_class_extension", b"share_class_extension", "shares_outstanding", b"shares_outstanding", "total_net_assets", b"total_net_assets", "umbrella_fund", b"umbrella_fund"]) -> None: ...

global___RT0006XG4 = RT0006XG4

@typing_extensions.final
class RT0006XG4_batch(google.protobuf.message.Message):
    """Batch set of RT0006XG4 responses"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def response(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RT0006XG4]: ...
    def __init__(
        self,
        *,
        response: collections.abc.Iterable[global___RT0006XG4] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["response", b"response"]) -> None: ...

global___RT0006XG4_batch = RT0006XG4_batch
