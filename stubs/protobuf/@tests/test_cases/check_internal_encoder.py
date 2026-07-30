from collections.abc import Callable
from typing_extensions import assert_type

from google.protobuf.internal import encoder

_Encoder = Callable[[Callable[[bytes], int], bytes, bool], int]

encoder.Int32Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.Int64Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.EnumEncoder(field_number=1, is_repeated=False, is_packed=False)
encoder.UInt32Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.UInt64Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.SInt32Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.SInt64Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.Fixed32Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.Fixed64Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.SFixed32Encoder(field_number=1, is_repeated=False, is_packed=False)
encoder.SFixed64Encoder(field_number=1, is_repeated=False, is_packed=False)
assert_type(encoder.FloatEncoder(field_number=1, is_repeated=False, is_packed=False), _Encoder)
encoder.DoubleEncoder(field_number=1, is_repeated=False, is_packed=False)
